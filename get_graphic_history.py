import matplotlib.pyplot as plt
from get_macd import get_macd_sinal

def get_sinals(stock_name, year):
    df = get_macd_sinal(stock_name, year)

    menor = 0
    maior = 3

    num_vezes = int(len(df) - 2)

    sinais_de_compra_dia = []
    sinais_de_compra_valor = []

    sinais_de_venda_dia = []
    sinais_de_venda_valor = []

    for c in range(num_vezes):
        df_tres_numeros = df[menor:maior]

        if df_tres_numeros['Sinal'][1]>df_tres_numeros['MACD'][1] and df_tres_numeros['MACD'][2]>df_tres_numeros['Sinal'][2]:
            sinais_de_compra_dia.append(df_tres_numeros.index[2])
            sinais_de_compra_valor.append(df_tres_numeros['MACD'][2])
        
        
        if df_tres_numeros['Sinal'][1]<df_tres_numeros['MACD'][1] and df_tres_numeros['MACD'][2]<df_tres_numeros['Sinal'][2]:
            sinais_de_venda_dia.append(df_tres_numeros.index[2])
            sinais_de_venda_valor.append(df_tres_numeros['MACD'][2])

        menor += 1
        maior += 1


    return [sinais_de_compra_dia, sinais_de_compra_valor, sinais_de_venda_dia, sinais_de_venda_valor]

def plot_graphic(stock_name, year):
    
    df = get_macd_sinal(stock_name, year)
    list_sinals = get_sinals(stock_name, year)

    sinais_de_compra_dia = list_sinals[0]
    sinais_de_compra_valor = list_sinals[1]

    sinais_de_venda_dia = list_sinals[2]
    sinais_de_venda_valor = list_sinals[3]

    plt.plot(df["MACD"], label="macd")
    plt.plot(df["Sinal"], label="Sinal")
    plt.scatter(sinais_de_compra_dia, sinais_de_compra_valor, color='green', marker='o')
    plt.scatter(sinais_de_venda_dia, sinais_de_venda_valor, color="red", marker='o')
    plt.title()
    plt.savefig()

def get_trade_history(stock_name, year):

    df = get_macd_sinal(stock_name, year)
    list_sinals = get_sinals(stock_name, year)

    sinais_de_compra_dia = list_sinals[0]
    sinais_de_venda_dia = list_sinals[2]

    trades = []

    if str(sinais_de_venda_dia[0])[8:10] < str(sinais_de_compra_dia[0])[8:10]:
        sinais_de_venda_dia.pop(0)
        sinais_de_compra_dia.pop(-1)

    if len(sinais_de_compra_dia) > len(sinais_de_venda_dia):
        sinais_de_compra_dia.pop(-1)

    for numero_sinal in range(len(sinais_de_compra_dia)):
        venda = df[df.index == sinais_de_venda_dia[numero_sinal]]["Close"]
        compra = df[df.index == sinais_de_compra_dia[numero_sinal]]["Close"]

        compra = float(compra.iloc[0])
        venda = float(venda.iloc[0])

        dif = venda - compra
        um_pct = compra / 100
        pct_real = dif / um_pct

        trades.append([compra, venda, pct_real])

    return trades
    