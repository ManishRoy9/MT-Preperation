import pandas as pd
import numpy as np
import re
import csv
import sys

def prepare(dataset_file, lang, lower=False):
    df = pd.read_csv(dataset_file, names=['Text'], sep="\0", quoting=csv.QUOTE_NONE, skip_blank_lines=False, on_bad_lines="skip")
    print("Dataframe shape (rows, columns):", df.shape)

    # Delete nan
    df = df.dropna()
    print("--- Rows with Empty Cells Deleted\t--> Rows:", df.shape[0])

    # Drop duplicates
    df = df.drop_duplicates()
    print("--- Duplicates Deleted\t\t\t--> Rows:", df.shape[0])

    # Drop too-long rows
    df["Too-Long"] = (df['Text'].str.count(' ') + 1) > 100
    df = df.set_index(['Too-Long'])
    try:
        df = df.drop([True])
    except:
        pass
    df = df.reset_index()
    df = df.drop(['Too-Long'], axis=1)
    print("--- Too Long Rows Deleted\t\t--> Rows:", df.shape[0])

    # Remove HTML and normalize
    df = df.replace(r'<.*?>|&lt;.*?&gt;|&?(amp|nbsp|quot);|{}', ' ', regex=True)
    df = df.replace(r'  ', ' ', regex=True)

    print("--- HTML Removed\t\t\t--> Rows:", df.shape[0])

    # Lower-case the data
    if lower:
        df['Text'] = df['Text'].str.lower()
        print("--- Rows are now lower-cased\t--> Rows:", df.shape[0])
    else:
        print("--- Rows will remain in true-cased\t--> Rows:", df.shape[0])

    # Replace empty cells with NaN
    df = df.replace(r'^\s*$', np.nan, regex=True)
    # Delete nan
    df = df.dropna()
    print("--- Rows with Empty Cells Deleted\t--> Rows:", df.shape[0])

    # Shuffle the data
    df = df.sample(frac=1).reset_index(drop=True)
    print("--- Rows Shuffled\t\t\t--> Rows:", df.shape[0])

    # Save the filtered dataset to a file
    output_file = dataset_file + '-filtered.' + lang
    df['Text'].to_csv(output_file, header=False, index=False, quoting=csv.QUOTE_NONE, sep="\n")
    print("--- Filtered Data Saved:", output_file)

# Dataset details
dataset_file = sys.argv[1]    # path to the monolingual dataset
lang = sys.argv[2]            # language of the dataset

# Run the prepare() function
# Data will be true-case; change to True to lower-case
prepare(dataset_file, lang, lower=False)