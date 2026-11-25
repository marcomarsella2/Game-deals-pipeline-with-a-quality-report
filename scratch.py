import sqlite3
conn = sqlite3.connect("data/deals.db")
print(conn.execute("SELECT COUNT(*) FROM deals").fetchone())
print(conn.execute("SELECT title, salePrice FROM deals LIMIT 3").fetchall())