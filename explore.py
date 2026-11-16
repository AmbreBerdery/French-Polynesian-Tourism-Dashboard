#first look at the data, we will run it once to understand data

import pandas as pd

#first, loading the dataset

df = pd.read_csv("data/11201.csv", sep=";", encoding = "utf-8") #separé par des virgules

#info about the dataset

print("Dimensions of the dataset: ", df.shape)
print("Columns names: ", list(df.columns))
print("First lines of the dataset: ", df.head())

print("Info about the dataset: ", df.info())

#missing values
print("Null values in the dataset: ", df.isnull().sum())
print("Missing values in the dataset ", df.isna().sum())

#duplicates
print("Number of duplicates lines: ", df.duplicated().sum())

#seems that everything is ok and there is no null or missing values



