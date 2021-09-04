from .forms import AddStock
from stock.models import Stock
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework.renderers import TemplateHTMLRenderer

from stock.serializers import StockSerializers

#Sales List
class StockList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'stock/stock.html'
    serializer_class = StockSerializers

    def get(self, request):
        queryset = Stock.objects.all()
        return Response({'stock': queryset})


class StockCreateView(CreateView):
    model = Stock
    form_class = AddStock
    template_name = 'stock/add_stock.html'
    

class StockUpdateView(UpdateView):
    model = Stock
    form_class = AddStock
    template_name = 'stock/stock.html'


class StockDeleteView(DeleteView):
    model = Stock
    success_url = 'stock:delete-stock'
