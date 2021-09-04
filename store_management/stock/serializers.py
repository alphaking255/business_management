from rest_framework import serializers
from .models import Stock
from django.db.models import fields


#sales Serializer
class StockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


