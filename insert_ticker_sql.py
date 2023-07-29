import sqlite3
from get_grow_2018_2022 import get_grow_2018_2022

def insert_into_sql_table(ticker):

    list_for_insert = get_grow_2018_2022(ticker)
    ticker = list_for_insert[0]
    pct_2018 = list_for_insert[1]
    pct_2019 = list_for_insert[2]
    pct_2020 = list_for_insert[3]
    pct_2021 = list_for_insert[4]
    pct_2022 = list_for_insert[5]

    conn = sqlite3.connect("2018_2022.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO pct_grow (ticker, pct_2018, pct_2019, pct_2020, pct_2021, pct_2022) VALUES (?, ?, ?, ?, ?, ?)", (ticker, pct_2018, pct_2019, pct_2020, pct_2021, pct_2022))

    conn.commit()

    conn.close()