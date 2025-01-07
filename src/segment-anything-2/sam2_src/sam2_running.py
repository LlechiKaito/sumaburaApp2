import time

import os
import cv2
import torch
import numpy as np
import pandas as pd
from glob import glob
from natsort import natsorted

import matplotlib
matplotlib.use('TkAgg')  # または 'Qt5Agg' など

from PIL import Image

import matplotlib.pyplot as plt

from sam2.build_sam import build_sam2
from sam2.sam2_image_predictor import SAM2ImagePredictor
from sam2.build_sam import build_sam2_video_predictor

import smtplib
from email.mime.text import MIMEText

device = 'cuda' if torch.cuda.is_available() else 'cpu'

# use bfloat16 for the entire notebook
torch.autocast(device_type="cuda", dtype=torch.bfloat16).__enter__()

if torch.cuda.get_device_properties(0).major >= 8:
    # turn on tfloat32 for Ampere GPUs (https://pytorch.org/docs/stable/notes/cuda.html#tensorfloat-32-tf32-on-ampere-devices)
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True

# マスク描画用関数
def show_mask(mask, ax, obj_id=None):
    cmap = plt.get_cmap("tab10")
    cmap_idx = 0 if obj_id is None else obj_id
    color = np.array([*cmap(cmap_idx)[:3], 0.6])

    h, w = mask.shape[-2:]
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    ax.imshow(mask_image)

# プロンプト描画用関数
def show_points(coords, labels, ax, marker_size=375):
    pos_points = coords[labels==1]
    neg_points = coords[labels==0]
    ax.scatter(pos_points[:, 0], pos_points[:, 1], color='green', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)
    ax.scatter(neg_points[:, 0], neg_points[:, 1], color='red', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)

def run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label):

    # 出力ディレクトリが存在しない場合は作成
    os.makedirs(output_img_dir, exist_ok=True) 

    # 動画の最初のフレームを取得
    frame_names = natsorted(glob(f"{input_img_dir}/*.jpeg"))
    image = cv2.imread(frame_names[0])
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # モデルのロード （Large を使用）
    sam2_checkpoint = "checkpoints/sam2.1_hiera_large.pt"
    model_cfg = "configs/sam2.1/sam2.1_hiera_l.yaml"
    predictor = build_sam2_video_predictor(model_cfg, sam2_checkpoint)

    # 初期化 + 動画の各フレームの image embedding 求める
    inference_state = predictor.init_state(video_path=input_img_dir)

    # 先頭のフレームに対するセグメンテーション結果を確認

    ## キャラの座標をプロンプトとして指定
    ann_frame_idx = 0
    ann_obj_id = 1


    ## 指定したフレームに対する入力プロンプトのセグメンテーションを計算
    _, out_obj_ids, out_mask_logits = predictor.add_new_points(
        inference_state=inference_state,
        frame_idx=ann_frame_idx,
        obj_id=ann_obj_id,
        points=input_point,
        labels=input_label,
    )

    ## セグメンテーション結果を描画
    # plt.figure(figsize=(8.54, 4.8), dpi=100)
    image = cv2.imread(frame_names[ann_frame_idx])
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # plt.imshow(image)
    # show_points(input_point, input_label, plt.gca())
    # show_mask((out_mask_logits[0] > 0.0).cpu().numpy(), plt.gca(), obj_id=out_obj_ids[0])
    # plt.axis('on')
    # plt.show()

    # 以下が動画を作成する（コメント化しておいたほうがいい）
    # 自分で追加したもの
    # 動画の各フレームに対してセグメンテーションを実行
    video_segments = {}
    for out_frame_idx, out_obj_ids, out_mask_logits in predictor.propagate_in_video(inference_state):
        # 各オブジェクトのマスクを取得
        masks = {
            out_obj_id: (out_mask_logits[i] > 0.0).cpu().numpy()
            for i, out_obj_id in enumerate(out_obj_ids)
        }

        # 元のフレームを取得
        original_frame = cv2.imread(frame_names[out_frame_idx])
        original_frame = cv2.cvtColor(original_frame, cv2.COLOR_BGR2RGB)

        # 各マスクを適用して対象以外を黒にする
        for obj_id, mask in masks.items():
            # マスクをブール型に変換
            mask_bool = mask.astype(bool)

            # 対象以外を黒にする
            segmented_frame = original_frame * mask_bool[..., None]

            # 結果を保存
            video_segments[out_frame_idx] = segmented_frame

    for out_frame_idx in range(len(frame_names)):
        # セグメント化されたフレームの描画
        segmented_frame = video_segments[out_frame_idx]

        # 形状を確認し、必要に応じてスライス
        if segmented_frame.ndim == 4:
            segmented_frame = segmented_frame[0]  # 最初の要素を取得

        # PIL用に変換
        if segmented_frame.max() <= 1.0:
            segmented_frame = (segmented_frame * 255).astype(np.uint8)  # 0-1の範囲を0-255に変換

        # RGBの順序が正しいか確認
        if segmented_frame.shape[-1] == 3:  # RGBの場合
            image = Image.fromarray(segmented_frame, 'RGB')
        else:
            raise ValueError("Unexpected channel size, expected 3 for RGB.")

        # 背景を黒に設定し、指定したサイズにリサイズ
        background = Image.new("RGB", (854, 480), (0, 0, 0))
        background.paste(image, (0, 0))

        # 結果を保存
        basename = os.path.basename(frame_names[out_frame_idx])
        output_frame = os.path.join(output_img_dir, basename)
        background.save(output_frame)
            
        
