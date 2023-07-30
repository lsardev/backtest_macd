from return_pct import get_pct_year

def get_grow_2018_2022(ticker):
    g2018 = get_pct_year(ticker, 2018)
    g2019 = get_pct_year(ticker, 2019)
    g2020 = get_pct_year(ticker, 2020)
    g2021 = get_pct_year(ticker, 2021)
    g2022 = get_pct_year(ticker, 2022)

    return [ticker, g2018, g2019, g2020, g2021, g2022]

