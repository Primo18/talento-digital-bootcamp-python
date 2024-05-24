from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def mascotas(request):
    return HttpResponse("<h1>Mascotas</h1><p>Esto es una página de mascotas.</p>")
