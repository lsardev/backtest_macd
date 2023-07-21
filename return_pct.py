from get_graphic_history import get_trade_history

def get_pct_year(ticker, year):
    list = get_trade_history(ticker, year)

    inicial = 1000
    cap_inicial = 1000
    for num in list:
        pct = num[-1]
        montante = cap_inicial + (cap_inicial/100 * pct)

        cap_inicial = montante

    pct_year = (cap_inicial - inicial)/(inicial/100)
    print("{} > {}".format(inicial, cap_inicial))
    print("{}|{}|{:.2f}%".format(ticker, year, pct_year))
    print("-"*100) 

    return "{:.2f}%".format(pct_year)



