from django.urls import path
from . import views



app_name='product'
urlpatterns = [
    path('category/<str:search>', views.category_detail, name='category_detail'),
    path('products_detail/<str:search>', views.product, name='products_detail'),
    path('pricelist', views.prices_list, name='price_list'),
    path('none', views.none, name='none'),
]