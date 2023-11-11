"""
URL configuration for DNA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import router
from django.urls import include, path, re_path
from rest_framework import routers

from DNA import views
from DNA.views import UserApi, BasketApi, MenuApi
from DNA.views import home
from DNA.views import menu, register, user_detail, user_list




router = routers.DefaultRouter()
router.register(r'api/user', UserApi)
router.register(r'api/basket', BasketApi)
router.register(r'api/menu', MenuApi)


urlpatterns = [
    # path('api/v1/drf-auth/',include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('menu/', menu),
    path('register/', register),
    path('', home),
    path('users/<int:id>/', user_detail, name='user_detail'),
    path('users/', user_list, name='user_list'),
]







