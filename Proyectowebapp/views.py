from django.shortcuts import render, HttpResponse
# Create your views here.

def home(request):
    return render(request, "Proyectowebapp/home.html")

def tienda(request):
    return render(request, "Proyectowebapp/tienda.html")

def contacto(request):
    return render(request, "Proyectowebapp/contacto.html")