from get_graphic_history import get_trade_history

all_trades = get_trade_history("VALE3", "2022")
for trade in all_trades:
    print(trade)