import json
import requests
from pandas.io.json import json_normalize

#url_info = {"upbit" : ["https://api.upbit.com", "/v1/candles/minutes/1" , "market", "KRW-BTC"],
#"binance" : ["https://api.binance.com", "/api/v3/ticker/price", "symbol", "BTCUSDT"],
#"bithum" : ["https://api.bithumb.com", "/public/ticker/BTC", "symbol" , "BTCUSDT" ]}

# url_info = {"upbit" : {"base_url":"https://api.upbit.com", "sub_url":"/v1/candles/minutes/1" , "param_key":"market", "param_value":"KRW-BTC", "symbol":"market", "price":"trade_price"},
# "binance" : {"base_url":"https://api.binance.com", "sub_url":"/api/v3/ticker/price", "param_key":"symbol", "param_value":"BTCUSDT", "symbol":"symbol", "price":"price"},
# }
# #"bithum" : {"base_url":"https://api.bithumb.com", "sub_url":"/public/ticker/BTC", "param_key":"symbol" , "param_value":"BTCUSDT" }}

#코인 이름을 키값으로 설정
url_info = {
    "BTC" : [
            {"store":"upbit","base_url":"https://api.upbit.com", "sub_url":"/v1/candles/minutes/1" , "param_key":"market", "param_value":"KRW-BTC", "symbol":"market", "price":"trade_price"},
            {"store":"binance","base_url":"https://api.binance.com", "sub_url":"/api/v3/ticker/price", "param_key":"symbol", "param_value":"BTCUSDT", "symbol":"symbol", "price":"price", "coin":"bitcoin"}
    ],
    
    "ETH" : [
            {"store":"upbit","base_url":"https://api.upbit.com", "sub_url":"/v1/candles/minutes/1" , "param_key":"market", "param_value":"KRW-ETH", "symbol":"market", "price":"trade_price"},
            {"store":"binance","base_url":"https://api.binance.com", "sub_url":"/api/v3/ticker/price", "param_key":"symbol", "param_value":"ETHUSDT", "symbol":"symbol", "price":"price","coin":"ethereim"}
    ],
}
#"bithum" : {"base_url":"https://api.bithumb.com", "sub_url":"/public/ticker/BTC", "param_key":"symbol" , "param_value":"BTCUSDT" }}
# market = "upbit"

def get_market(market):
    dict_res ={}
    price = 0.1
    symbol = ""
    #url = url_info[market][0]
    #res = requests.get(url +url_info[market][1], params={url_info[market][2]:url_info[market][3]})
    res = requests.get(url_info[market]['base_url'] +url_info[market]['sub_url'], params={url_info[market]['param_key']:url_info[market]['param_value']})
    Market_result = res.json()
    print(type(Market_result))
    if(str(type(Market_result))=="<class 'dict'>"):
        print("dict형식 입니다")
        print(Market_result)
        price = float(Market_result[url_info[market]['price']])
        #symbol = Market_result[url_info[market]['symbol']]

        # price = float(result['price']) #price str -> float로 형변환
        # result['price'] = price #바이낸스 가격 저장
    elif(str(type(Market_result))=="<class 'list'>"):
        print("list입니다")
        # 업비트의 price는 binance와 1000:1 관계
        price = Market_result[0][url_info[market]['price']]
        #symbol = Market_result[0][url_info[market]['symbol']]
        
    dict_res['market'] = market
    dict_res['coin_type'] = "BTC"
    dict_res['price'] = price
    str_Market_result = json.dumps(dict_res)
    json_Market_result = json.loads(str_Market_result) #json의 string 형태의 객체에서 json 형식 내용을 추출할 때 사용한다.
    pandas_Market_result = json_normalize(json_Market_result) #json에서 데이터프레임을 쉽게 생성하도록 도움을 준다
    return pandas_Market_result

def get_market_all():
    list_market =[]
    for key in url_info.keys():
        # get_market(key)
        list_market.append(get_market(key))
    return list_market

print(get_market_all())