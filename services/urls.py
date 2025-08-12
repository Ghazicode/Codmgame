from django.urls import path
from . import views



app_name='service'
urlpatterns = [
    path('', views.services, name='main'),
    path('/detail/<str:search>', views.service_detail, name='service_detail')
]