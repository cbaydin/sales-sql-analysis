import pandas as pd
import sqlite3

# CSV'yi oku
df = pd.read_csv("SampleSuperstore.csv")

# SQLite veritabanı oluştur
conn = sqlite3.connect("sales.db")

# Tabloyu veritabanına yaz
df.to_sql("orders", conn, if_exists="replace", index=False)

# Örnek SQL sorgusu
query = """
SELECT
    ROUND(SUM(Sales),2) AS total_sales,
    ROUND(SUM(Profit),2) AS total_profit,
    COUNT(DISTINCT [Order ID]) AS total_orders
FROM orders;
"""

result = pd.read_sql_query(query, conn)
print(result)

conn.close()
