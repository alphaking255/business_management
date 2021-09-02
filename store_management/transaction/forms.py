from django import forms
from .models import Sales


class AddSale(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['product_sold', 'price','quantity',]