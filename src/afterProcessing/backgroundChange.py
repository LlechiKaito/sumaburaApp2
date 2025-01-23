import cv2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from PIL import Image
import os

class BackgroundChange:
    def __init__(self, directory_input_path, stage_path, directory_output_path):
        self.directory_input_path = directory_input_path
        self.stage_path = stage_path
        self.directory_output_path = directory_output_path

        os.makedirs(self.directory_output_path, exist_ok=True)
        self.image_list = os.listdir(self.directory_input_path)
        
    def stage_display(self):

        # 画像を読み込む
        image = cv2.imread(self.stage_path) 
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # # 画像を表示
        # plt.figure(figsize=(8.54, 4.8), dpi=100)
        # plt.imshow(image)
        # plt.axis('off')
        # plt.show()
    
    def stage_resize(self):
        stageimage = Image.open(self.stage_path)
        stageimage = stageimage.resize((608, 342))
        stageimage.save("../../input/images/stage/resize/senjou.png")
    
    # def background_change(self):
    #     for image_name in self.image_list:
    #         # ステージ画像とキャラクター画像を読み込む
    #         stage_image = Image.open(self.stage_path)
    #         character_image = Image.open(os.path.join(self.directory_input_path, image_name))
            
    #         # NumPy配列に変換し、RGBモードに統一
    #         stage_array = np.array(stage_image.convert('RGB'))
    #         character_array = np.array(character_image.convert('RGB'))
            
    #         # キャラクター画像の黒い部分(背景)をステージ画像で置き換える
    #         mask = (character_array == 0).all(axis=2)
    #         result_array = np.where(mask[:, :, np.newaxis], stage_array, character_array)
            
    #         # PILイメージに戻す
    #         result_image = Image.fromarray(result_array.astype(np.uint8))
    #         result_image.save(os.path.join(self.directory_output_path, image_name))
            
    def background_change(self):
        # ディレクトリ内のすべての画像を処理
        for image_name in self.image_list:
            # 入力画像を読み込む
            img = cv2.imread(os.path.join(self.directory_input_path, image_name))
            stage_img = cv2.imread(self.stage_path)

            # 黒い部分を検出
            lower_black = np.array([0, 0, 0])
            upper_black = np.array([50, 50, 50])
            mask = cv2.inRange(img, lower_black, upper_black)

            # マスクを反転
            mask_inv = cv2.bitwise_not(mask)
            try:
                # マスクを使って元画像から黒以外の部分を抽出
                fg = cv2.bitwise_and(img, img, mask=mask_inv)

                # マスクを使って背景画像から黒い部分に入れる領域を抽出
                bg = cv2.bitwise_and(stage_img, stage_img, mask=mask)

            except(cv2.error):
                print(image_name)
                print(cv2.error, self.directory_input_path, "プログラムを終了します．")
                break

            # 前景と背景を合成
            result = cv2.add(fg, bg)

            # 結果を保存
            cv2.imwrite(os.path.join(self.directory_output_path, image_name), result)
    
    def run(self):
        self.background_change()

# コードの説明を書く予定