from json import load
from re import template
from aiohttp import request
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Familiares
from django.template import loader
# Create your views here.


def mama(self):
    Mama = Familiares(nombre= "Monica", apellido = "Alvarez", edad ="62", FechaDeNacimiento ="26/01/1960")
    Mama.save(self)
    documentoDetexto = f"Nombre: {Mama.nombre}  Apellido:  {Mama.apellido}  Edad:  {Mama.edad}  Fecha de Nacimiento: {Mama.FechaDeNacimiento}" 
    dicc = {'Mama': Mama}
    template = loader.get_template('AppCoder/Mama.html')
    Documento = template.render(dicc)
    return HttpResponse(Documento)

def Hermano(self):
    Hermano = Familiares(nombre= "Lucas", apellido = "Prosdocimo", edad ="32", FechaDeNacimiento ="09/09/1989")
    Hermano.save(self)
    documentoDetexto = f"Nombre: {Hermano.nombre}  Apellido:  {Hermano.apellido}  Edad:  {Hermano.edad}  Fecha de Nacimiento: {Hermano.FechaDeNacimiento}" 
    dicc = {'Hermano': Hermano}
    template = loader.get_template('AppCoder/Hermano.html')
    Documento = template.render(dicc)
    return HttpResponse(Documento)

def Hermana(self):
    Hermana = Familiares(nombre= "Agustina", apellido = "Prosdocimo", edad ="29", FechaDeNacimiento ="06/03/1993")
    Hermana.save(self)
    documentoDetexto = f"Nombre: {Hermana.nombre}  Apellido:  {Hermana.apellido}  Edad:  {Hermana.edad}  Fecha de Nacimiento: {Hermana.FechaDeNacimiento}" 
    dicc = {'Hermana': Hermana}
    template = loader.get_template('AppCoder/Hermana.html')
    Documento = template.render(dicc)
    return HttpResponse(Documento)
