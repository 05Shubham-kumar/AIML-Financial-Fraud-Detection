import pandas as pd
from pathlib import Path

data_path=Path("data/paysim.csv")

df=pd.read_csv(data_path)

print(df.shape)
print(df.head())
print(df.describe())
print(df.info())
print(df.isnull().sum())
print(df.columns.tolist())

if "type" in df.columns:
    print(df['type'].value_counts())

if "is_Fraud" in df.columns:
    print(df['is_Fraud'].value_counts())