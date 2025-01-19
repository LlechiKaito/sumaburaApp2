import csv
import os
import pandas as pd
import numpy as np

class Accuracy():
    def __init__(self, txt_dir, csv_dir):
        self.test_txt_dir = txt_dir
        self.result_csv_dir = csv_dir
        self.total_correct = 0
        self.total_samples = 0
        self.csv_df = pd.read_csv(self.result_csv_dir)
        temp = pd.read_csv(self.test_txt_dir, index_col=None, header=None)
        self.txt_df = temp.values
        for i, value in enumerate(self.txt_df):
            self.txt_df[i] = value[0].split(".")[0].split("_")[0]

    def calculate_accuracy(self):
        label_counts = {}  # 真のラベルの総数
        label_correct = {}  # 正しく予測できた数
        label_predicted = {}  # 予測した総数
        
        remove_class = ["F-throw", "U-throw", "D-throw", "B-throw", "Grab-blow", "Grab"]
        # remove_class = []
        
        for i, value in enumerate(self.txt_df):
            true_label = value[0]
            judge_elements = self.csv_df[self.csv_df["No"] == i]
            if true_label in remove_class:
                continue

            if not judge_elements.empty:
                max_score_idx = judge_elements["Score"].idxmax()
                max_score_row = judge_elements.loc[max_score_idx]
                pred_label = max_score_row["Label"]
                
                # 予測したラベルの集計
                if pred_label not in label_predicted:
                    label_predicted[pred_label] = 1
                else:
                    label_predicted[pred_label] += 1
                    
                if pred_label == true_label:
                    self.total_correct += 1
                    if true_label not in label_correct:
                        label_correct[true_label] = 1
                    else:
                        label_correct[true_label] += 1
                        
            self.total_samples += 1
            if true_label not in label_counts:
                label_counts[true_label] = 1
            else:
                label_counts[true_label] += 1

        # 全体の正解率を出力
        print(self.total_samples, self.total_correct)
        print(f"Accuracy: {self.total_correct / self.total_samples * 100}%")
        print(label_counts)
        for label, count in label_counts.items():
            if label in label_correct:
                print(f"{label}: 正解数：{ label_correct[label] }, 総数：{ count }")
                print(f"{label}: {label_correct[label] / count * 100}%")
            else:
                print(f"{label}: 0%")
        
        # Precision, Recall, F値の計算と出力
        print("\nPrecision, Recall, and F-score:")
        print("Label\tPrecision\tRecall\t\tF1-Score")
        print("-" * 50)
        
        for label in sorted(set(list(label_counts.keys()) + list(label_predicted.keys()))):
            # Precision = TP / (TP + FP)
            precision = label_correct.get(label, 0) / label_predicted.get(label, 1) * 100
            
            # Recall = TP / (TP + FN)
            recall = label_correct.get(label, 0) / label_counts.get(label, 1) * 100
    
            # F1 Score = 2 * (Precision * Recall) / (Precision + Recall)
            f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
            
            print(f"{label}\t{precision:.2f}%\t\t{recall:.2f}%\t\t{f1:.2f}　　　おまけ：TP: {label_correct.get(label, 0) }, FP: {label_predicted.get(label, 1) - label_correct.get(label, 0) }")

if __name__ == "__main__":
    accuracy = Accuracy("train_data/yolov3_yossi_electroplankton_24_1.txt", "result_data/yolov3_yossi_electroplankton_24_1.csv")
    accuracy.calculate_accuracy()
    # accuracy = Accuracy("train_data/yolov3_yossi_senjou_24_0.txt", "result_data/yolov3_yossi_senjou_24_0.csv")
    # accuracy.calculate_accuracy()
