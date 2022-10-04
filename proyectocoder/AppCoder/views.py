from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from AppCoder.models import Familiar

def mostrar_datos(request):

    template = loader.get_template("template1.html")

    familiar_1 = Familiar(nombre="Maria", edad="42", fecha_ingreso="2020-02-15")
    familiar_2 = Familiar(nombre="Juan", edad="10", fecha_ingreso="2022-02-01")
    familiar_3 = Familiar(nombre="Roberto", edad="25", fecha_ingreso="2010-05-05")

    dict_contexto = {"familiar1": familiar_1, "familiar2": familiar_2, "familiar3": familiar_3}
    respuesta = template.render(dict_contexto)
    
    return HttpResponse(respuesta)