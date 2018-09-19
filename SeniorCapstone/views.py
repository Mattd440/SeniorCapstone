from django.shortcuts import render

def HomePage(request):
    request.session['cart'] = ['product1', 'product2']
    return render(request, 'home_page.html')

def AboutPage(request):
    items = request.session['cart']
    return render(request, 'about_page.html', {'items': items})

def ContactPage(request):
    return render(request, 'contact_page.html')