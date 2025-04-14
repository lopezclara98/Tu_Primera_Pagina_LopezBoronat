from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.forms import VelaForm
from inicio.models import Vela
# Create your views here.
def inicio(request):
    return render(request, 'inicio/inicio.html', {})

def crear_vela(request):

    if request.method == 'POST':
        formulario =VelaForm(request.POST)
        if formulario.is_valid():
            # Guardar la vela en la base de datos
            info=formulario.cleaned_data
            vela = Vela(nombre=info.get('nombre'), aroma=info.get('aroma'), color=info.get('color'), precio=info.get('precio'))
            vela.save()
            return redirect('listado_de_velas')  # Redirigir a la lista de velas después de crear una nueva vela
        else:
            return HttpResponse("Error al crear la vela")
    else:
        formulario = VelaForm() 

    return render(request, 'inicio/crear_vela.html', {'formulario': formulario})

def listado_de_velas(request):
    velas = Vela.objects.all()  # Obtener todas las velas de la base de datos
    return render(request, 'inicio/listado_de_velas.html', {'velas': velas})  # Pasar las velas al template  