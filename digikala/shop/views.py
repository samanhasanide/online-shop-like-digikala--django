from django.shortcuts import render, redirect
from .import models
from django.contrib.auth import authenticate, login, logout
from cart.cart import CartBasket
from django.contrib.auth.decorators import login_required
from decimal import Decimal


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
        return render(request, 'shop/index.html', {'products': products, "category": category})
    except:
        return redirect('home')


def category_summary(request):
    all_categories = models.Category.objects.all()
    return render(request, 'shop/category_summary.html', {'categories': all_categories})


@login_required
def checkout(request):

    cart = CartBasket(request)

    products = cart.get_prods()
    quantities = cart.get_quants()

    if not products.exists():
        return redirect('home')

    try:
        customer = models.Customer.objects.get(user=request.user)
    except models.Customer.DoesNotExist:
        return redirect('profile')

    addresses = customer.addresses.all()

    cart_items = []
    total_price = Decimal('0.00')

    for product in products:

        quantity = quantities.get(str(product.id), 0)

        if product.is_sale and product.sale_price > 0:
            price = product.sale_price
        else:
            price = product.price

        subtotal = price * quantity
        total_price += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'price': price,
            'subtotal': subtotal,
        })

    context = {
        'addresses': addresses,
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'shop/checkout.html', context)
