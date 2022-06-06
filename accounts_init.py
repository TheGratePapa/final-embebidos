import sqlite3

# Datos iniciales
cards = [
    {"card_id": 0xAABBCCDD, "code": "1470", "balance": 50020},  # $500.20 = 50020
    {"card_id": 0xDDCCBBAA, "code": "0963", "balance": 1530},   # $15.30 = 1530
    {"card_id": 2739627546, "code": "1234", "balance": 42069}   # $429.69 = 42969
]

con = sqlite3.connect("accounts.db")
cur = con.cursor()

# Crear tabla
cur.execute(
    """CREATE TABLE IF NOT EXISTS accounts
       (card_id INTEGER PRIMARY KEY, code TEXT, balance INTEGER)"""
)

# Insertar datos iniciales
cur.executemany("INSERT OR REPLACE INTO accounts VALUES (:card_id, :code, :balance)", cards)

con.commit()
con.close()
