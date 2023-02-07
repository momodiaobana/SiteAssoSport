"""siteAsso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from appAsso.views import index, userLogin, signup, base, foot, basket, boxe, deleteItem, add, edit
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from . import settings

urlpatterns = [
    path('', index, name='index'),
    path('', base, name='base'),
    path('add/', add, name='add'),
    path('userLogin/', userLogin, name='userLogin'),
    path('signup/', signup, name='signup'),
    path('basket/', basket, name='basket'),
    path('foot/', foot, name='foot'),
    path('boxe/', boxe, name='boxe'),
    path('admin/', admin.site.urls),
    path('edit/<int:id>/', edit, name='edit'),
    path('deleteItem/<int:id>/', deleteItem, name = 'deleteItem'), 
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
