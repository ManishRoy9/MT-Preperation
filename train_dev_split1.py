import pandas as pd
import numpy as np
import re
import csv
import sys

segment_no = sys.argv[1]    # Number of segments in the dev set
dataset_file = sys.argv[2]  # Path to the dataset file

def extract_dev(segment_no, dataset_file):
    df = pd.read_csv(dataset_file, names=['Text'], sep="\0", quoting=csv.QUOTE_NONE, skip_blank_lines=False, on_bad_lines="skip")
    print("Dataframe shape:", df.shape)
    
    # Delete rows with empty cells
    df = df.dropna()
    print("--- Empty Cells Deleted", "--> Rows:", df.shape[0])
    
    # Extract Dev set from the main dataset
    df_dev = df.sample(n=int(segment_no))
    df_train = df.drop(df_dev.index)
    
    # Write the dataframe to train and dev files
    train_file = dataset_file + '.train'
    dev_file = dataset_file + '.dev'
    
    df_train.to_csv(train_file, header=False, index=False, quoting=csv.QUOTE_NONE, sep="\n")
    df_dev.to_csv(dev_file, header=False, index=False, quoting=csv.QUOTE_NONE, sep="\n")
    
    print("--- Wrote Files")
    print("Done!")
    print("Output files:", train_file, dev_file)


extract_dev(segment_no, dataset_file)