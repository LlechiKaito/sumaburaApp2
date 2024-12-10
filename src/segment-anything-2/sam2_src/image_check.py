import cv2
from glob import glob
from natsort import natsorted

import matplotlib
matplotlib.use('TkAgg')  # または 'Qt5Agg' など

import matplotlib.pyplot as plt

# 画像のパス設定
input_img_dir = "../../input/images/jabDa_0/resize"

# 動画の最初のフレームを取得
frame_names = natsorted(glob(f"{input_img_dir}/*.jpeg"))
image = cv2.imread(frame_names[0])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 描画
plt.figure(figsize=(8.54, 4.8), dpi=100)
plt.imshow(image)
plt.axis('on')
plt.show()