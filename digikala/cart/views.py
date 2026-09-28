from django.shortcuts import render, get_object_or_404, redirect
from .cart import CartBasket
from shop.models import Product
from django.http import JsonResponse


def cart_summary(request):

    cart = CartBasket(request)

    cart_products = cart.get_prods()
    quantities = cart.get_quants()

    cart_items = []
    cart_total = 0
    cart_quantity = 0

    for product in cart_products:

        quantity = int(
            quantities.get(str(product.id), 0)
        )

        subtotal = product.price * quantity

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

        cart_total += subtotal
        cart_quantity += quantity

    return render(
        request,
        'cart/cart_summary.html',
        {
            'cart_products': cart_products,
            'cart_items': cart_items,
            'cart_total': cart_total,
            'cart_quantity': cart_quantity,
        }
    )


def cart_add(request):

    if request.method != 'POST':
        return JsonResponse(
            {'error': 'Invalid request'},
            status=400
        )

    if request.POST.get('action') != 'post':
        return JsonResponse(
            {'error': 'Invalid action'},
            status=400
        )

    product_id = request.POST.get('product_id')
    product_qty = request.POST.get('product_qty')

    if not product_id or not product_qty:
        return JsonResponse(
            {'error': 'Product ID or quantity is missing'},
            status=400
        )

    try:

        product_id = int(product_id)
        product_qty = int(product_qty)

        if product_qty < 1:
            raise ValueError

    except (TypeError, ValueError):

        return JsonResponse(
            {'error': 'Invalid product or quantity'},
            status=400
        )

    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart = CartBasket(request)

    cart.add(
        product=product,
        quantity=product_qty
    )

    return JsonResponse({
        'qty': len(cart),
        'product_qty': cart.get_quants()[str(product.id)]
    })


def cart_delete(request):
    pass


def cart_update(request):

    if request.method != 'POST':
        return JsonResponse(
            {'error': 'Invalid request'},
            status=400
        )

    try:
        product_id = int(
            request.POST.get('product_id')
        )

        quantity = int(
            request.POST.get('quantity')
        )

        if quantity < 1:
            raise ValueError

    except (TypeError, ValueError):
        return JsonResponse(
            {'error': 'Invalid quantity'},
            status=400
        )

    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart = CartBasket(request)

    cart.update(
        product=product,
        quantity=quantity
    )

    return redirect('cart_summary')
