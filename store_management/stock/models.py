from django.db import models
from product.models import Product, ProductCategory
from django.urls import reverse

class Stock(models.Model):
    id = models.AutoField(primary_key = True)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-product_category',)

    def __str__(self):
        return self.product_category


