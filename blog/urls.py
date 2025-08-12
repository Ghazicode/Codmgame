from django.urls import path
from . import views



app_name='article'
urlpatterns = [
    path('', views.article, name='main'),
    path('/<str:search>', views.article_detail, name='article_detail'),
]