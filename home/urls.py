from django.urls import path
from . import views



app_name='home'
urlpatterns = [
    path('', views.home, name='main'),
    path("terms", views.terms, name='terms'),
    path('about', views.about, name='about' )

]