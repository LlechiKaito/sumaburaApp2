import cv2
import os
from glob import glob
import pandas as pd
import numpy as np
import datetime
from PIL import Image
import shutil

class MakeData:
    def __init__(self, is_shuffle, video_path, directory_path):
        # キャプチャーする動画のパス
        self.VIDEO_PATH          = video_path

        # 画像を保存する大元のパス（ここの下にMAKE_DIRECTORY_NAMEを作ってその下にbeforeProcessingというディレクトリを作る）
        self.DIRECTORY_PATH      = directory_path

        # 加工前の画像を保存するディレクトリーのディレクトリーの名前(self.VIDEO_PATHの一番下のファイル名を.に対して分割した最初の文字列を取得)
        self.MAKE_DIRECTORY_NAME = os.path.basename(self.VIDEO_PATH).rsplit('.', 1)[0]

        # 加工後の画像の拡張子の指定
        self.EXT = "png"
        
        # シャッフルする画像のあるパス（空の場合．afterProcessingがシャッフル対象）
        self.TARGET_SHUFFLE_PATH = ""
        
        # ログを保存しておくディレクトリーのパス
        self.LOGS_PATH = "logs"
        
        # リサイズするときの縦の長さ
        self.IMAGE_HEIGHT_SIZE = 480
        
        # リサイズするときの横の長さ
        self.IMAGE_WIDTH_SIZE = 854
        
        # リサイズするとき背景の横の長さ
        self.IMAGE_BACKGROUND_WIDTH_SIZE = 854
        
        # リサイズするときの背景の縦の長さ
        self.IMAGE_BACKGROUND_HEIGHT_SIZE = 480

        self.save_all_freames()
        self.resize_images()
        
        # シャッフルするかどうかの判定
        if (is_shuffle):
            self.shuffle()

    # 動画データを各フレーム画像にする関数
    def save_all_freames(self):
        # 動画をキャプチャーして，インスタンス化
        cap = cv2.VideoCapture(self.VIDEO_PATH)

        # ビデオがない場合，実行終了
        if not cap.isOpened():
            return
        
        # MAKE_DIRECTORY_NAMEとbeforeProcessingを結合してパス形式にする（MAKE_DIRECTORY_NAME/resize）
        mkdir = os.path.join(self.MAKE_DIRECTORY_NAME, "origin")

        # DIRECTORY_PATHとmkdirを結合してパス形式にする（DIRECTORY_PATH/mkdir）
        self.target_folder_path = os.path.join(self.DIRECTORY_PATH, mkdir)
        # shuffleとresizeで使うコピーしたデータを置くフォルダーのパス(DIRECTORY_PATH/MAKE_DIRECTORY_NAME/resize)
        self.set_folder_after_copy_path = os.path.join(os.path.join(self.DIRECTORY_PATH, self.MAKE_DIRECTORY_NAME, "resize"))
         # anotation後のデータを置くフォルダーのパス(DIRECTORY_PATH/MAKE_DIRECTORY_NAME/annotations)
        self.set_folder_after_anotation_path = os.path.join(os.path.join(self.DIRECTORY_PATH, self.MAKE_DIRECTORY_NAME, "annotations"))
        
        # cap.get(cv2.CAP_PROP_FNAME_COUNT):フレーム数
        # フレーム数の桁数を格納する．
        self.total_files = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.dight = len(str(self.total_files))

        # target_folder_pathが存在しない場合，作成する．存在する場合，関数自体を終了
        if not os.path.isdir(self.target_folder_path):
            # DIRECTORY_PATHの下にディレクトリを作る（途中含み存在しない場合は，そこを作る（exist_ok=True）存在する場合は，作らない）
            os.makedirs(self.target_folder_path, exist_ok=True)
            os.makedirs(self.set_folder_after_copy_path)
            os.makedirs(self.set_folder_after_anotation_path)
            
        else:
            print("加工前の画像はすでに作成しています．")
            print()
            return
        
        count = 0
        while True:
            # retは，読み込みが成功したかどうか(Bool)
            # frameは．画像データ
            ret, frame = cap.read()

            # str(count).zfill(dight)は．桁数をdightにする(0002みたいな)
            # ファイルを保存するパス．(MAKE_DIRECTORY_NAME_0002.pngみたいなファイル名で保存する．)
            store_file_path = os.path.join(self.target_folder_path, self.MAKE_DIRECTORY_NAME + "_" + str(count).zfill(self.dight) + "." + self.EXT)

            if ret:
                # store_file_nameにframeを保存する
                cv2.imwrite(store_file_path, frame)
                print(str(count) + " : freamize OK")
                
            else:
                # キャプチャーしたものを開放する
                cap.release()

                # すべてのOpenCVウィンドウを閉じる
                cv2.destroyAllWindows()

                print()
                return
            count += 1
            
    def resize_images(self):
        
        image_paths_after_processing_total = np.array(glob(os.path.join(self.set_folder_after_copy_path, f"*.{self.EXT}"))).size
        
        if (image_paths_after_processing_total == self.total_files):
            print("正常にリサイズされています．")
            print()
            return
        
        image_paths = np.array(glob(os.path.join(self.target_folder_path, f"*.{self.EXT}")))
        
        if (image_paths.size == 0):
            print("リサイズする対象がありません．")
            print()
            return

        for i, image_path in enumerate(image_paths):
            # 画像を開いてRGB形式に変換する
            image = Image.open(image_path)
            rgb_image = image.convert('RGB')
            # リサイズするコマンド
            rgb_image.thumbnail((self.IMAGE_WIDTH_SIZE, self.IMAGE_HEIGHT_SIZE))
            
            # 白い背景を作成して上記のリサイズした画像を張り付ける
            back_ground = Image.new("RGB", (self.IMAGE_BACKGROUND_WIDTH_SIZE, self.IMAGE_BACKGROUND_HEIGHT_SIZE), color=(255, 255, 255))
            back_ground.paste(rgb_image)
            
            # image_pathの一番下にあるすなわちファイル名を格納（元画像のファイル名）
            old_name = os.path.basename(image_path)
            # 保存先の画像のファイルのパス
            after_resize_path = os.path.join(self.set_folder_after_copy_path, old_name)
            # backgroundをafter_resize_pathに保存する
            back_ground.save(after_resize_path)

            print(str(i) + " : resize ok")
        print()
        return
    
    def shuffle(self):
        
        if not (self.TARGET_SHUFFLE_PATH):
            self.TARGET_SHUFFLE_PATH = self.set_folder_after_copy_path
        
        # シャッフルする画像ファイルのパスをすべて取得する
        image_paths = np.array(glob(os.path.join(self.TARGET_SHUFFLE_PATH, f"*.{self.EXT}")))
                                        
        if (image_paths.size == 0):
            print("シャッフルする対象がありません．")
            return
        
        # 0~画像ファイル数までの値をランダムにarrayに格納(重複なし)
        random_int_array = np.random.permutation(np.arange(self.total_files))
        
        # csvを作るためのファイル名を格納するためのもの
        old_file_names = np.array([])
        new_file_names = np.array([])

        for i, image_path in enumerate(image_paths):
            # image_pathの一番下にあるすなわちファイル名を格納（元画像のファイル名）
            old_name = os.path.basename(image_path)
            # コピー後の画像のファイル名(MAKE_DIRECTORY_NAME_0002.pngみたいなファイルで保存する)
            new_name = self.MAKE_DIRECTORY_NAME + "_" + str(random_int_array[i]).zfill(self.dight) + "." + self.EXT
            # コピー後の画像のファイルのパス
            after_shuffle_path = os.path.join(self.TARGET_SHUFFLE_PATH, new_name)
            
            # コピーするときに同じパスだとエラーが起こるためパスが違う場合に実行している
            if (after_shuffle_path != image_path):
                # image_pathをafter_shuffle_pathにコピーする
                shutil.copyfile(image_path, after_shuffle_path)
            
            # csvのために格納する
            old_file_names = np.append(old_file_names, old_name)
            new_file_names = np.append(new_file_names, new_name)
            print(str(i) + " : shuffle ok")
        
        # csvの内容を格納
        logs = pd.DataFrame({"old name": old_file_names, "new name": new_file_names})
        # csvの名前(shuffle_日付.csv)
        log_file_name = "shuffle" + "_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".csv"
        # ログを保存するディレクトリーとログファイルを結合してパスににする(ここにcsvを保存する)
        log_path = os.path.join(self.LOGS_PATH, log_file_name)
        # csvにindexなしで保存(いる？)
        logs.to_csv(log_path, index=False)
        print()
        return