from django.urls import path, re_path
from . import views

app_name = 'products'

urlpatterns = [
    re_path(r'^$', views.ProductTypes),
re_path(r'[\D]+/(?P<product_id>[\d]+)/$', views.ProductDetail),
    re_path(r'(?P<product_type>[\D]+)/$', views.ProductList),

]