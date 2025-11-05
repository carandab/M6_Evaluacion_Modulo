from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from .models import Tarea



def index(request):
    return render(request, 'index.html')

def lista_tareas(request):

    tarea = Tarea.objects.all().order_by('fecha_creacion')

    return render(request, 'tareas_lista')

def detalle_tarea(request):
    tarea = get_object_or_404(Tarea, pk=pk)
    return render(request, 'detalle_tarea.html', {'Tarea': tarea})

def agregar_tarea(request):
    return render(request, 'AgregarTarea.html')

def eliminar_tarea(request):
    return render(request, 'EliminarTarea.html')