import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSVファイルを読み込む
file_path = 'train_output/history_final.csv'
data = pd.read_csv(file_path)

# データの確認
print(data.head())

# グラフの作成
plt.figure(figsize=(14, 6))

# 総損失のプロット
plt.plot(data['iter'], data['loss_total'], label='Total Loss', color='blue', linewidth=1)

# グラフの詳細設定
plt.xlabel('Iteration')
plt.ylabel('Validation Total Loss')
plt.title('Validation Total Loss Over Iterations')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# y軸のメモリの細かさを設定
y_min, y_max = data['loss_total'].min(), data['loss_total'].max()
plt.yticks(np.arange(y_min, y_max, (y_max - y_min) / 20))

# グラフを表示
plt.tight_layout()
plt.show()