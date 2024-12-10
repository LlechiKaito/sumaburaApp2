import cv2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from PIL import Image

class BackgroundChange:
    def __init__(self, directory_input_path, directory_output_path):
        self.directory_input_path = directory_input_path
        self.directory_output_path = directory_output_path
        
    def stage_display(self):

        # 画像を読み込む
        image = cv2.imread("./stage_image/senjou.png") 
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 画像を表示
        plt.figure(figsize=(8.54, 4.8), dpi=100)
        plt.imshow(image)
        plt.axis('off')
        plt.show()
    
    def stage_resize(self):
        stageimage = Image.open("./stage_image/senjou.png")
        stageimage = stageimage.resize((854, 480))
        stageimage.save("./stage_image/senjou_resize.png")
    
    def background_change(self):
        # ステージ画像とキャラクター画像を読み込む
        stage_image = Image.open("./stage_image/senjou_resize.png")
        character_image = Image.open("./segment-anything-2/output/b_0/01000.jpg")
        
        # NumPy配列に変換し、RGBモードに統一
        stage_array = np.array(stage_image.convert('RGB'))
        character_array = np.array(character_image.convert('RGB'))
        
        # キャラクター画像の黒い部分(背景)をステージ画像で置き換える
        mask = (character_array == 0).all(axis=2)
        result_array = np.where(mask[:, :, np.newaxis], stage_array, character_array)
        
        # PILイメージに戻す
        result_image = Image.fromarray(result_array.astype(np.uint8))
        result_image.save("./output/result.jpg")

# コードの説明を書く予定