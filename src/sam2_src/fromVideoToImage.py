import subprocess
import os

# 入力動画ファイルのパス
input_video_path = '../../input/videoes/air_0.mp4'

# 出力画像ディレクトリ
output_img_dir = '../../input/images/air_0'
os.makedirs(output_img_dir, exist_ok=True)

# ffmpegコマンドを構築
ffmpeg_command = [
    'ffmpeg',
    '-i', input_video_path,          # 入力ファイル
    '-q:v', '2',                     # 画像品質
    '-vf', 'scale=854:480',          # 解像度を854x480に設定（320x180, 480x270, 640x360, 854x480, 1280x720）
    '-start_number', '0',            # 出力ファイルの開始番号
    os.path.join(output_img_dir, '%05d.jpg')  # 出力ファイルのパス
]

# ffmpegコマンドを実行
subprocess.run(ffmpeg_command, check=True)

print("動画から画像への変換が完了しました。")