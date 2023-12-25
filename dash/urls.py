from django.urls import path
from dash import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login.html/', views.login_page, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('pricing', views.pricing, name='pricing'),
    path('basic-acc-mgt', views.base, name='basic-acc-mgt'),
    path('dash/stock-markets.html', views.stockMarkets, name='stock-markets'),
    path('dash/trading-view.html', views.tradindViwe, name='trading-view'),
]



