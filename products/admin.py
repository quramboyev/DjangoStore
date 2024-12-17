from django.contrib import admin

from products.models import ProductCategory, Product, hiha

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(hiha)