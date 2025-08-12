
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('GHAZIKHANI/', admin.site.urls),
    path('', include('home.urls')),
    path('account/', include('account.urls')),
    path('product/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('blog', include('blog.urls')),
    path('services', include('services.urls'))
]

