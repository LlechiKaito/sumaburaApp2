from makeData import MakeData
import os

video_dir = './../../input/videoes'
video_files = [os.path.join(video_dir, f) for f in os.listdir(video_dir) if os.path.isfile(os.path.join(video_dir, f))]

for video_path in video_files:
    directory_path = './../../input/images'
    is_shuffle = False

    # 第一引数がシャッフルするかどうか
    MakeData(is_shuffle, video_path, directory_path)