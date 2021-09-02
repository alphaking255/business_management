from django.shortcuts import render
from django.shortcuts import get_object_or_404
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
from .forms import AddForm

from .models import ProductCategory, Product
from .serializers import ProductSerializer, ProductCategorySerializer


#Product views
class ProductList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product/products.html'
    serializer_class = ProductSerializer(many=True), ProductCategorySerializer(many=True)

    def get(self, request):

        products = Product.objects.values()
        
        # categories_to_product = ProductCategory.objects.annotate(num_products=Count('name'))
        
        # category = [cat for cat in categories_to_product]
        # print('===cattttt===')
        # print(category)
        # product_in_category = Product.objects.filter(product_category__name=category)

        # for category in categories_to_product:
        #     category_item = category
        #     print("  category   ")
        #     print(category_item)
            
        #     product_in_category = Product.objects.filter(product_category__name=category)
        #     for product in product_in_category:
        #         product_item = product
        #         print("=====product_item====")
        #         print(product_item)

        #     print("Count")
        #     print(category.num_products)
        

        my_dict={
            'products':products,
            # 'categories':category_item
            }
        print("My dict========")
        print(my_dict)
        return Response(my_dict)



       

    # def count(self, request):
       

    #     return Response({'counts':result})


#Add product
class ProductCreateView(CreateView):
    model = Product
    form_class = AddForm
    template_name = 'product/product_create.html'

