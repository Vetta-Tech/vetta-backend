from django.contrib import admin
from django.urls import path, include

from users.views import FacebookLogin, GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),

    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('api/login/', include('rest_social_auth.urls_token')),

    path('api/v1/auth/', include('proman_phone_login.urls')),
    path('api/v1/products/', include('products.api.urls'))
]
