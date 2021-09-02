from django.db import models
from product.models import Product, ProductCategory
from decimal import Decimal
from django.db.models import F, Sum
from django.urls import reverse

class Sales(models.Model):
    id = models.AutoField(primary_key = True)
    product_sold = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    # total_price = models.IntegerField()

    class Meta:
        ordering = ('-product_sold',)

    def __str__(self):
        return self.product_sold

    def get_absolute_url(self):
        return reverse('sales')


class Purchases(models.Model):
    id = models.AutoField(primary_key = True)
    product_name = models.CharField(max_length=50)
    amount = models.IntegerField(default = 0)
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return '%s, %s' (self.product_name, self.amount)