import os
import shutil
from PIL import Image

# 入力ディレクトリのパス
input_text_dir = ["../../output/texts/B-air_0", 
                  "../../output/texts/B-throw_0", 
                  "../../output/texts/D-air_0", 
                #   "../../output/texts/D-smash_0", 
                  "../../output/texts/D-throw_0", 
                  "../../output/texts/D-tilt_0",
                  "../../output/texts/DA_0", "../../output/texts/Down-B_0",
                  "../../output/texts/F-air_0", "../../output/texts/F-smash_0",
                  "../../output/texts/F-throw_0", 
                  "../../output/texts/F-tilt_0",
                  "../../output/texts/Grab-blow_0", 
                  "../../output/texts/Jab_0",
                  "../../output/texts/N-air_0", "../../output/texts/NB_0",
                  "../../output/texts/Side-B_0", "../../output/texts/U-air_0",
                  "../../output/texts/U-smash_0", 
                  "../../output/texts/U-throw_0",
                  "../../output/texts/U-tilt_0", "../../output/texts/Up-B_0"
                ]
# input_image_dir = ["../../input/images/B-air_0/resize2", "../../input/images/B-throw_0/resize2", 
#                    "../../input/images/D-air_0/resize2", 
#                 #    "../../input/images/D-smash_0/resize2", 
#                    "../../input/images/D-throw_0/resize2", "../../input/images/D-tilt_0/resize2",
#                    "../../input/images/DA_0/resize2", "../../input/images/Down-B_0/resize2",
#                    "../../input/images/F-air_0/resize2", "../../input/images/F-smash_0/resize2",
#                    "../../input/images/F-throw_0/resize2", "../../input/images/F-tilt_0/resize2",
#                    "../../input/images/Grab-blow_0/resize2", "../../input/images/Jab_0/resize2",
#                    "../../input/images/N-air_0/resize2", "../../input/images/NB_0/resize2",
#                    "../../input/images/Side-B_0/resize2", "../../input/images/U-air_0/resize2",
#                    "../../input/images/U-smash_0/resize2", "../../input/images/U-throw_0/resize2",
#                    "../../input/images/U-tilt_0/resize2", "../../input/images/Up-B_0/resize2"
#                 ]
# senjouステージの奴
# input_image_dir = ["../../output/images/B-air_0/senjou", "../../output/images/B-throw_0/senjou", 
#                    "../../output/images/D-air_0/senjou", 
#                 #    "../../output/images/D-smash_0/senjou", 
#                    "../../output/images/D-throw_0/senjou", "../../output/images/D-tilt_0/senjou",
#                    "../../output/images/DA_0/senjou", "../../output/images/Down-B_0/senjou",
#                    "../../output/images/F-air_0/senjou", "../../output/images/F-smash_0/senjou",
#                    "../../output/images/F-throw_0/senjou", "../../output/images/F-tilt_0/senjou",
#                    "../../output/images/Grab-blow_0/senjou", "../../output/images/Jab_0/senjou",
#                    "../../output/images/N-air_0/senjou", "../../output/images/NB_0/senjou",
#                    "../../output/images/Side-B_0/senjou", "../../output/images/U-air_0/senjou",
#                    "../../output/images/U-smash_0/senjou", "../../output/images/U-throw_0/senjou",
#                    "../../output/images/U-tilt_0/senjou", "../../output/images/Up-B_0/senjou"
#                 ]

input_image_dir = ["../../output/images/B-air_0/senjou2", 
                   "../../output/images/B-throw_0/senjou2", 
                   "../../output/images/D-air_0/senjou2", 
                #    "../../output/images/D-smash_0/senjou2", 
                   "../../output/images/D-throw_0/senjou2", 
                   "../../output/images/D-tilt_0/senjou2",
                   "../../output/images/DA_0/senjou2", "../../output/images/Down-B_0/senjou2",
                   "../../output/images/F-air_0/senjou2", "../../output/images/F-smash_0/senjou2",
                   "../../output/images/F-throw_0/senjou2", 
                   "../../output/images/F-tilt_0/senjou2",
                   "../../output/images/Grab-blow_0/senjou2", 
                   "../../output/images/Jab_0/senjou2",
                   "../../output/images/N-air_0/senjou2", "../../output/images/NB_0/senjou2",
                   "../../output/images/Side-B_0/senjou2", "../../output/images/U-air_0/senjou2",
                   "../../output/images/U-smash_0/senjou2", 
                   "../../output/images/U-throw_0/senjou2",
                   "../../output/images/U-tilt_0/senjou2", "../../output/images/Up-B_0/senjou2"
                ]

# 出力ディレクトリのパス
output_dir = "../pytorch_yolov3/custom_dataset"
output_image_dir = os.path.join(output_dir, "images")
output_label_dir = os.path.join(output_dir, "labels")

# 出力ディレクトリが存在しない場合は作成
os.makedirs(output_dir, exist_ok=True)
os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_label_dir, exist_ok=True)

class_counts = {"Notwaza": 0}
image_names_list = []
for i, text_dir in enumerate(input_text_dir):
    for text_file in os.listdir(text_dir):
        with open(os.path.join(text_dir, text_file), 'r') as f:
            first_line = f.readline().strip()
            class_name = first_line.split()[0]
            if class_name == "Notwaza" and class_counts["Notwaza"] >= 10000:
                continue
            else:
                if class_name not in class_counts:
                    class_counts[class_name] = 1
                else:
                    class_counts[class_name] += 1
                output_text_path = os.path.join(output_label_dir, class_name + "_senjou_" + str(class_counts[class_name]).zfill(5) + ".txt")
                with open(output_text_path, 'w') as f:
                    f.write(first_line)

                output_image_path = os.path.join(output_image_dir, class_name + "_senjou_" + str(class_counts[class_name]).zfill(5) + ".png")
                # 元画像を読み込む
                original_img = Image.open(os.path.join(input_image_dir[i], text_file.replace('.txt', '.jpeg')))
                # 新しい画像を作成 (608x608, 白背景)
                new_img = Image.new('RGB', (608, 608), 'white')
                # 元画像を新しい画像の上部に配置
                new_img.paste(original_img, (0, 0))
                # 保存
                new_img.save(output_image_path, 'PNG')
                image_names_list.append(class_name + "_senjou_" + str(class_counts[class_name]).zfill(5) + ".png")

# train.txtを新規作成または空にする
with open(os.path.join(output_dir, "train.txt"), "w") as f:
    pass

for image_name in image_names_list:
    with open(os.path.join(output_dir, "train.txt"), "a") as f:
        f.write(image_name + "\n")

print("\nクラスごとの画像数:")
for cls, count in class_counts.items():
    print(f"{cls}: {count}枚")
