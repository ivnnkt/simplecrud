from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('main.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    # для аутентификации по JSON Web Token
    path('auth/', include('djoser.urls.jwt')),
    # для аутентификации по базовому токену
    path('auth/', include('djoser.urls.authtoken')),
]

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]
