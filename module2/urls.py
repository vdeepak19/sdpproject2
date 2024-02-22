# url_shortener/urls.py
from django.urls import path
from .views import url_shortener, redirect_to_original

urlpatterns = [
    path('', url_shortener, name='url_shortener'),
    path('<str:short_url>/', redirect_to_original, name='redirect_to_original'),
]
