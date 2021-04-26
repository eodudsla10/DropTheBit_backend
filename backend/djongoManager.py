from django.core.exceptions import ObjectDoesNotExist

from .models import User, CoinName, UserFavorite
from .serializer import UserSerializer, CoinNameSerializer


def get_user_info(user_id, user_pw=None):
    try:
        if user_pw is not None:
            print('login')
            user = User.objects.get(user_id=user_id, user_pw=user_pw)
            return UserSerializer(user)
        else:
            user = User.objects.get(user_id=user_id)
            return UserSerializer(user)
    except ObjectDoesNotExist:
        return {}
        # return {'user_id': 'default', 'email': 'example.com', 'name': 'anonymous'}


def insert_user_info(user_id, user_pw, email, name):
    data = {
        'user_id': user_id,
        'user_pw': user_pw,
        'email': email,
        'name': name
    }
    user = User()
    query = UserSerializer(user, data=data)
    if query.is_valid():
        query.save()


def get_krw_coin_name(coin_name):
    try:
        res = CoinName.objects.get(coin_id=coin_name)
        ser = CoinNameSerializer(res)
        ret = ser.data["name_kr"]
    except ObjectDoesNotExist:
        ret = ""

    return ret


def get_eng_coin_name(coin_name):
    try:
        res = CoinName.objects.get(coin_id=coin_name)
        ser = CoinNameSerializer(res)
        ret = ser.data["name_en"]
    except ObjectDoesNotExist:
        ret = ""

    return ret


def get_standard_market(user_id):
    res = UserFavorite.objects.get(user_id=user_id)
    return res["standard"]


def get_target_market(user_id):
    res = UserFavorite.objects.get(user_id=user_id)
    return res["targets"]


def update_standard_market(user_id, standard_market):
    res = UserFavorite.objects.get(user_id=user_id)
    res["standard"] = standard_market
    res.save()
