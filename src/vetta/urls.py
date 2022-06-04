from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),

    path('api/v1/auth/', include('proman_phone_login.urls')),
    path('api/v1/products/', include('products.api.urls'))
]
