import pandas as pd
import csv
import os

dir = "/home/pbl9/group10/results/csv_results"
fnames = os.listdir(dir)
# getting top 5 & top 1 accuracy for each csv files 
dfs_5 = []
dfs_1 = []
for fname in fnames : 
    path = os.path.join(dir, fname)
    f = open(path, "r")
    csv_reader = csv.reader(f)

    data = []
    for row in csv_reader :
        data.append(row)
    
    sliced = data[data.index(['epoch', 'train_acc', 'test_acc']):]
    df = pd.DataFrame(sliced[1:], columns=sliced[0])
    top_5 = df.sort_values('test_acc', ascending=False).head(5)
    top_5['fname'] = [fname]*5
    dfs_5.append(top_5)

    top_1 = df.sort_values('test_acc', ascending=False).head(1)
    top_1['fname'] = [fname]
    dfs_1.append(top_1)
# make new dataframe to save results and save it in csv file
result_5 = pd.concat(dfs_5, ignore_index=True)
result_5.to_csv("./top5_best_accuracy.csv", index=False)
result_1 = pd.concat(dfs_1, ignore_index=True)
result_1.to_csv("./top1_best_accuracy.csv", index=False)