from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from rest_framework import viewsets
from django.urls import reverse_lazy
from rest_framework.renderers import TemplateHTMLRenderer
from django.db.models import Count
from .forms import AddProductForm, AddCategoryForm

from .models import ProductCategory, Product
from .serializers import ProductSerializer, ProductCategorySerializer



#Add product
class ProductCreateView(CreateView):
    model = Product
    form_class = AddProductForm
    template_name = 'product/product_create.html'


#ProductList views

class ProductList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product/products.html'
    serializer_class = ProductSerializer(many=True)

    def get(self, request):

        products = Product.objects.values()
        

        my_dict={
            'products':products,
            }
        return Response(my_dict)


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'product/product_edit.html'
    form_class = AddProductForm
    success_url = reverse_lazy('product:products')


#Add Product Category
class CategoryCreateView(CreateView):
    model = ProductCategory
    form_class = AddCategoryForm
    template_name = 'product/category_create.html'


class CategoryListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product/category.html'
    serializer_class = ProductCategorySerializer(many=True)

    def get(self, request):
        categories = ProductCategory.objects.values()
        count = Product.objects.filter().count()

        return Response({
            'categories':categories,
            'counts':count
        })



class CategoryDetailView(DetailView):
    model = ProductCategory
    template_name = 'product/category.html'


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'product/category_edit.html'
    form_class = AddCategoryForm
    success_url  = reverse_lazy('categories')

    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(ProductCategory, category_id=id_)


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'product/category_delete.html'
    success_url = reverse_lazy('categories')