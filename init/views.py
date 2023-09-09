from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    # Vista para la página de inicio
    return render(request, 'home.html')

def contact(request):
    # Vista para la página de contacto
    return render(request, 'contact.html')

def about(request):
    # Vista para la página de acerca de mi
    return render(request, 'about.html')

