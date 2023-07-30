import sqlite3

tickers = [["VALE3", "Minerios e Petroleo"], ["JBSS3", "Agronegocio"], ["MRFG3", "Agronegocio"], ["PETR3", "Minerios e Petroleo"]]
for ticker in tickers:
    try:
        conn = sqlite3.connect("2018_2022.db")
        cursor = conn.cursor()

        valor_para_adicionar = ticker[1]
        cursor.execute("UPDATE pct_grow SET sector = ? WHERE ticker = ?", (valor_para_adicionar, ticker[0]))
        conn.commit()
        print("Valores atualizados na nova coluna com sucesso.")
    except sqlite3.Error as e:
        print("Erro ao atualizar a nova coluna:", e)

    conn.close()