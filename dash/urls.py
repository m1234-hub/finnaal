from django.urls import path
from dash import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login.html/', views.login_page, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('pricing.html/', views.pricing, name='pricing'),
    path('stock-markets.html/', views.stockMarkets, name='stock-markets'),
    path('trading-view.html/', views.tradindViwe, name='trading-view'),
]



