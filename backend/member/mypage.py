import json

from ..djongoManager import *


def get_mypage(user_id):
    # request.GET 하면은 QueryDict 형태로 받아진다 {'user_id':'jeongsun'}
    # login 페이지에서 쓰는 get_user_info 혹은 get_user_info_id 쓰면 됨
    dbUserData = get_user_info({'user_id':user_id}) # _id, user_id, user_pw, name, email 이렇게 온다고 가정하자
    # del dbUserData['_id']
    # del dbUserData['user_pw']
    return json.dumps(dbUserData) # user_id, name, email 의 딕셔너리가 json으로 변환되어 전달 될 것