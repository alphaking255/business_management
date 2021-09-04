from django.urls import path, include
from django.views.generic import TemplateView
from product.views import CategoryCreateView, CategoryListView, ProductCreateView, ProductList
from . import views


urlpatterns = [
    path('add_product', ProductCreateView.as_view(), name='add_product'),
    path('products', ProductList.as_view(), name='products'),
    path('add_category', CategoryCreateView.as_view(), name='add_category'),
    path('categories', CategoryListView.as_view(), name='categories'),
]
