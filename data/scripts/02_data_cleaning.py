import pandas as pd

# Load raw data
file_path = "data/raw/online_retail_sample.xlsx"
df = pd.read_excel(file_path)

print("Before cleaning:", df.shape)

# -------------------------
# 1. Remove missing Customer IDs
# -------------------------
df = df.dropna(subset=["Customer ID"])

# -------------------------
# 2. Remove duplicates
# -------------------------
df = df.drop_duplicates()

# -------------------------
# 3. Remove negative or zero quantities
# -------------------------
df = df[df["Quantity"] > 0]

# -------------------------
# 4. Remove negative prices
# -------------------------
df = df[df["Price"] > 0]

print("After cleaning:", df.shape)

# Save cleaned data
df.to_csv("data/cleaned/cleaned_data.csv", index=False)

print("Cleaned data saved successfully.")