# # 動画のパス設定
# input_img_dir = "../../input/images/B-air_0/resize"
# output_img_dir = "../../output/images/B-air_0/only_mask"
# output_video_path = "../../output/B-air_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[196, 264], [181, 234]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/B-throw_0/resize"
# output_img_dir = "../../output/images/B-throw_0/only_mask"
# output_video_path = "../../output/B-throw_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[287, 234]], dtype=np.float16)
# input_label = np.array([1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/D-air_0/resize"
# output_img_dir = "../../output/images/D-air_0/only_mask"
# output_video_path = "../../output/D-air_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[191, 240], [204, 273]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# 動画のパス設定
input_img_dir = "../../input/images/D-smash_0/resize"
output_img_dir = "../../output/images/D-smash_0/only_mask"
output_video_path = "../../output/D-smash_0_result.mp4" # 出力の動画ファイルパス
# ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
input_point = np.array([[113, 270], [141, 239]], dtype=np.float16)
input_label = np.array([1, 1], np.int16)

run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/D-throw_0/resize"
# output_img_dir = "../../output/images/D-throw_0/only_mask"
# output_video_path = "../../output/D-throw_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[246, 296]], dtype=np.float16)
# input_label = np.array([1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/D-tilt_0/resize"
# output_img_dir = "../../output/images/D-tilt_0/only_mask"
# output_video_path = "../../output/D-tilt_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[126, 238], [113, 274]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/DA_0/resize"
# output_img_dir = "../../output/images/DA_0/only_mask"
# output_video_path = "../../output/DA_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[129, 245], [140, 270]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/Down-B_0/resize"
# output_img_dir = "../../output/images/Down-B_0/only_mask"
# output_video_path = "../../output/Down-B_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[116, 243], [103, 275]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/F-air_0/resize"
# output_img_dir = "../../output/images/F-air_0/only_mask"
# output_video_path = "../../output/F-air_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[186, 239], [200, 275]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/F-smash_0/resize"
# output_img_dir = "../../output/images/F-smash_0/only_mask"
# output_video_path = "../../output/F-smash_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[129, 235], [117, 278]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/F-throw_0/resize"
# output_img_dir = "../../output/images/F-throw_0/only_mask"
# output_video_path = "../../output/F-throw_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[354, 277], [392, 215]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/F-tilt_0/resize"
# output_img_dir = "../../output/images/F-tilt_0/only_mask"
# output_video_path = "../../output/F-tilt_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[133, 235], [115, 269]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/Grab-blow_0/resize"
# output_img_dir = "../../output/images/Grab-blow_0/only_mask"
# output_video_path = "../../output/Grab-blow_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[300, 211], [256, 281]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/Jab_0/resize"
# output_img_dir = "../../output/images/Jab_0/only_mask"
# output_video_path = "../../output/Jab_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[130, 235], [109, 264]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/N-air_0/resize"
# output_img_dir = "../../output/images/N-air_0/only_mask"
# output_video_path = "../../output/N-air_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[126, 244], [109, 274]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/NB_0/resize"
# output_img_dir = "../../output/images/NB_0/only_mask"
# output_video_path = "../../output/NB_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[130, 235], [112, 277]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/Side-B_0/resize"
# output_img_dir = "../../output/images/Side-B_0/only_mask"
# output_video_path = "../../output/Side-B_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[125, 240], [111, 274]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/U-air_0/resize"
# output_img_dir = "../../output/images/U-air_0/only_mask"
# output_video_path = "../../output/U-air_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[178, 240], [195, 264]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/U-smash_0/resize"
# output_img_dir = "../../output/images/U-smash_0/only_mask"
# output_video_path = "../../output/U-smash_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[134, 232], [113, 265]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/U-throw_0/resize"
# output_img_dir = "../../output/images/U-throw_0/only_mask"
# output_video_path = "../../output/U-throw_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[325, 225], [285, 296]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/U-tilt_0/resize"
# output_img_dir = "../../output/images/U-tilt_0/only_mask"
# output_video_path = "../../output/U-tilt_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[130, 242], [109, 269]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)

# # 動画のパス設定
# input_img_dir = "../../input/images/Up-B_0/resize"
# output_img_dir = "../../output/images/Up-B_0/only_mask"
# output_video_path = "../../output/Up-B_0_result.mp4" # 出力の動画ファイルパス
# # ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
# input_point = np.array([[135, 239], [116, 277]], dtype=np.float16)
# input_label = np.array([1, 1], np.int16)

# run_sam2(input_img_dir, output_img_dir, output_video_path, input_point, input_label)