from django.db import models
from django.urls import reverse

class ProductCategory(models.Model):
    category_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=30)
    

    def __str__(self):
        return self.name

    


class Product(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    product_category = models.ForeignKey(ProductCategory, on_delete = models.CASCADE)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name