import pandas as pd

# File path to the raw dataset
file_path = "data/raw/online_retail_sample.xlsx"

# Load the dataset
df = pd.read_excel(file_path)

# Basic inspection
print("Dataset loaded successfully.")
print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values by column:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())
