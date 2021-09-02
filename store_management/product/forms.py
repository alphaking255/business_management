from django import forms
from .models import Product


class AddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','product_category']

