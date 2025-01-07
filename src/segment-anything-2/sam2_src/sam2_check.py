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

# 動画のパス設定
input_img_dir = "../../input/images/D-smash_0/resize"
output_img_dir = "../../output/images/D-smash_0/only_mask"
output_video_path = "../../output/D-smash_0_result.mp4" # 出力の動画ファイルパス

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
# ここの値によってマスク化される(sam2_pre_running.pyで値を確認する)
input_point = np.array([[113, 270], [141, 239]], dtype=np.float16)
input_label = np.array([1, 1], np.int16)

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
plt.imshow(image)
show_points(input_point, input_label, plt.gca())
show_mask((out_mask_logits[0] > 0.0).cpu().numpy(), plt.gca(), obj_id=out_obj_ids[0])
plt.axis('on')
plt.show()