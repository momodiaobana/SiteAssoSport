from django.contrib import admin
from django.urls import path
from appAsso.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from . import settings



urlpatterns = [
    
    path('', index, name='index'),
    path('', base, name='base'),
    path('accueil/', accueil, name='accueil'),
    path('userLogin/', userLogin, name='userLogin'),
    path('signup/', signup, name='signup'),
    path('profil/', profil, name='profil'),
    path('updateProfil/', updateProfil, name='updateProfil'),
    path('add/', add, name='add'),
    path('basket/', pages, name='basket', kwargs={'categorie':'basket'}),
    path('foot/', pages, name='foot', kwargs={'categorie':'foot'}),
    path('boxe/', pages, name='boxe', kwargs={'categorie':'boxe'}),
    path('edit/<int:id>/', edit, name='edit'),
    path('deleteItem/<int:id>/', deleteItem, name = 'deleteItem'), 
    path('userLogout/', userLogout, name='userLogout'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

