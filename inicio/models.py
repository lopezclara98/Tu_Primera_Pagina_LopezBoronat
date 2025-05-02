from django.db import models
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
# Create your models here.
class Vela(models.Model):
    """
    Modelo para representar una vela.
    """
    nombre = models.CharField(max_length=100)
    aroma = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateField(null=True)
    imagen = models.ImageField(upload_to='velas/', null=True, blank=True)  # Campo de imagen para la vela

    def __str__(self):
        return f"{self.nombre} - {self.aroma} - {self.color} - ${self.precio} - {self.fecha_creacion}- {self.imagen}"
    

