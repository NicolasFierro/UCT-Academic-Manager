"""
URL configuration for primerProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from miApp import views
import miApp.views

urlpatterns = [
    path('admin/', admin.site.urls),  # para acceder al administrador de Django
    path('holaMundo/', views.holaMundo, name="Hola Mundo"), #Cuando se llama a esta vista se ejecutara la funcion holaMundo
    path('saludo/<int:redirigir>',views.saludo, name="Saludo"), 
    path('Inicio',views.index, name="Index"),
    path('presentacion/',views.presentacion, name="Presentacion"),
    # path('contacto/',miApp.views.contacto, name="Contacto"),
    # path('contacto/<str:nombre>',miApp.views.contacto, name="Contacto"),
    # path('contacto/<str:nombre>/<str:apellido>',miApp.views.contacto, name="Contacto"),
    path('quienesSomos/',views.quienesSomos, name="QuienesSomos"),
    path('productAndServices/',miApp.views.productAndServices, name="Productos  y Servicios"),
    path('contacto/',miApp.views.contacto, name="contacto"),
    path('', views.index, name='Inicio'),
    path('pagina/', miApp.views.pagina, name="Pagina"),
    path('crear_articulo/', miApp.views.crear_articulo, name="crear articulo"),
    path('crear_articulo/<str:title>/<str:content>/<str:public>',miApp.views.crear_articulo, name="crear articulo"),
    path('articulo/',miApp.views.articulo, name="Articulo"),
    path('editar_articulo/',miApp.views.editar_articulo, name="editar articulo"),
    path('articulos/',miApp.views.articulos, name="Listar"),
    path('borrar_articulos/<int:id>',miApp.views.borrar_articulo, name="borrar"),
    path('delete_articulox/<int:id>',miApp.views.delete_articulo, name="eliminar_sql"),
    path('update_articulo/<str:title>/<int:id>',miApp.views.update_articulo, name="actualizar_sql"),
    path('create_articulo/',miApp.views.create_articulo, name="create"),
    path('save_articulo/',miApp.views.save_articulo, name="save"),
    path('create_full_articulo/',miApp.views.create_full_articulo, name="create_full"),
]
