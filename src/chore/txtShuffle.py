import random

class txtShuffle:
    def __init__(self, txt_paths):
        self.TXT_PATHS = txt_paths
        for txt_path in self.TXT_PATHS:
            # ファイルを読み込む
            with open(txt_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # 行をランダムにシャッフルする
            random.shuffle(lines)

            # シャッフルした内容をファイルに書き戻す
            with open(txt_path, 'w', encoding='utf-8') as file:
                file.writelines(lines)