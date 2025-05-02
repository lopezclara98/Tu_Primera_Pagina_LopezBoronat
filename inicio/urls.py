from django.urls import path
from inicio.views import inicio, crear_vela, listado_de_velas, detalle_vela, VistaEditarVela, VistaEliminarVela

urlpatterns = [

    path('', inicio, name='inicio'),
    path('velas/crear', crear_vela, name='crear_vela'),
    path('velas/', listado_de_velas, name='listado_de_velas'),
    path('velas/<int:pk>/',detalle_vela , name='detalle_vela'),  
    path('velas/editar/<int:pk>/', VistaEditarVela.as_view(), name='editar_vela' ), 
    path('velas/eliminar/<int:pk>/', VistaEliminarVela.as_view(), name='eliminar_vela' ), 


]