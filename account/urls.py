from django.urls import path
from . import views



app_name='account'
urlpatterns = [
    path('login', views.UserLogin.as_view(), name='login'),
    path('register', views.UserRegister.as_view(), name='register'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('logout', views.logout_view, name='logout'),
    path('user', views.user_panel, name='user_panel')

]