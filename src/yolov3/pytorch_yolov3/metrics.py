import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルを読み込む
data = pd.read_csv('0.7/metrics.csv')

# データをDataFrameに変換
df = pd.DataFrame(data)

# 空の値をNaNに変換
df.replace("", float("NaN"), inplace=True)

# プロットの作成
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['AP'], marker='o', linestyle='-')
plt.title('AP Metrics')
plt.xlabel('Index')
plt.ylabel('AP')
plt.grid(True)

# PNGファイルとして保存
plt.savefig('0.7/metrics_plot.png')
plt.close()