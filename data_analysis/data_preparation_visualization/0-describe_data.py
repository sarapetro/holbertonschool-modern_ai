#!/usr/bin/env python3
import pandas as pd
df = pd.read_csv('"C:\Users\sara\Downloads\94d36c24104e5cfdda80bac5c6dbacec0b5c6cf6"')
shape = df.shape
data_types = df.dtypes
head = df.head()
missing_count = df.isna().sum()
duplicates = df.duplicated().sum()
print("Shape:", shape)
print("Dtypes:\n", data_types)
print("First rows:\n", head)
print("Missing values:\n", missing_count)
print("Duplicates:", duplicates)
