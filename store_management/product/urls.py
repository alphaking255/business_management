from django.urls import path, include
from django.views.generic import TemplateView
from product.views import AddProductView, ProductList
from . import views


urlpatterns = [
    path('add_product', AddProductView.as_view(), name='add_product'),
    # path('products', views.products, name = 'products'),
    path('products', ProductList.as_view(), name='products'),
]
