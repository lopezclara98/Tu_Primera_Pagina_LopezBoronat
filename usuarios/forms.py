from django import forms    
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import InfoExtra

class FormularioRegistro(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {llave : '' for llave in fields}

class FormularioEdicionPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(required =False)
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required = False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar')
        help_texts = {llave : '' for llave in fields}

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class InfoExtraForm(forms.ModelForm):
    class Meta:
        model = InfoExtra
        fields = ['avatar', 'informacion_adicional']
