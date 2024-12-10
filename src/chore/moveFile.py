import os
import numpy as np
import shutil

# このファイルが実行できない場合，numpy arrayで扱っているところをリストにすれば動く
class moveFile:
    def __init__(self, to_path, from_paths):
        self.TO_DIRECTORY_PATH = to_path
        self.FROM_DIRECTORY_PATHS = np.array(from_paths)  # from_paths をnumpyのarrayで扱う
        self.move()

    def move(self):
        # それぞれの from_path について処理を行う
        for from_path in self.FROM_DIRECTORY_PATHS:
            # ファイルをリスト化したものをnumpyのarrayにする
            files = np.array(os.listdir(from_path))

            for file_name in files:
                # 移動するファイルのパスの作成（ディレクトリパスにファイル名をくっつけるだけ）
                from_file_path = os.path.join(from_path, file_name)
                # 移動先のファイルのパスの作成
                to_file_path = os.path.join(self.TO_DIRECTORY_PATH, file_name)

                # ファイルだった場合処理
                if os.path.isfile(from_file_path):
                    # コピーする
                    shutil.copy(from_file_path, to_file_path)
                    # コピーしたことを標準出力
                    print(f"{file_name} を {self.TO_DIRECTORY_PATH} にコピーしました from {from_path}")
