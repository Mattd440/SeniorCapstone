from django.db import models

# Create your models here.
from django.conf import settings
from products.models import *
from decimal import Decimal



class ShoppingCart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = dict()

        self.cart = cart

    def addProduct(self, product, quantity=1, update_quantity=False):
        product_id = product.id

        if product_id not in self.cart :
            self.cart[product_id] = {'quantity': 0, 'price':str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] - quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.saveCart()

    def saveCart(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True


    def removeProduct(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.saveCart()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def getTotalPrice(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clearCart(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
