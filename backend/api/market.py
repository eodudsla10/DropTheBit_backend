import requests

# 이거 DB에 입력하면 > url_info = {}, coin_info = {} 를 채우는 함수 만들어야 함
url_info = {
    "upbit" : {
            "base_url":"https://api.upbit.com", "sub_url":"/v1/candles/minutes/1" , "param_key":"market", "symbol":"market", "price":"trade_price", "data_type":"list"
    },

    "binance" : {
            "base_url":"https://api.binance.com", "sub_url":"/api/v3/ticker/price", "param_key":"symbol", "symbol":"symbol", "price":"price", "data_type":"dict"
    },
}

# API 호출 시 market 별로 다른 coin 명칭 필요
coin_info = {
    # "upbit" : {"BTC":"KRW-BTC", "ETH":"KRW-ETH"},
    # "binance" : {"BTC":"BTCUSDT", "ETH":"ETHUSDT"}
}

def load_db():
    # url_info = MongoDbManager().get_url_info({})
    # coin_info = MongoDbManager().get_coin_info({})
    pass


u_res = requests.get("https://api.upbit.com/v1/market/all", params={"isDetails":"false"})
b_res = requests.get("https://api.binance.com/api/v3/exchangeInfo")
u_Market_result = u_res.json()
b_Mareket_result = b_res.json()['symbols']

#f_all = open('C:/Users/ChoiJeongSun/Desktop/CoinNameAll.txt','w')

#f_all.write('{\n')
u_market = "upbit"
name_kr = "name_kr"
name_en = "name_en"
coin_info[u_market] = {}
for dict_coin in u_Market_result:
    u_coin = dict_coin[url_info[u_market]["param_key"]] # u_coin = KRW-BTC
    if u_coin[0:3] == "KRW":
        data = u_coin.split('-')
        coin_info[u_market][data[1]] = u_coin
        #f_all.write('\''+data[1]+'\''+ ':{\''+name_kr+'\':\''+dict_coin['korean_name']+'\', \''+name_en+'\':\''+dict_coin['english_name']+'\'},\n')
#f_all.write('}')  
#f_all.close()      

b_market = "binance"
coin_info[b_market] = {}
for dict_coin in b_Mareket_result:
    b_coin = dict_coin[url_info[b_market]["param_key"]]
    if b_coin[-4:] == "USDT":
        data = b_coin[:-4]
        if data in coin_info['upbit'].keys(): #업비트에 있는 코인에 대한 데이터만 binance에서 고르기
            coin_info[b_market][data] = b_coin


#f = open('C:/Users/ChoiJeongSun/Desktop/CoinList.txt','w')
#for market in coin_info.keys():
#    f.write('\n')
#    f.write(market)
#    f.write('\n')
#    for coin in coin_info[market].keys():
#        f.write(coin)
#        f.write(' : ')
#        f.write(coin_info[market][coin])
#        f.write('\n')
#f.close()

def get_market(market):
    #res_list =[]
    dict_coin_info ={}
    dict_res = {}
    index = 0
    price = 0.1
    symbol = ""

    for coin in coin_info[market].keys():

        while True:
            try:
                res = requests.get(url_info[market]['base_url'] +url_info[market]['sub_url'], params={url_info[market]['param_key']:coin_info[market][coin]})
                Market_result = res.json()
                #print('-----'+coin+'-----')
                if(url_info[market]['data_type']=="dict"):
                    price = float(Market_result[url_info[market]['price']])
                    # price = float(result['price']) #price str -> float로 형변환
                    # result['price'] = price #바이낸스 가격 저장
                elif(url_info[market]['data_type']=="list"):
                    # 업비트의 price는 binance와 1000:1 관계
                    price = Market_result[0][url_info[market]['price']]

                break

            except Exception as ex:
                pass

        dict_coin_info[coin] = price

    dict_res[market] = dict_coin_info
    return dict_res


def get_market_all():
    # DB로부터 url_info, coin_info를 채우는 함수 호출 필요
    dict_market = {}
    for key in url_info.keys():
        market = get_market(key)
        dict_market[key] = market[key]
    return dict_market

# print(get_market('upbit'))
# print(get_market_all())

# 판다스로 값을 불러올 때, dict 형식이 아니기 때문에 key, value로 쪼개서 다시 배치할 수가 없다!
# arbitrage.py로 넘겨줘야 할 형식은 다음과 같다!
# {
#     'upbit':{'BTC':100, 'ETH':200},
#     'binance':{'BTC':300, 'ETH':400}
# }

# 이래야 arbitrage.py에서 v[market][coin] 해서 price를 바로 불러올 수 있음