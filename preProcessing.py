import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import LstmM.lstmFun
from subprocess import check_output

import splitData

dframe = pd.read_csv("data/label_data/ner.csv", encoding = "ISO-8859-1")


# Change "Sentence #" column name to "sentence_idx"
dframe = dframe.rename(columns={"Sentence #": "sentence_idx"})
dframe = dframe.rename(columns={"Word": "word"})
dframe = dframe.rename(columns={"POS": "pos"})
dframe = dframe.rename(columns={"Tag": "tag"})

# Remove "Sentence: " from the values in "sentence_idx" column
dframe["sentence_idx"] = dframe["sentence_idx"].str.replace("Sentence: ", "")

dframe["sentence_idx"].fillna(method="ffill", inplace=True)

# Convert the values in the "sentence_idx" column to integers
dframe["sentence_idx"] = dframe["sentence_idx"].astype(int)

print(dframe.head(60))
output_file = "data/label_data/nerReformat.csv"
dframe.to_csv(output_file, index=False)



# convert data to train and test run this part of code only for the first time
data = pd.read_csv("data/label_data/nerReformat.csv", encoding='latin-1')

output_dir = "data/label_data/"
splitData.split_data(data, output_dir, "ner")

