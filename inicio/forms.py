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

    class Meta:
        model = Vela
        fields = ['nombre', 'aroma', 'color', 'precio']