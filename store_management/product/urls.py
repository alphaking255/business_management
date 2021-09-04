from django.urls import path, include
from django.views.generic import TemplateView
from product.views import CategoryCreateView, CategoryDeleteView, CategoryListView, CategoryUpdateView, ProductCreateView, ProductList
from . import views


urlpatterns = [
    path('add_product', ProductCreateView.as_view(), name='add_product'),
    path('products', ProductList.as_view(), name='products'),
    path('categories', CategoryListView.as_view(), name='categories'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category'),
    path('category/add', CategoryCreateView.as_view(), name='add_category'),
    path('category/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete', CategoryDeleteView.as_view(), name='category-delete'),
]
