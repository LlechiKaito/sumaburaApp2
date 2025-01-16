import cv2
import numpy as np
import os

class Combination:
    def __init__(self, input_dir1, input_dir2, output_dir):
        self.input_dir1= input_dir1
        self.input_dir2 = input_dir2 
        self.output_dir = output_dir

    def combine_images(self):
        # 出力ディレクトリがない場合は作成
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        # 入力ディレクトリ1の画像を取得
        files1 = sorted(os.listdir(self.input_dir1))

        # 入力ディレクトリ2の画像を取得  
        files2 = sorted(os.listdir(self.input_dir2))

        # 両方のディレクトリの画像を処理
        for f1, f2 in zip(files1, files2):
            # 画像を読み込み
            img1 = cv2.imread(os.path.join(self.input_dir1, f1))
            img2 = cv2.imread(os.path.join(self.input_dir2, f2))

            # 画像のサイズが同じことを確認
            if img1.shape != img2.shape:
                raise ValueError("画像のサイズが異なります")

            # 結果を格納する配列を作成
            result = np.zeros_like(img1)

            print(img1.shape)
            print(img2.shape)

            # ピクセルごとに処理(欠点：2次元目が0の場合黒と判断するので，色変更して2次元目を０にするときは注意してほしい)
            for i in range(img1.shape[0]):
                for j in range(img1.shape[1]):
                    if img1[i,j, 0] == img2[i,j, 0]:
                        # 同じ値の場合はそのまま
                        result[i,j] = img1[i,j]
                    else:
                        # 黒(0,0,0)でない方を採用
                        if img1[i,j, 0] == 0:
                            result[i,j] = img2[i,j]
                        else:
                            result[i,j] = img1[i,j]

            # 結果を保存
            cv2.imwrite(os.path.join(self.output_dir, f1), result)