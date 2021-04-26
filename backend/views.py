# from django.shortcuts import render
# from rest_framework import viewsets
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import arbitrage
from . import news
from .main import star_coin
from .main.view_table import standard
from .member import login, mypage, register


# http 메소드로 들어오는 get,post 방식에 따라 응답하는 것을 만들거다
@api_view(['GET'])
def get_all_coin_info(request):
    user_id = request.GET.get('user_id')
    # user_id를 기반으로 DB로부터 STANDARD_MARKET 받아와야 한다
    # STANDARD_MARKET = MongoDbManager().get_standard_market({'user_id':user_id})
    # TARGET_MARKET도 마찬가지다
    # TARGET_MARKET = MongoDbManager().get_target_market({'user_id':user_id})
    STANDARD_MARKET = "upbit"
    TARGET_MARKET = ["binance"]
    coins = arbitrage.get_coins_lst(STANDARD_MARKET)
    data = arbitrage.get_all_coin_info(coins, STANDARD_MARKET, TARGET_MARKET)
    return Response(data)
    # return Response()


@api_view(['GET'])
def get_news_info(request):
    data = news.get_news()
    return Response(data)


@api_view(['POST'])
def update_standard(request):
    user_id = request.POST['user_id']
    standard_market = request.POST['standard_market']
    standard.update_standard(user_id, standard_market)


@api_view(['POST'])
def update_star_coin(request):
    user_id = request.POST['user_id']
    star_coin = request.POST['star_coin']
    status = request.POST['status']
    star_coin.update_star_coin(user_id, star_coin, status)


@api_view(['POST'])
def update_star_market(request):
    user_id = request.POST['user_id']
    star_market = request.POST['star_market']
    status = request.POST['status']
    star_coin.update_star_market(user_id, star_market, status)


@api_view(['GET'])
def get_login(request):
    user_id = request.GET.get('user_id')  # 이거 view에서 넘겨받아야 한다
    user_pw = request.GET.get('user_pw')
    status = login.get_login(user_id, user_pw)  # 200 성공, 400 비번틀림, 404 회원정보 없음
    if status == 200:
        return Response(status=200)
    elif status == 400:
        return Response(status=400)
    else:
        return Response(status=404)


@api_view(['POST'])
def create_user(request):
    request = json.loads(request.body)["user"]
    user_id = request['user_id']
    user_pw = request['user_pw']
    email = request['email']
    name = request['name']
    status = register.create_user(user_id, user_pw, email, name)
    if status == 200:
        return Response(status=200)
    else:
        return Response(status=400)


@api_view(['GET'])
def get_mypage(request):
    user_id = request.GET.get('user_id')
    data = mypage.get_mypage(user_id)
    return Response(data)
