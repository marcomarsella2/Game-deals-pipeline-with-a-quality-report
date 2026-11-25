import sqlite3
from pathlib import Path
from fetch_deals import fetch_deals
from clean import clean_deal

DB_PATH = Path("data/deals.db")

"-------------DO NOT TOUCH IF WORKS----------------"
def create_table():
    "Creates the deals table if it doesnt exit already"
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS deals (
                    dealID TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    storeID TEXT NOT NULL,
                    gameID TEXT,
                    salePrice REAL,
                    normalPrice REAL,
                    savings REAL,
                    metacriticScore INTEGER
                    )
                """)
    conn.commit()
    conn.close()

def save_deals(deals):
    "Inserts a list of deal dictionaries into the database, replacing any with the same dealID"
    create_table()
    cleaned_rows = [clean_deal(deal) for deal in deals]
    rows = [
        (
        deal["dealID"],
        deal["title"],
        deal["storeID"],
        deal.get("gameID"),
        deal.get("salePrice"),
        deal.get("normalPrice"),
        deal.get("savings"),
        deal.get("metacriticScore")
        )
        for deal in cleaned_rows
    ]


    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executemany(
        """
        INSERT OR REPLACE INTO deals
            (dealID, title, storeID, gameID, salePrice, normalPrice, savings, metacriticScore)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            rows,
    )
    conn.commit()
    conn.close()
    return len(rows)

if __name__ == "__main__":
    deals = fetch_deals()
    print(list(clean_deal(deals[0]).keys()))
    deals = fetch_deals()
    count = save_deals(deals)
    print(f"Saved {count} deals.")
