from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def mostrar_datos(request):
    return HttpResponse("Mostrando Datos")