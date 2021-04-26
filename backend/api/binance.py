import json
import requests
from pandas.io.json import json_normalize

# def Binance():
#     url = "https://api.binance.com"
#     res = requests.get(url + "/api/v3/ticker/price", params={'symbol': "BTCUSDT"})
#     Bin_result = res.json()
#     print(Bin_result)
#     binance_price = float(Bin_result['price'])
#     Bin_result['price'] = binance_price
#     str_Bin_result = json.dumps(Bin_result)
#     json_Bin_result = json.loads(str_Bin_result)
#     pandas_Bin_result = json_normalize(json_Bin_result)
#     return pandas_Bin_result


url = "https://api.binance.com"
res = requests.get(url + "/api/v3/ticker/price", params={'symbol': "BTCUSDT"})
Bin_result = res.json()
#print(type(Bin_result))
#print(Bin_result[0]['price'])
#print(Bin_result[0]['symbol'])
#print("--------------------여기는 Bin_result의 값입니다--------------------")
#print(type(Bin_result['price']))
# Bin_result['price']는 string이므로 float 변환
binance_price = float(Bin_result['price'])
Bin_result['price'] = binance_price
str_Bin_result = json.dumps(Bin_result)
json_Bin_result = json.loads(str_Bin_result)
pandas_Bin_result = json_normalize(json_Bin_result)




   


# 1. 열 추가 방법
    # 1-1. 방법1
    # city = ['32424']
    # pandas_Bin_result['city'] = city
# 1-2. 방법2
# df = df.assign(city = ['Lahore'])
#print(df)

#210406
#데이터 순서(symbol,price)
#변수명 변경 완료
#데이터 불러오기 완료
#함수로 변환하는 작업 필요