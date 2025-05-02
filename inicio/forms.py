from django import forms
from .models import Vela

class VelaForm(forms.ModelForm):
    """
    Formulario para crear una vela.
    """
    nombre = forms.CharField(max_length=100)
    aroma = forms.CharField(max_length=100)
    color = forms.CharField(max_length=50)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = forms.DateField( widget =forms.DateInput(attrs={'type': 'date'}))
    imagen = forms.ImageField(required=False)


    class Meta:
        model = Vela
        fields = ['nombre', 'aroma', 'color', 'precio', 'fecha_creacion', 'imagen']