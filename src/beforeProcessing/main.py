from makeData import MakeData

video_path = './../../input/videoes/jabDa_0.mp4'
directory_path = './../../input/images'
is_shuffle = False

# 第一引数がシャッフルするかどうか
MakeData(is_shuffle, video_path, directory_path)