from .forms import AddSale
from transaction.models import Sales, Purchases
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework.renderers import TemplateHTMLRenderer

from transaction.serializers import SalesSerializers, PurchasesSerializers

#Sales List
class SalesList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'transaction/sales.html'
    serializer_class = SalesSerializers

    def get(self, request):
        queryset = Sales.objects.all()
        return Response({'sales': queryset})

    

class SalesDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'transaction/sale_detail.html'
    serializer_class = SalesSerializers

    def get(self, request, pk):
        sale = get_object_or_404(Sales, pk=pk)
        serializer = SalesSerializers(sale)
        return Response({'serializer': serializer, 'sale': sale})

    def post(self, request, pk):
        sale = get_object_or_404(Sales, pk=pk)
        serializer = SalesSerializers(sale, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'sale': sale})
        serializer.save()
        return redirect('sales')

class SaleCreateView(CreateView):
    model = Sales
    form_class = AddSale
    # fields = ['product_sold','price','quantity']
    template_name = 'transaction/sale_create.html'
    

class SaleUpdateView(UpdateView):
    model = Sales
    fields = ['product_sold','price','quantity']
    template_name = 'transaction/sales.html'


class SaleDeleteView(DeleteView):
    model = Sales
    success_url = 'transaction:delete-sales'


#Purchases Views
# class PurchasesViewSet(viewsets.ViewSet):
#     def list(self, request):
        
#         serializer = PurchasesSerializers(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Purchases.objects.all()
#         purchases = get_object_or_404(queryset, pk=pk)
#         serializer = PurchasesSerializers(purchases)
#         return Response(serializer.data)