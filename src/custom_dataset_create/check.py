import cv2
import os

img_dir = "../pytorch_yolov3/custom_dataset/images"

image_list = os.listdir(img_dir)

for image_name in image_list:
    # 画像を読み込む。
    img = cv2.imread(os.path.join(img_dir, image_name))

    # cv2.cvtColorの結果がNoneかどうかを確認
    try:
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    except:
        print(image_name)