from django.contrib import admin
from django.urls import path, include
from appAsso.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from . import settings
from rest_framework import routers

#Router est une classe qui va permettre de rendre des vues génériques 
router = routers.SimpleRouter()
router.register('product', ProductsViewset, basename='product')


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

    ##### API #####
    path('api-auth/', include('rest_framework.urls')), 
   # path('api/product', ProductsAPIView.as_view()), endpoint get 
    path('', include(router.urls))


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

