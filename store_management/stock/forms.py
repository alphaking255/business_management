from django import forms
from .models import Stock


class AddStock(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product_category','product_name',]