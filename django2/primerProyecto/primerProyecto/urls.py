from django.urls import path
from . import views

urlpatterns = [
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/agregar/', views.agregar_estudiante, name='agregar_estudiante'),
    path('estudiantes/<int:id>/', views.detalle_estudiante, name='detalle_estudiante'),
    path('estudiantes/<int:id>/editar/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/<int:id>/eliminar/', views.eliminar_estudiante, name='eliminar_estudiante'),
]


