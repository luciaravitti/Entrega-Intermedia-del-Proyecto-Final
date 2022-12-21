from django.urls import path
from .views import *

urlpatterns = [
    
    path('crearprincipal/', crearprincipal, name="crearprincipal"),
    path('crearpostre/', crearpostre, name="crearpostre"),
    path('crearentrada/', crearentrada, name="crearentrada"),
    path('principales/', principales, name="principales"),
    path('entradas/', entradas, name="entradas"),
    path('postres/', postres, name="postres"),
    path('inicio/', inicio, name="inicio"),
    path('entradaFormulario/', entradaFormulario, name="entradaFormulario"),
    path('postreFormulario/', postreFormulario, name="postreFormulario"),
    path('principalFormulario/', principalFormulario, name="principalFormulario"),
    path('busquedaEntrada/', busquedaEntrada, name="busquedaEntrada"),
    path('buscar/', buscar, name="buscar"),



]