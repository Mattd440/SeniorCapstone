from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import  Product
from .ShoppingCart import ShoppingCart
from .forms import CartAddProductForm

@require_POST
def addToCart(request, product_id):
    cart = ShoppingCart(request)  # create a new cart object passing it the request object
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = ShoppingCart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.removeProduct(product)
    return redirect('cart:cart_detail')


def cartDetail(request):
    cart = ShoppingCart(request)
    # for item in cart:
    #     item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})

# @require_POST
# def addToCart(request, product_id):
#     cart = ShoppingCart(request)
#     print(type(cart), "CART TYPEPEPEPEPEPE")
#     product = Product.objects.get(id=product_id)
#     form = CartAddProductForm(request.POST)
#
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
#     return redirect('cart:cart_detail')
#
# #
# # def removeFromCart(request, product_id):
# #     cart= ShoppingCart(request)
# #     product = get_object_or_404(Product, id=product_id)
# #     cart.removeProduct(product)
# #     return redirect('cart:cart_detail')
# #
# def cartDetail(request):
#     cart= ShoppingCart(request)
#     for item in cart:
#         item['quantity_update_form'] = CartAddProductForm(initial={
#         'quantity':item['quantity'], 'update': True})
#     return render(request, 'cart/detail.html')
#     #return render(request, 'cart/detail.html', {'cart': cart})