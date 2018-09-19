from django.shortcuts import render
from django.http import Http404
from .models import ProductType , Product
# Create your views here.

def ProductTypes(request):
    #prodTypes = ['laptops', 'tablets', 'printers', 'accessories']
    try:
        prodTypes = ProductType.objects.all()
    except:
        raise Http404("Unable To Find Product Type")
    return render(request, 'products/product_type.html', {'productTypes': prodTypes})


def ProductList(request, product_type):
    try:
        type = ProductType.objects.get(name=product_type)
        products = Product.objects.all().filter(type=type.id)
    except:
        raise Http404("Unable To Find Product")

    return render(request, 'products/product_list.html', {'products': products, 'type':type })


def ProductDetail(request, type, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except:
        raise Http404("Unable To Find Product ")

    return render(request, 'products/product_detail.html', {'id':product_id, 'type':type})