from get_ticker import get_dataframe_ticker

def get_macd_sinal(stock_name, year):
    dataframe = get_dataframe_ticker(stock_name, year)

    #média dos 12 períodos
    mme12 = dataframe['Close'].ewm(span=12).mean()

    #média dos 26 períodos
    mme26 = dataframe['Close'].ewm(span=26).mean()

    #macd
    macd = mme12 - mme26

    #linha de sinal de compra e venda
    sinal=macd.ewm(9).mean()

    #colocando dados do MACD e sinal no dataframe
    dataframe['MACD'] = macd
    dataframe['Sinal'] = sinal

    return dataframe