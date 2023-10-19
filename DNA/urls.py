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
from DNA.views import ColdDApi

router = routers.DefaultRouter()
router.register(r'api/cold', ColdDApi)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('HotDrinks/', views.hot_list),
    path('ColdDrinks/', views.cold_list),
    path('Desserts/', views.dessert_list),
    path('Snacks/', views.snack_list), 
    path('HotDrinks/<int:id>', views.hot_detail),
    path('ColdDrinks/<int:id>', views.cold_detail),
    path('Desserts/<int:id>', views.dessert_detail),
    path('Snacks/<int:id>', views.snacks_detail),
    path('', include(router.urls)),
]






