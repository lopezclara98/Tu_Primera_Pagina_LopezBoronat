from django.db import models

# Create your models here.
class Vela(models.Model):
    """
    Modelo para representar una vela.
    """
    nombre = models.CharField(max_length=100)
    aroma = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - {self.aroma} - {self.color} - ${self.precio}"