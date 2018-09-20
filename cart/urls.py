from django.urls import re_path, path
from . import views

app_name = 'cart'


urlpatterns = [
    re_path(r'^$', views.cartDetail, name='cart_detail'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.addToCart, name='cart_add'),
    #re_path(r'^remove/(?P<product_id>\d+)/$', views.removeFromCart, name='cart_remove')
]