from django.shortcuts import render,redirect
from .models import Proveedores

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def dulce(request):
    return render(request, 'core/dulce.html')

def salada(request):
    return render(request, 'core/salada.html')

def mixta(request):
    return render(request, 'core/mixta.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def sismos(request):
    return render(request, 'core/sismos.html')

def home(request):
    return redirect(to="index")

def listar_proveedores(request):
    proveedores = Proveedores.objects.all()
    datos = {
        "proveedores" : proveedores
    }
    return render(request, 'core/listar_proveedores.html', datos)