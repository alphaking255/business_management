from rest_framework import viewsets, generics
from django.views.generic import ListView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .serializers import StockSerializer
from .models import Stock


class ListStockView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer