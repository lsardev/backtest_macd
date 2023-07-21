#pegando o codigo da ação e o ano para ser averiguado
import yfinance as yf

def get_dataframe_ticker(stock_name, year):
    ticker = yf.Ticker("{}.SA".format(stock_name))

    start = "{}-01-01".format(year)
    end = "{}-12-31".format(year)

    stock_dataframe = ticker.history(interval='1d', start=start, end=end)

    return stock_dataframe

print(get_dataframe_ticker("VALE3", "2022"))