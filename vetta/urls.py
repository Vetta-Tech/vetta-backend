from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.generic import TemplateView


from users.views import FacebookLogin, GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),

    path('rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/',
         include('rest_auth.registration.urls')),
    path('api/v1/rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('api/v1/rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('api/login/', include('rest_social_auth.urls_token')),

    path('api/v1/auth/', include('proman_phone_login.urls')),
    path('api/v1/supplier/', include('supplier.api.urls')),
    path('api/v1/products/', include('products.api.urls')),
    path('api/v1/category/', include('category.api.urls')),
    path('api/v1/cart/', include('cart.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


if not settings.DEBUG:
    urlpatterns += [re_path(r'.*',
                            TemplateView.as_view(template_name='index.html'))]
