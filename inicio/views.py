from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from inicio.forms import VelaForm
from inicio.models import Vela
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, 'inicio/inicio.html', {})

@login_required
def crear_vela(request):

    if request.method == 'POST':
        formulario = VelaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('listado_de_velas')
        else:
            return HttpResponse("Error al crear la vela")
    else:
        formulario = VelaForm() 

    return render(request, 'inicio/crear_vela.html', {'formulario': formulario})

def listado_de_velas(request):
    velas = Vela.objects.all()  # Obtener todas las velas de la base de datos
    return render(request, 'inicio/listado_de_velas.html', {'velas': velas})  # Pasar las velas al template  

def detalle_vela(request, pk):
    vela = get_object_or_404(Vela, pk=pk)  # Esto ya maneja el caso "no encontrada"
    return render(request, 'inicio/detalle_vela.html', {'vela': vela})

class VistaEditarVela(LoginRequiredMixin,UpdateView):
    model = Vela
    fields = ['nombre', 'aroma', 'color', 'precio', 'fecha_creacion', 'imagen']  
    template_name = 'inicio/editar_vela.html'
    success_url = reverse_lazy('listado_de_velas')  # Redirigir a la lista de velas después de editar una vela

class VistaEliminarVela(LoginRequiredMixin,DeleteView):
    model = Vela
    template_name = 'inicio/eliminar_vela.html'
    success_url = reverse_lazy('listado_de_velas')  # Redirigir a la lista de velas después de eliminar una vela



