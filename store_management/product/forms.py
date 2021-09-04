from django import forms
from .models import Product, ProductCategory


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name']

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','product_category']

