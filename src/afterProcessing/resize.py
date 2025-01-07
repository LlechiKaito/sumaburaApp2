import cv2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from PIL import Image
import os

class Resize:
    def __init__(self, directory_input_path, directory_output_path):
        self.directory_input_path = directory_input_path
        self.directory_output_path = directory_output_path

        os.makedirs(self.directory_output_path, exist_ok=True)
        os.makedirs(self.directory_input_path, exist_ok=True)

        self.image_list = os.listdir(self.directory_input_path)
    
    def resize(self):
        for image_name in self.image_list:
            # 画像を読み込む
            image = Image.open(os.path.join(self.directory_input_path, image_name))
            # リサイズ
            image = image.resize((608, 342))
            # 保存
            image.save(os.path.join(self.directory_output_path, image_name))
