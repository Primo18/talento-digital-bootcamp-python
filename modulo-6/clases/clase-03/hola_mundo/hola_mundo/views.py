from django.shortcuts import render
from django.http import HttpResponse


def hola_mundo(request):
    return HttpResponse("<h1>Hola, mundo!</h1><p>Esto es una página de bienvenida.</p>")
