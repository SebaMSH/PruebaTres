from django.urls import path
from .views import index , dulce, salada, mixta, contacto, nosotros, sismos, home,lista_proveedores


urlpatterns = [
    path('', index, name="index"),
    path('dulce', dulce, name="dulce"),
    path('salada', salada, name="salada"),
    path('mixta', mixta, name="mixta"),
    path('contacto', contacto, name="contacto"),
    path('lista_proveedores', lista_proveedores, name="lista_proveedores"),
    path('nosotros', nosotros, name="nosotros"),
    path('sismos', sismos, name="sismos"),
    path('home', home, name="home"),
]