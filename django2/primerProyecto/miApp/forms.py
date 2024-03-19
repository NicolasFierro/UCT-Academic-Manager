# forms.py

from django import forms
from .models import Estudiante, Profesor, Materia, Carrera

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['codigo', 'nombre', 'apellido', 'email', 'telefono', 'fecha_nacimiento', 'foto', 'carrera']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['codigo', 'nombre', 'apellido', 'email', 'telefono', 'foto', 'fecha_nacimiento', 'materias']

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['codigo', 'nombre', 'descripcion', 'creditos', 'carrera']

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['codigo', 'nombre', 'duracion']
