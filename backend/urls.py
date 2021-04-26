from django.urls import path

from . import views

urlpatterns = [
    path('main/', views.get_all_coin_info, name="get_all_coin_info"),
    path('news/', views.get_news_info, name="get_news_info"),

    path('main/view_table/standard', views.update_standard, name="update_standard"),
    path('main/star_coin/', views.update_star_coin, name="update_star_coin"),
    path('main/star_market/', views.update_star_market, name="update_star_market"),

    path('member/login/', views.get_login, name="get_login"),
    path('member/register/', views.create_user, name="create_user"),
    path('member/mypage/', views.get_mypage, name="get_mypage"),
    #path('detail/<str:pk>/', views.memberDetail, name="detail"),
    #path('create/', views.memberCreate, name="create"),
    #path('update/<str:pk>/', views.memberUpdate, name="update"),
    #path('delete/<str:pk>/', views.memberDelete, name="delete")
] 
