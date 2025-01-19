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
        
        # remove_class = ["F-throw", "U-throw", "D-throw", "B-throw", "Grab-blow", "Grab", "Notwaza"]
        remove_class = ["F-throw", "U-throw", "D-throw", "B-throw", "Grab-blow", "Grab"]
        
        # remove_class = ["Notwaza"]
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
        
        total_tp = 0  # 全クラスの True Positive の合計
        total_predicted = 0  # 全クラスの予測総数の合計
        total_actual = 0  # 全クラスの実際の総数の合計
        
        for label in sorted(set(list(label_counts.keys()) + list(label_predicted.keys()))):
            tp = label_correct.get(label, 0)
            predicted = label_predicted.get(label, 0)
            actual = label_counts.get(label, 0)
            
            total_tp += tp
            total_predicted += predicted
            total_actual += actual
            
            # Precision = TP / (TP + FP)
            precision = tp / predicted * 100 if predicted > 0 else 0
            
            # Recall = TP / (TP + FN)
            recall = tp / actual * 100 if actual > 0 else 0
    
            # F1 Score = 2 * (Precision * Recall) / (Precision + Recall)
            f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
            
            print(f"{label}\t{precision:.2f}%\t\t{recall:.2f}%\t\t{f1:.2f}　　　おまけ：TP: {tp}, FP: {predicted - tp}")
            
        # マクロ平均の計算と出力
        # 各クラスのPrecision、Recallの平均を計算
        precisions = []
        recalls = []
        for label in sorted(set(list(label_counts.keys()) + list(label_predicted.keys()))):
            if label not in remove_class:
                tp = label_correct.get(label, 0)
                predicted = label_predicted.get(label, 0)
                actual = label_counts.get(label, 0)
                
                precision = tp / predicted * 100 if predicted > 0 else 0
                recall = tp / actual * 100 if actual > 0 else 0
                
                precisions.append(precision)
                recalls.append(recall)
            
        macro_precision = sum(precisions) / len(precisions) if precisions else 0
        macro_recall = sum(recalls) / len(recalls) if recalls else 0
        macro_f1 = 2 * macro_precision * macro_recall / (macro_precision + macro_recall) if (macro_precision + macro_recall) > 0 else 0
        
        print("\n全体の指標:")
        print(f"Accuracy: {self.total_correct / self.total_samples * 100}%")
        print(f"Macro Precision: {macro_precision:.2f}%")
        print(f"Macro Recall: {macro_recall:.2f}%") 
        print(f"Macro F1-Score: {macro_f1:.2f}")

if __name__ == "__main__":
    accuracy = Accuracy("result_data/yolov3_yossi_electroplankton_24_1.txt", "result_data/yolov3_yossi_electroplankton_24_1.csv")
    accuracy.calculate_accuracy()
    # accuracy = Accuracy("result_data/yolov3_yossi_senjou_24_0.txt", "result_data/yolov3_yossi_senjou_24_0.csv")
    # accuracy.calculate_accuracy()
