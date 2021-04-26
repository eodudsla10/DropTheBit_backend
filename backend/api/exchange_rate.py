from datetime import datetime

import requests


def Exchange_Rate():
    url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON"
    today = datetime.today().strftime("%Y%m%d")
    # 당일 몇시에 환율 api가 생성되는지 알아볼 필요 있다. 오전10시라고 하면 아래와 같이 수정
    # 자정부터 오전10시까지는 그 전날 환율을, 그 이후에는 당일 환율을 계산하도록 코드 수정
    querystring = {"authkey":"cVVI6zqyibj82ElHwc2TBv37RyNNF29C","searchdate":"20210412", "data":"AP01", "cur_unit":"USD"}
    res = requests.request("GET", url, params=querystring)
    dict_res = res.json()
    return dict_res[0]['deal_bas_r']