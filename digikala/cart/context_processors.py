from .cart import CartBasket


def cart(request):
    return {'cart': CartBasket(request)}
