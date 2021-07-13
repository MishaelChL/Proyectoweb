from django.shortcuts import render, HttpResponse
from servicios.models import Servicio
# Create your views here.

def home(request):
    return render(request, "Proyectowebapp/home.html")

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "Proyectowebapp/servicios.html", {'servicios': servicios})

def tienda(request):
    return render(request, "Proyectowebapp/tienda.html")

def blog(request):
    return render(request, "Proyectowebapp/blog.html")

def contacto(request):
    return render(request, "Proyectowebapp/contacto.html")