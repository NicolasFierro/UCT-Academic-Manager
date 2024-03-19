from django.shortcuts import render, redirect
from .models import Estudiante, Profesor, Materia, Carrera
from .forms import EstudianteForm, ProfesorForm, MateriaForm, CarreraForm

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista_estudiantes.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    return render(request, 'detalle_estudiante.html', {'estudiante': estudiante})

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'agregar_estudiante.html', {'form': form})

def editar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'editar_estudiante.html', {'form': form})

def eliminar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('lista_estudiantes')
    return render(request, 'confirmar_eliminar_estudiante.html', {'estudiante': estudiante})

