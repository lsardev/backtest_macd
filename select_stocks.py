import sqlite3

def get_media(sector, year):
    conn = sqlite3.connect("2018_2022.db")
    cursor = conn.cursor()

    pct_year = "pct_{}".format(year)

    cursor.execute("SELECT AVG({}) AS media FROM pct_grow WHERE sector = ?".format(pct_year), (sector,))
    media = cursor.fetchone()[0]
    print("A média do setor: {} em {} é {:.2f}%".format(sector, year, media))

    conn.close

    return media

def get_media_2018_2020(sector):
    m2018 = get_media(sector, 2018)
    m2019 = get_media(sector, 2019)
    m2020 = get_media(sector, 2020)
    m2021 = get_media(sector, 2019)
    m2022 = get_media(sector, 2022)

    mTotal = (m2018 + m2019 + m2020 + m2021 + m2022)/5

    print("A média total do setor {} é: {:.2f}%".format(sector, mTotal))

get_media_2018_2020("Minerios e Petroleo")