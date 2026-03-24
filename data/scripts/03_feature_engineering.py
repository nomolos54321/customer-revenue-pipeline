import pandas as pd

# Load cleaned data
file_path = "data/cleaned/cleaned_data.csv"
df = pd.read_csv(file_path)

print("Before feature engineering:", df.shape)

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

# Create YearMonth column for monthly trend analysis
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)

print("After feature engineering:", df.shape)
print("\nNew columns added:")
print(["Revenue", "YearMonth"])

# Save transformed data
df.to_csv("data/cleaned/featured_data.csv", index=False)

print("Featured data saved successfully.")
