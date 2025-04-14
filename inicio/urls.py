from django.urls import path
from inicio.views import inicio, crear_vela, listado_de_velas

urlpatterns = [

    path('', inicio, name='inicio'),
    path('velas/crear', crear_vela, name='crear_vela'),
    path('velas/', listado_de_velas, name='listado_de_velas'),

]