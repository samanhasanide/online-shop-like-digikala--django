from django.shortcuts import render, redirect
from .import models
from django.contrib.auth import authenticate, login, logout


def homepage(request):
    all_products = models.Product.objects.all()
    return render(request, 'shop/index.html', {'products': all_products})


def product_pages(request, pk):
    product = models.Product.objects.get(id=pk)
    return render(request, 'shop/product.html', {'product': product})


def category_page(request, cat):
    cat = cat.replace('-', ' ')
    try:
        category = models.Category.objects.get(name=cat)
        products = models.Product.objects.filter(category=category)
        return render(request, 'shop/index.html', {'product': products}, {"category": category})
    except:
        return redirect('home')
