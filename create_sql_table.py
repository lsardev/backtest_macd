import sqlite3

conn = sqlite3.connect("2018_2022.db")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS pct_grow 
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               ticker CHAR(6) NOT NULL,
               pct_2018 FLOAT NOT NULL,
               pct_2019 FLOAT NOT NULL,
               pct_2020 FLOAT NOT NULL,
               pct_2021 FLOAT NOT NULL,
               pct_2022 FLOAT NOT NULL)
''')

conn.commit()

conn.close()