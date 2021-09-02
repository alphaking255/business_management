from rest_framework import serializers
from .models import Sales, Purchases
from django.db.models import fields


#sales Serializer
class SalesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'


#Purchases Serializer
class PurchasesSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchases
        fields = '__all__'

