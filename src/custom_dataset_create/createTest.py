import os
import shutil
from PIL import Image

# 入力ディレクトリのパス
input_text_dir = ["../../output/texts/air_test_0", "../../output/texts/b_test_0",
                  "../../output/texts/grab_test_0", 
                  "../../output/texts/smash_test_0", 
                  "../../output/texts/jabDa_test_0", "../../output/texts/tilt_test_0",
                  "../../output/texts/nb_test_0"
                ]
input_image_dir = ["../../input/images/air_test_0/resize2", "../../input/images/b_test_0/resize2",
                   "../../input/images/grab_test_0/resize2", 
                   "../../input/images/smash_test_0/resize2", 
                   "../../input/images/jabDa_test_0/resize2", "../../input/images/tilt_test_0/resize2",
                   "../../input/images/nb_test_0/resize2"
                ]

# input_text_dir = ["../../output/texts/air_senjou_test_0", "../../output/texts/b_senjou_test_0",
#                 #   "../../output/texts/grab_senjou_test_0", 
#                   "../../output/texts/smash_senjou_test_0", 
#                   "../../output/texts/jabDa_senjou_test_0", "../../output/texts/tilt_senjou_test_0"
#                 ]
# input_image_dir = ["../../input/images/air_senjou_test_0/resize2", "../../input/images/b_senjou_test_0/resize2",
#                 #    "../../input/images/grab_senjou_test_0/resize2", 
#                    "../../input/images/smash_senjou_test_0/resize2", 
#                    "../../input/images/jabDa_senjou_test_0/resize2", "../../input/images/tilt_senjou_test_0/resize2"
#                 ]

# 出力ディレクトリのパス
output_dir = "../pytorch_yolov3/custom_dataset"
output_image_dir = os.path.join(output_dir, "images")
output_label_dir = os.path.join(output_dir, "labels")

# 出力ディレクトリが存在しない場合は作成
os.makedirs(output_dir, exist_ok=True)
os.makedirs(output_image_dir, exist_ok=True)
os.makedirs(output_label_dir, exist_ok=True)

remove_class = ["D-smash"]
remove_class_num = []

class_counts = {"Notwaza": 0}
image_names_list = []
for i, text_dir in enumerate(input_text_dir):
    for text_file in os.listdir(text_dir):
        with open(os.path.join(text_dir, text_file), 'r') as f:
            first_line = f.readline().strip()
            class_name = first_line.split()[0]
            if class_name == "Notwaza" and class_counts["Notwaza"] >= 2000:
                continue
            else:
                if class_name in remove_class:
                    continue
                elif class_name not in class_counts:
                    class_counts[class_name] = 1
                else:
                    class_counts[class_name] += 1
                output_text_path = os.path.join(output_label_dir, class_name + "_test_" + str(class_counts[class_name]).zfill(4) + ".txt")
                with open(output_text_path, 'w') as f:
                    f.write(first_line)

                output_image_path = os.path.join(output_image_dir, class_name + "_test_" + str(class_counts[class_name]).zfill(4) + ".png")
                # 元画像を読み込む
                original_img = Image.open(os.path.join(input_image_dir[i], text_file.replace('.txt', '.jpeg')))
                # 新しい画像を作成 (608x608, 白背景)
                new_img = Image.new('RGB', (608, 608), 'white')
                # 元画像を新しい画像の上部に配置
                new_img.paste(original_img, (0, 0))
                # 保存
                new_img.save(output_image_path, 'PNG')
                image_names_list.append(class_name + "_test_" + str(class_counts[class_name]).zfill(4) + ".png")

# train.txtを新規作成または空にする
with open(os.path.join(output_dir, "test.txt"), "w") as f:
    pass

for image_name in image_names_list:
    with open(os.path.join(output_dir, "test.txt"), "a") as f:
        f.write(image_name + "\n")

print("\nクラスごとの画像数:")
for cls, count in class_counts.items():
    print(f"{cls}: {count}枚")
