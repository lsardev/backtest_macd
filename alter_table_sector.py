import sqlite3

conn = sqlite3.connect("2018_2022.db")
cursor = conn.cursor()

try:
    cursor.execute("ALTER TABLE pct_grow ADD COLUMN sector TEXT")
    conn.commit()
    print("Nova coluna adicionada com sucesso.")
except sqlite3.OperationalError as e:
    print("Erro ao adicionar a nova coluna:", e)

conn.close