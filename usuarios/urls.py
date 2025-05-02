
from django.urls import path
from usuarios.views import login,registro, editar_perfil,visualizar_perfil
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/',login,name='login'),
    path('logout/',LogoutView.as_view(template_name ='usuarios/logout.html'),name='logout'),
    path('registro/',registro,name='registro'),
    path('editar/perfil/',editar_perfil,name='editar_perfil' ),
    path('perfil/', visualizar_perfil, name='visualizar_perfil')
]