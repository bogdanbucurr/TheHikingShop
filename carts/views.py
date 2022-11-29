from django.shortcuts import render, redirect

from carts.models import Cart, CartItem
from store.models import Product


def _cart_id(request):
    cart1 = request.session.session_key   # I named this cart cart1 because I don t want to get confused with func cart
    if not cart1:
        cart1 = request.session.create()
    return cart1


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)  # get the product
    try:
        cart1 = Cart.objects.get(cart_id=_cart_id(request))  # get the cart using the cart_id present in the session
    except Cart.DoesNotExist:
        cart1 = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart1.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1  # cart_item.quantity = cart_item.quantity + 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()
    return redirect('cart')


def cart(request):
    return render(request, 'store/cart.html')
