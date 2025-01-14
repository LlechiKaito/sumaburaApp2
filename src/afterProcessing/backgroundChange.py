import cv2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from PIL import Image
import os

class BackgroundChange:
    def __init__(self, directory_input_path, stage_directory_path, directory_output_path):
        self.directory_input_path = directory_input_path
        self.stage_directory_path = stage_directory_path
        self.directory_output_path = directory_output_path

        os.makedirs(self.directory_output_path, exist_ok=True)
        os.makedirs(self.stage_directory_path, exist_ok=True)
        os.makedirs(self.directory_input_path, exist_ok=True)

        self.image_list = os.listdir(self.directory_input_path)
        
    def stage_display(self):

        # 画像を読み込む
        image = cv2.imread(self.stage_directory_path) 
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 画像を表示
        plt.figure(figsize=(8.54, 4.8), dpi=100)
        plt.imshow(image)
        plt.axis('off')
        plt.show()
    
    def stage_resize(self):
        stageimage = Image.open(self.stage_directory_path)
        stageimage = stageimage.resize((854, 480))
        stageimage.save(self.stage_directory_path)
    
    def background_change(self):
        for image_name in self.image_list:
            # ステージ画像とキャラクター画像を読み込む
            stage_image = Image.open(os.path.join(self.stage_directory_path, "senjou_resize.png"))
            character_image = Image.open(os.path.join(self.directory_input_path, image_name))
            
            # NumPy配列に変換し、RGBモードに統一
            stage_array = np.array(stage_image.convert('RGB'))
            character_array = np.array(character_image.convert('RGB'))
            
            # キャラクター画像の黒い部分(背景)をステージ画像で置き換える
            mask = (character_array == 0).all(axis=2)
            result_array = np.where(mask[:, :, np.newaxis], stage_array, character_array)
            
            # PILイメージに戻す
            result_image = Image.fromarray(result_array.astype(np.uint8))
            result_image.save(os.path.join(self.directory_output_path, image_name))
    
    # def remove_small_objects(self, num_labels_max=2):
    #     for image_name in self.image_list:
    #         # 画像を読み込む
    #         img = cv2.imread(os.path.join(self.directory_input_path, image_name))
            
    #         while True:
    #             gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #             # 2値化 (黒の範囲を調整: 閾値を10に設定)
    #             _, binary = cv2.threshold(gray_image, 10, 255, cv2.THRESH_BINARY)
                
    #             # ラベリング処理
    #             num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=4)
                
    #             if num_labels <= num_labels_max:
    #                 break

    #             # statsの5次元目(面積)を取得
    #             areas = stats[:, 4]
                
    #             # 面積の降順でインデックスを取得
    #             sorted_indices = np.argsort(areas)[::-1]
                
    #             # 背景(最大)と2番目の領域以外を黒(0)にするマスクを作成
    #             mask = np.zeros_like(labels, dtype=np.uint8)
    #             # 背景と最大オブジェクトのみ255に設定
    #             mask[labels == sorted_indices[0]] = 255  # 背景
    #             mask[labels == sorted_indices[1]] = 255  # 最大オブジェクト
                    
    #             # マスクを適用して結果を保存
    #             img = cv2.bitwise_and(img, img, mask=mask)

    #         cv2.imwrite(os.path.join(self.directory_input_path, image_name), img)
    
    def run(self):
        self.background_change()

# コードの説明を書く予定