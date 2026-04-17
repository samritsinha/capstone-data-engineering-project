import pandas as pd

# Load dataset
df = pd.read_csv("data/orders.csv")

print("Original Data:")
print(df)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert date format
df['order_date'] = pd.to_datetime(df['order_date'])

# Save cleaned data
df.to_csv("data/clean_orders.csv", index=False)

print("\nCleaned Data Saved ✅")