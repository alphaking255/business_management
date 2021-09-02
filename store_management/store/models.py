from django.db import models
from product.models import Product

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_product_list(self):
        return Product.objects.filter(id=self)

    def get_total_products(self):
        total_products = Product.objects.filter(id=self)
        total = 0
        for item in total_products:
            total += item
        return total