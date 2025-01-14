from glob import glob
import math
import os
import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET

import yaml

class MakeTextForTrain:
    def __init__(self, text_dir, image_dir, annotation_dir, dataset_dir, val_rate=0.16, test_rate=0.2, max_total_data=1000, ext="png"):
        # テキストファイルを格納するディレクトリの相対パス
        self.TEXT_DIR = text_dir
        # 学習に使うpngファイルの入ったディレクトリのパス
        self.IMAGE_DIR = image_dir
        # pngデータのアノテーション情報の入った.xmlファイルの入ったディレクトリの相対パス
        self.ANNOTATION_DIR = annotation_dir
        self.DATASET_DIR = dataset_dir
        # 学習データの割合
        self.TRAIN_RATE = 1 - val_rate - test_rate
        # 検証データの割合
        self.VAL_RATE = val_rate
        # テストーデータの割合
        self.TEST_RATE = test_rate
        # 写真データの拡張子（デフォルト.png）
        self.EXT = ext
        # 格納するテキストの名前
        self.TEXT_NAMES = np.array(['train', 'val', 'test'])
        
        # 技の種類をnumpyのarrayで格納
        self.CLASSES = np.array(["Jab1","Jab2","Jab3","notwaza","B-air","D-air","D-smash",
            "D-tilt","DA","Down-B","F-air","F-smash","F-tilt","N-air","NB","Side-B","U-air",
            "U-smash","U-tilt","Up-B","B-throw","D-throw","F-throw","U-throw","Grab-blow","Grab"
        ])
        
        train_total_data = int( max_total_data / ( len(self.CLASSES) + 9 ) * self.TRAIN_RATE )
        val_total_data = int( max_total_data / ( len(self.CLASSES) + 9 ) * self.VAL_RATE )
        test_total_data = int( max_total_data / ( len(self.CLASSES) + 9 ) * self.TEST_RATE )
        
        # 技の種類を辞書型で格納
        self.TOTAL_CLASSES = {
            "Jab1":      np.array([train_total_data, val_total_data, test_total_data]),
            "Jab2":      np.array([train_total_data, val_total_data, test_total_data]),
            "Jab3":      np.array([train_total_data, val_total_data, test_total_data]),
            "notwaza":   np.array([train_total_data * 10, val_total_data * 10, test_total_data * 10]),
            "B-air":     np.array([train_total_data, val_total_data, test_total_data]),
            "D-air":     np.array([train_total_data, val_total_data, test_total_data]),
            "D-smash":   np.array([train_total_data, val_total_data, test_total_data]),
            "D-tilt":    np.array([train_total_data, val_total_data, test_total_data]),
            "DA":        np.array([train_total_data, val_total_data, test_total_data]),
            "Down-B":    np.array([train_total_data, val_total_data, test_total_data]),
            "F-air":     np.array([train_total_data, val_total_data, test_total_data]),
            "F-smash":   np.array([train_total_data, val_total_data, test_total_data]),
            "F-tilt":    np.array([train_total_data, val_total_data, test_total_data]),
            "N-air":     np.array([train_total_data, val_total_data, test_total_data]),
            "NB":        np.array([train_total_data, val_total_data, test_total_data]),
            "Side-B":    np.array([train_total_data, val_total_data, test_total_data]),
            "U-air":     np.array([train_total_data, val_total_data, test_total_data]),
            "U-smash":   np.array([train_total_data, val_total_data, test_total_data]),
            "U-tilt":    np.array([train_total_data, val_total_data, test_total_data]),
            "Up-B":      np.array([train_total_data, val_total_data, test_total_data]),
            "B-throw":   np.array([train_total_data, val_total_data, test_total_data]),
            "D-throw":   np.array([train_total_data, val_total_data, test_total_data]),
            "F-throw":   np.array([train_total_data, val_total_data, test_total_data]),
            "U-throw":   np.array([train_total_data, val_total_data, test_total_data]),
            "Grab-blow": np.array([train_total_data, val_total_data, test_total_data]),
            "Grab":      np.array([train_total_data, val_total_data, test_total_data])
        }
        
        self.name_count = {
            "Jab1":      np.array([0, 0, 0]),
            "Jab2":      np.array([0, 0, 0]),
            "Jab3":      np.array([0, 0, 0]),
            "notwaza":   np.array([0, 0, 0]),
            "B-air":     np.array([0, 0, 0]),
            "D-air":     np.array([0, 0, 0]),
            "D-smash":   np.array([0, 0, 0]),
            "D-tilt":    np.array([0, 0, 0]),
            "DA":        np.array([0, 0, 0]),
            "Down-B":    np.array([0, 0, 0]),
            "F-air":     np.array([0, 0, 0]),
            "F-smash":   np.array([0, 0, 0]),
            "F-tilt":    np.array([0, 0, 0]),
            "N-air":     np.array([0, 0, 0]),
            "NB":        np.array([0, 0, 0]),
            "Side-B":    np.array([0, 0, 0]),
            "U-air":     np.array([0, 0, 0]),
            "U-smash":   np.array([0, 0, 0]),
            "U-tilt":    np.array([0, 0, 0]),
            "Up-B":      np.array([0, 0, 0]),
            "B-throw":   np.array([0, 0, 0]),
            "D-throw":   np.array([0, 0, 0]),
            "F-throw":   np.array([0, 0, 0]),
            "U-throw":   np.array([0, 0, 0]),
            "Grab-blow": np.array([0, 0, 0]),
            "Grab":      np.array([0, 0, 0])
        }
        
        self.index = 0
        self.texts = ['', '', '']
        
        self.make_text()
        self.voc_annotation()
        # self.write_custom_classes()
        
        # TOTAL_CLASSESの結果を出力
        print("TOTAL_CLASSES:")
        for class_name, values in self.TOTAL_CLASSES.items():
            print(f"{class_name}: {values}")
    
    # pytorchを使うために必要な処理の一つ
    # pytorch_yolov3/config/custom_classes.txtに技名一覧を書き込むためのプログラム
    def write_custom_classes(self):
         # クラス名をファイルに書き込む
        with open('../pytorch_yolov3/config/custom_classes.txt', 'w', encoding='utf-8') as file:
            for cls in self.CLASSES:
                file.write(cls + '\n')
        
    def make_text(self):
        # 格納するテキストの宣言
        text = ''
        
        # 画像ファイルのパスをすべて取得する
        image_paths = np.array(glob(os.path.join(self.IMAGE_DIR, f"*.{self.EXT}")))
        
        # 画像ファイルがない場合，実行されない
        if image_paths.size == 0:
            print('image not found in ', self.IMAGE_DIR)
            return
    
        for i, image_path in enumerate(image_paths):
            if i == 0:
                text = os.path.basename(image_path) + '\n'
            else:
                text += os.path.basename(image_path) + '\n' 

        new_file = open(os.path.join(self.TEXT_DIR, 'data.txt'), 'w')
        new_file.write(text)
        new_file.close()
    
    def convert_annotation(self, image_file_path, image_id):
        # xmlファイルを読み込む
        tree = ET.parse(os.path.join(self.ANNOTATION_DIR, f'{image_id.replace(".png", "")}.xml'))
        # 一番上の行の要素を取り出します．
        root = tree.getroot()

        # オブジェクトタグの中のobject要素について処理する（実際は一つしかないため一回しか実行されない）
        for obj in root.iter('object'):
            # difficultタグに囲まれている値を格納
            difficult = obj.find('difficult').text
            # nameタグに囲まれている値を格納
            cls = obj.find('name').text
            
            # 技名が存在しない場合とdifficultの値が1の時ループを飛ばす
            if cls not in self.CLASSES or int(difficult) == 1:
                return True
            if cls in self.TOTAL_CLASSES:
                self.name_count[cls][self.index] += 1
            else:
                self.name_count[cls][self.index] = 1
            if self.name_count[cls][self.index] > self.TOTAL_CLASSES[cls][self.index]:
                self.index += 1
                if cls in self.TOTAL_CLASSES:
                    self.name_count[cls][self.index] += 1
                else:
                    self.name_count[cls][self.index] = 1
                if self.name_count[cls][self.index] > self.TOTAL_CLASSES[cls][self.index]:
                    self.index += 1
                    if cls in self.TOTAL_CLASSES:
                        self.name_count[cls][self.index] += 1
                    else:
                        self.name_count[cls][self.index] = 1
                    if self.name_count[cls][self.index] > self.TOTAL_CLASSES[cls][self.index]:
                       return True
        
            # 最初のnp.where(self.CLASSES == cls)[0]で一致した要素をすべて得れるそこから[0]することで一番最初の要素つまり一つの値だけ持ってこれる
            cls_id = np.where(self.CLASSES == cls)[0][0]  # クラスIDを取得
            
            # bndboxタグに囲まれている値を格納
            xmlbox = obj.find('bndbox')
            # xmin, ymin, xmax, ymaxをfloat型にしてそれを小数点切り捨てをして整数型にしてタプル形式にして格納
            b = (int(float(xmlbox.find('xmin').text)),
                 int(float(xmlbox.find('ymin').text)),
                 int(float(xmlbox.find('xmax').text)),
                 int(float(xmlbox.find('ymax').text)))
            with open(os.path.join(os.path.join(self.DATASET_DIR, 'labels'), f'{image_id}.txt'), 'w') as list_file:
                # list_file.write(str(cls_id) + ',' + ",".join([str(a) for a in b]))
                list_file.write(cls + ' ' + " ".join([str(a) for a in b]))
            if self.texts[self.index] == '':
                self.texts[self.index] = image_id + '.' + self.EXT + '\n'
            else:
                self.texts[self.index] += image_id + '.' + self.EXT + '\n'
        return False

    def voc_annotation(self):
        # csvとして読み込み一列目をすべて格納する
        image_ids = pd.read_csv(os.path.join(self.TEXT_DIR, 'data.txt'), header=None).iloc[:, 0].str.replace('.png', '').values  # 画像IDリストを取得し、.pngを削除
        os.makedirs(os.path.join(os.path.join(self.DATASET_DIR, 'labels')), exist_ok=True)
        os.makedirs(os.path.join(os.path.join(self.DATASET_DIR, 'images')), exist_ok=True)
        # 画像名を一つずつ取り出しながら処理
        for image_id in image_ids:
            self.index = 0
            # 画像の相対パスを格納
            image_file_path = os.path.join(self.IMAGE_DIR, image_id)
            is_continue = self.convert_annotation(image_file_path, image_id)
            if is_continue:
                continue
        for i, text in enumerate(self.texts):
            # テキスト名_annotations.txtを開くなかったら作成
            with open(os.path.join(self.DATASET_DIR, f'{self.TEXT_NAMES[i]}.txt'), 'w') as list_file:
                # 相対パス, xmin, ymin, xmax, ymax, 技のラベルインデックスを書き込む
                list_file.write(text)