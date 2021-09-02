from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from transaction.views import SaleCreateView, SalesList, SalesDetail
from django.contrib import admin


urlpatterns = [
    path('sales', SalesList.as_view(), name='sales'),
    path('sales/<pk>/', SalesDetail.as_view(), name='sale-detail'),
    path('sales/add', SaleCreateView.as_view(), name = 'add-sales')
]