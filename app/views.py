from django.shortcuts import render
from .models import *
from django.http import HttpResponse

from app.forms import *

# Create your views here.

def crearprincipal(request):
    principal = Principal(nombre="Bife de lomo con pure", vegano=0, cantidad_personas=2)
    principal.save()
    Cadena=f" plato creado: {principal.nombre}"
    return HttpResponse (Cadena)

def crearentrada(request):
    entrada = Entrada(nombre="Empanada de carne", vegano=0, cantidad_personas=1)
    entrada.save()
    Cadena=f" entrada creada: {entrada.nombre}"
    return HttpResponse (Cadena)

def crearpostre(request):
    postre = Postre(nombre="Ensalada de fruta", vegano=1, cantidad_personas=1)
    postre.save()
    Cadena=f" postre creada: {postre.nombre}"
    return HttpResponse (Cadena)

def principales(request):
    return render ( request, "app/principales.html")

def entradas(request):
    return render ( request, "app/entradas.html")

def postres(request):
    return render ( request, "app/postres.html")

def inicio(request):
    return render ( request, "app/inicio.html")

def entradaFormulario(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        vegano=request.POST["vegano"]
        cantidad_personas=request.POST["cantidad_personas"]
        entrada= Entrada(nombre=nombre, vegano=vegano, cantidad_personas=cantidad_personas)
        entrada.save()
        return render (request, "app/inicio.html" ,{"mensaje": "entrada guardada"})
    else:
        return render(request, "app/entradaFormulario.html" )#

def postreFormulario(request):
    if request.method=="POST":
        form= PostreForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            vegano= informacion["vegano"]
            cantidad_personas= informacion["cantidad_personas"]
            postre= Postre(nombre=nombre, vegano=vegano, cantidad_personas=cantidad_personas)
            postre.save()
            return render (request, "app/inicio.html" ,{"mensaje":"postre guardado correctamente"})
        else:
            return render (request, "app/postreFormulario.html", {"form": form, "mensaje": "Informacion no valida"})
    else:
        formulario= PostreForm()
        return render (request, "app/postreFormulario.html", {"form": formulario})



def principalFormulario(request):
    if request.method=="POST":
        form= PrincipalForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            vegano= informacion["vegano"]
            cantidad_personas= informacion["cantidad_personas"]
            principal= Principal(nombre=nombre, vegano=vegano, cantidad_personas=cantidad_personas)
            principal.save()
            return render (request, "app/inicio.html" ,{"mensaje":"postre guardado correctamente"})
        else:
            return render (request, "app/principalFormulario.html", {"form": form, "mensaje": "Informacion no valida"})
    else:
        formulario= PostreForm()
        return render (request, "app/principalFormulario.html", {"form": formulario})

def busquedaEntrada(request):
    return render(request, "app/busquedaEntrada.html")

def buscar(request):

    nombre= request.GET["nombre"]
    if nombre!="":
        entradas= Entrada.objects.filter(nombre=nombre)
        return render (request, "app/resultadosBusqueda.html", {"entradas":entradas})
    else:
        return render(request, "app/busquedaEntrada.html", {"mensaje":"Ingrese entrada"})
