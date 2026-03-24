import pandas as pd
import mysql.connector

# File path
csv_path = "data/cleaned/featured_data.csv"

# Load data
df = pd.read_csv(csv_path)

print("Featured data loaded successfully.")
print("Shape:", df.shape)

# MySQL connection details (EDIT THESE)
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Solomon1.",
    database="retail_pipeline"
)

cursor = conn.cursor()

# Create table (basic structure)
create_table_query = """
CREATE TABLE IF NOT EXISTS retail_transactions (
    Invoice VARCHAR(50),
    StockCode VARCHAR(50),
    Description TEXT,
    Quantity INT,
    InvoiceDate DATETIME,
    Price FLOAT,
    Customer_ID FLOAT,
    Country VARCHAR(100),
    Revenue FLOAT,
    YearMonth VARCHAR(10)
)
"""

cursor.execute(create_table_query)

print("Table created successfully.")

# Insert data row by row
for _, row in df.iterrows():
    insert_query = """
    INSERT INTO retail_transactions (
        Invoice, StockCode, Description, Quantity,
        InvoiceDate, Price, Customer_ID, Country,
        Revenue, YearMonth
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = tuple(row)

    cursor.execute(insert_query, values)

conn.commit()

print("Data inserted successfully.")

# Validate
cursor.execute("SELECT COUNT(*) FROM retail_transactions")
count = cursor.fetchone()

print("Total rows in table:", count[0])

# Close connection
cursor.close()
conn.close()

print("MySQL load complete.")
