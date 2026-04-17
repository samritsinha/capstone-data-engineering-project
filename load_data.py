import pandas as pd
from sqlalchemy import create_engine

# 🔴 Change password if yours is different
engine = create_engine("mysql+pymysql://root:root123@localhost/ecommerce")

# Load cleaned data
df = pd.read_csv("data/clean_orders.csv")

# Insert into MySQL
df.to_sql("orders", con=engine, if_exists="replace", index=False)

print("Data inserted into MySQL ✅")