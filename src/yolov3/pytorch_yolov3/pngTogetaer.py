from PIL import Image
import os

# 画像が保存されているディレクトリ
input_dir = '0.7'
output_dir = '0.7/output'

# 出力ディレクトリが存在しない場合は作成
os.makedirs(output_dir, exist_ok=True)

# 画像を読み込む
images = []
for filename in os.listdir(input_dir):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path)

        # 画像を正方形にリサイズ
        size = max(img.size)
        new_img = Image.new("RGB", (size, size), (255, 255, 255))
        new_img.paste(img, ((size - img.size[0]) // 2, (size - img.size[1]) // 2))
        images.append(new_img)

# 画像を横に3枚、縦に3枚のグリッドで3つの画像を作成
grid_size = 3
num_grids = 3
if images:
    img_width, img_height = images[0].size
    total_width = img_width * grid_size
    total_height = img_height * grid_size

    for grid_index in range(num_grids):
        combined_image = Image.new('RGB', (total_width, total_height), (255, 255, 255))

        for row in range(grid_size):
            for col in range(grid_size):
                index = grid_index * grid_size * grid_size + row * grid_size + col
                if index < len(images):
                    combined_image.paste(images[index], (col * img_width, row * img_height))

        # 結合した画像を保存
        output_image_path = os.path.join(output_dir, f'combined_grid_{grid_index + 1}.jpg')
        combined_image.save(output_image_path)