from django.shortcuts import render

# Create your views here.

def ProductTypes(request):
    return render(request, 'products/product_type.html')

def ProductList(request, product_type):
    return render(request, 'products/product_list.html', {'type': product_type})

def ProductDetail(request, product_id):
    return render(request, 'products/product_detail.html', {'id':product_id})