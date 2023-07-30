# backtest_macd
Fazendo uma estratégia de investimento baseada no indicador de Analise Tecnica MACD e retornando o crescimento da ação


## O que é o indicador MACD ?
O indicador MACD (Moving Average Convergence Divergence) é uma estratégia muito utilizada por traders do mundo inteiro, a estratégia foi criada em 1960 por Gerard Apple com o intuito de monitorar a aceleração ou desaceleração das tendencias de preços das ações. A MACD é uma estratégia de Trend Following, uma estrategia de investimentos que consiste em analizar tendencias nas ações e em outros ativos do mercado financeiro.

## Como funciona o calculo da MACD ?
O calculo da MACD é feito por meio da diferença entre a media móvel curta e a média móvel longa, que no caso do nosso algoritmo será feito através de uma média de 12 dias para médias exponenciais rapidas e uma média de 26 dias para médias exponenciais lentas, que são as medidas mais comuns utilizadas pelos traders para utilizam a MACD.

<img src="/sinais/Captura de tela 2023-07-30 164914.png">

É traçada sobre a MACD uma linha sinal, que quando encontra com a linha MACD de cima para baixo é utilizada como sinal de venda e quando encontra a linha MACD de baixo para cima é utilizada como sinal de compra. Veja um exemplo dos sinais de compra e de venda, sendo os sinais de venda verde e os sinais de compra vermelho.

<img src="/sinais/sinalex.png">

Descobrimos então os sinais de compra e venda das ações e quanto rendeu a ação em cada ano e colocamos em um grafico no pdf:

<img src="/pdfs/VALE3-2022.pdf">

Em nosso algoritmo colocamos também uma funcionalidade que retorna o crescimento das ações nos últimos 5 anos antes do ano atual (2023):

<img src="/pdfs_2018_2020/VALE3_2018_2020">

## Lembrando
Não estou fazendo nenhuma recomendação de estratégia para fazer trade, apenas estou mostrando com fins educacionais como algoritmos podem ajudar a tomar decisões no mercado financeiro.

