from txtShuffle import txtShuffle
from moveFile import moveFile
from makeTextForTrain import MakeTextForTrain
from beforeProcessing.makeData import MakeData
from vottCheck import vottCheck

# ここはコメントアウトしながら使って

# video_path = './../../input/videoes/air_0.mp4'
# directory_path = './../../input/images'
# is_shuffle = False

# # 第一引数がシャッフルするかどうか
# MakeData(is_shuffle, video_path, directory_path)

# 現状検証データを作るとき以外では使わない
text_dir = './../../input/texts'
image_dir = './../../input/images/air_0/annotations/air_0-PascalVOC-export/JPEGImages'
annotation_dir = './../../input/images/air_0/annotations/air_0-PascalVOC-export/Annotations'
# 以下は変更する可能性が高い
dataset_dir = './../pytorch_yolov3/custom_dataset'

MakeTextForTrain(text_dir, image_dir, annotation_dir, dataset_dir, val_rate=0, test_rate=1, max_total_data=14000)

# テキストをシャッフルする
# txt_paths = [
#                 './../pytorch_yolov3/custom_dataset/train.txt',
#                 './../pytorch_yolov3/custom_dataset/val.txt',
#                 './../pytorch_yolov3/custom_dataset/test.txt',
#                 './../pytorch_yolov3/custom_dataset/testTemp.txt',
#             ]
# txtShuffle(txt_paths)

# 先輩のデータを持ってくるときに使用しただけなので，使わない
# # ファイルを送信したいディレクトリの相対パス
# to_path = './../pytorch_yolov3/custom_dataset/images'

# # 送信したいファイルの入ったディレクトリの相対パス（複数指定可）
# from_paths = [
#                 './../../../Suzuki/データ/VoTT/export/つかみ以外技export/JPEGImages',
#                 './../../../Suzuki/データ/VoTT/export/弱識別-PascalVOC-export0114/JPEGImages',
#                 './../../../Suzuki/データ/VoTT/export/弱識別-PascalVOC-export1005/JPEGImages',
#                 './../../../Suzuki/データ/VoTT/export/弱識別-PascalVOC-export1024/JPEGImages',
#                 './../../../Suzuki/データ/VoTT/export/弱識別-PascalVOC-export1122/JPEGImages',
#                 './../../../Suzuki/データ/VoTT/export/弱識別-PascalVOC-export1209/JPEGImages'
#             ]

# moveFile(to_path, from_paths)

# # MakeDataと同じ引数でOK（こいつは二つ以上のアノテーションがないかの確認するものだから）(デバックしないと動かない使わん予定)
# vottCheck = vottCheck(is_shuffle, video_path, directory_path)
# vottCheck.anotation_check()
