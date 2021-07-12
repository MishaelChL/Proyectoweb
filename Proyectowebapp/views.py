from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "Proyectowebapp/home.html")

def servicios(request):
    return render(request, "Proyectowebapp/servicios.html")

def tienda(request):
    return render(request, "Proyectowebapp/tienda.html")

def blog(request):
    return render(request, "Proyectowebapp/blog.html")

def contacto(request):
    return render(request, "Proyectowebapp/contacto.html")