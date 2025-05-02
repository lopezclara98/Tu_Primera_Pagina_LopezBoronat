from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InfoExtra(models.Model):
    """
    Modelo para almacenar información adicional del usuario.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='infoextra')
    avatar = models.ImageField(upload_to='avatares', null = True, blank=True)
    informacion_adicional = models.CharField(max_length=100, blank=True, null=True)

    
