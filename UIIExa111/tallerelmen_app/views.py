from django.shortcuts import render
from .models import Clientes
# Create your views here.

def inicio_vista(request):
    # Obtener todos los registros de la tabla Materia
    Listadoclientes = Clientes.objects.all()
    return render (request, 'gestionarClientes.html',{"Losclientes":Listadoclientes})
