from django.urls import path
from dash import views


urlpatterns = [
    path('', views.RegistratiobView.as_view(), name='register')
]