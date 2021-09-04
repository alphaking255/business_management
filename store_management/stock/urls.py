from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from stock.views import StockCreateView, StockDeleteView, StockUpdateView, StockList
from django.contrib import admin


urlpatterns = [
    path('stock', StockList.as_view(), name='stock'),
    path('stock/add', StockCreateView.as_view(), name = 'add-stock'),
]