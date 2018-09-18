from django.shortcuts import render

def HomePage(request):
    return render(request, 'home_page.html')

def AboutPage(request):
    return render(request, 'about_page.html')

def ContactPage(request):
    return render(request, 'contact_page.html')