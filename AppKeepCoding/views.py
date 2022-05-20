from django.http import HttpResponse

from AppKeepCoding.models import Curso

def curso(self):

      curso = Curso(nombre = "Desarrollo web", camada = "19881")
      curso.save()
      documentoDeTexto = f"--->Curso:{curso.nombre}, Camada:{curso.camada}"
      return HttpResponse(documentoDeTexto)

from django.contrib import admin
from django.urls import path
from AppKeepCoding import curso
