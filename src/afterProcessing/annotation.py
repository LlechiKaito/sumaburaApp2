import cv2
import numpy as np
import os
import matplotlib
matplotlib.use('TkAgg')  # または 'Qt5Agg' など

import matplotlib.pyplot as plt

class Annotation:
    def __init__(self, directory_input_path, directory_output_path, waza_list):
        self.directory_input_path = directory_input_path
        self.directory_output_path = directory_output_path
        os.makedirs(self.directory_output_path, exist_ok=True)

        self.image_names = os.listdir(self.directory_input_path)
        self.waza_list = waza_list

        self.txt_contents = np.array([])

    def get_annotation_area(self, image_name, frame_idx):
        temp_image = cv2.imread(os.path.join(self.directory_input_path, image_name))
        image = cv2.cvtColor(temp_image, cv2.COLOR_BGR2RGB)

        plt.imshow(image)
        plt.show()

        numpy_image = image[:,:,0]
        print(numpy_image)
        bool_mask = (numpy_image != 255) & (numpy_image != 0)
        print(bool_mask)
        # bool_maskのTrueの位置を取得
        true_positions = np.where(bool_mask)

        # 0次元目(y座標)の最小値と最大値を取得
        min_y = np.min(true_positions[0])
        max_y = np.max(true_positions[0])

        # 1次元目(x座標)の最小値と最大値を取得
        min_x = np.min(true_positions[1]) 
        max_x = np.max(true_positions[1])

        print(f"y座標の最小値: {min_y}")
        print(f"y座標の最大値: {max_y}")
        print(f"x座標の最小値: {min_x}")
        print(f"x座標の最大値: {max_x}")

        print('技名', min_x, min_y, max_x, max_y)
        # self.txt_contents[frame_idx] = f"{self.txt_contents[frame_idx]} {min_x} {min_y} {max_x} {max_y}"

    def get_annotation_waza(self, waza_name):
        self.txt_contents = np.append(self.txt_contents, waza_name)
        print(self.txt_contents)
    
    def save_txt(self, image_name, txt_content):
        with open(os.path.join(self.directory_output_path, f"{image_name}.txt"), "w") as file:
            file.write(txt_content)
            file.write("\n")
    
    def annotation_main(self):
        if self.waza_list[-1][1] != len(self.image_names):
            print("技名のフレーム数と画像のフレーム数が一致しません")
            return

        waza_idx = 0
        for i, image_name in enumerate(self.image_names):
            if i <= self.waza_list[waza_idx][1]:
                self.get_annotation_waza(self.waza_list[waza_idx][0])
            else:
                waza_idx += 1
                self.get_annotation_waza(self.waza_list[waza_idx][0])
            self.get_annotation_area(image_name, i)
            self.save_txt(image_name, self.txt_contents[i])
        
# コードの説明を書く予定