from django.shortcuts import render
from products.models import Product, ProductCategory

def index(request):
    context = {
        'title': 'Store',        }
    return  render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(), 
    }
    return render(request, 'products/products.html', context)

def home(request):
    categories = ProductCategory.objects.all()

    categories_with_products = []
    for category in categories:
        products = category.products.all()[:3]  
        categories_with_products.append({
            'category': category,
            'products': products
        })
    
    context = {
        'categories_with_products': categories_with_products
    }
    return render(request, 'products/index.html', context)

