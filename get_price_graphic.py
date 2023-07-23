import os
from get_ticker import get_dataframe_ticker
from get_graphic_history import get_sinals
import matplotlib.pyplot as plt

def show_price_graphic(ticker, year):

    df = get_dataframe_ticker(ticker, year)
    sinals = get_sinals(ticker, year)

    dias_compra = sinals[0]
    dias_venda = sinals[2]

    dias_sinais_compra = []
    for dia in dias_compra:
        sinal = float(df[df.index == dia]["Close"])
        dias_sinais_compra.append(sinal)
    
    dias_sinais_venda = []
    for dia in dias_venda:
        sinal = float(df[df.index == dia]["Close"])
        dias_sinais_venda.append(sinal)

    plt.plot(df["Close"], label="Valor da ação")
    plt.scatter(dias_compra, dias_sinais_compra, color='green', marker='o', label="Sinais de compra")
    plt.scatter(dias_venda, dias_sinais_venda, color="red", marker='o', label="Sinais de venda")
    plt.title("Valor da ação: {} com entradas e saídas no ano de {}".format(ticker, year))
    plt.legend(loc="upper left")
    
    nome_arquivo = "valor_{}_{}".format(ticker, year) 
    pasta_destino = "graficos" 

    caminho_arquivos = os.path.join(pasta_destino, nome_arquivo)

    plt.savefig(caminho_arquivos, format="png")

    return caminho_arquivos
