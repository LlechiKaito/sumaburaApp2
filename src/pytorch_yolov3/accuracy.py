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
        label_counts = {}
        label_correct = {}
        for i, value in enumerate(self.txt_df):
            # Convert numpy array to string
            label = value[0]
            judge_elements = self.csv_df[self.csv_df["No"] == i]
            if not judge_elements.empty:
                max_score_idx = judge_elements["Score"].idxmax()
                max_score_row = judge_elements.loc[max_score_idx]
                if max_score_row["Label"] == label:
                    self.total_correct += 1
                    if label not in label_correct:
                        label_correct[label] = 1
                    else:
                        label_correct[label] += 1
            self.total_samples += 1
            if label not in label_counts:
                label_counts[label] = 1
            else:
                label_counts[label] += 1
        print(self.total_samples, self.total_correct)
        print(f"Accuracy: {self.total_correct / self.total_samples * 100}%")
        print(label_counts)
        for label, count in label_counts.items():
            if label in label_correct:
                print(f"{label}: {label_correct[label] / count * 100}%")
            else:
                print(f"{label}: 0%")

if __name__ == "__main__":
    accuracy = Accuracy("custom_dataset/test.txt", "result_data/yolov3_yossi_electroplankton_24_1_to18.csv")
    accuracy.calculate_accuracy()
