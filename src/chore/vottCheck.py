import xml.etree.ElementTree as ET
from beforeProcessing.makeData import MakeData
import numpy as np
from glob import glob
import os

class vottCheck(MakeData):
    def __init__(self):
        super().__init__(False)
        # self.set_folder_after_anotation_path <- これに関しては継承して保持している
        
        # タグ一覧をarrayに格納
        self.TAGS_counts = np.array([
            ["B_air", 0],
            ["DA", 0],
            ["D_air", 0],
            ["Down_B", 0],
            ["D_smash", 0],
            ["D_tilt", 0],
            ["F_air", 0],
            ["F_smash", 0],
            ["F_tilt", 0],
            ["Jab1", 0],
            ["Jab2", 0],
            ["Jab3", 0],
            ["Jump", 0],
            ["N_air", 0],
            ["NB", 0],
            ["Side_B", 0],
            ["Stand", 0],
            ["Up_B", 0],
            ["U_smash", 0],
            ["U_tilt", 0],
            ["notwaza", 0],
            ["U_throw", 0],
            ["Grab", 0],
            ["Grab_blow", 0],
            ["F_throw", 0],
            ["D_throw", 0],
            ["B_throw", 0],
            ["U_air", 0]
        ])
        
        # 対象となる拡張子（一回しか使用しないため*.も加えた形にした)
        self.EXT = "*.xml"
        
        # self.EXTファイルが格納されているフォルダー
        self.TARGET_FOLDER_NAME_FOR_EXT = "Annotations"
        
    def anotation_check(self):
        
        # 対象ファイルを格納するフォルダーのパス（これがない場合は，vottの設定が終わっていない）
        check_folder_path = os.path.join(self.set_folder_after_anotation_path, self.TARGET_FOLDER_NAME_FOR_EXT)
        
        if not (os.path.isdir(check_folder_path)):
            print("アノテーションするための前処理ができていません．")
            return
        
        # 対象ファイルのパスの格納
        file_paths = np.array(glob(os.path.join(check_folder_path, self.EXT)))
        
        # file_pathsが空の場合（アノテーションしていない場合），関数終了
        if (file_paths.size == 0):
            print("アノテーションチェックするためのファイルが存在しません．")
            return
        
        # nameタグによって区別できるため（ファイルの中身を見ればわかる）
        search_element = "name"
        
        for file_path in file_paths:
            # xmlファイルの中身の内容を使いたいときに使用する
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            # カウントのための変数ほとんどの場合，2以上にならない，2以上の場合例外処理する
            count = 0
            # objectタグについてループする
            for element in root.iter(search_element):
                count += 1
                
                # タグとnameタグの内容が一致するかのチェック
                for i, tag_count in (self.TAGS_counts):
                    if (element == tag_count[0]):
                        self.TAGS_counts[i][1] += 1
                        
            # 例外処理
            if (count >= 2):
                print(file_path + " : " + count + "個アノテーションしています．")
        
        return