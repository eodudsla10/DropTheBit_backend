import ccxt
import pyupbit


def get_coin_up_info():
    dict_market1 ={}
    ticker = pyupbit.get_tickers()
    dict_market1["upbit"] = ticker

    return dict_market1

def get_coin_bin_info():
    binance = ccxt.binance()
    markets = binance.fetch_tickers()
    
    return markets.keys()



print(get_coin_up_info())

# 업비트


# 바이낸스
# dict_keys(['ETH/BTC', 'LTC/BTC', 'BNB/BTC', 'NEO/BTC', 'QTUM/ETH', 'EOS/ETH',

# 업비트
# {'upbit': ['KRW-BTC', 'KRW-ETH', 'BTC-ETH', 'BTC-LTC', 'BTC-XRP'