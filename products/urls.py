from django.urls import path, re_path
from . import views

app_name = 'products'

urlpatterns = [
    re_path(r'^$', views.ProductTypes, name='products'),
    #re_path(r'^addtocart/$', views.AddToCart, name='addToCart'),
    re_path(r'(?P<product_type>[\D]+)/$', views.ProductList, name='productsList'),
    re_path(r'(?P<type>[\D]+)/(?P<product_id>[\d]+)/$', views.ProductDetail, name='productDetail'),



]