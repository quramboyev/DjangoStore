from django.db import models


class ProductCategory(models.Model):
    name =  models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class hiha(models.Model):
    sla = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f'Продукт: {self.name} | Категория {self.category.name}'


