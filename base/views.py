from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def prueba(request):
    return render(request, 'home.html', {})

#
# AREA PERSONAL
#
def areaPersonal(request):
    context = {}
    return render(request, 'base/area_personal.html', context)

#                                                                           /base/template/base/academia.html
# django.template.loaders.filesystem.Loader: C:\Users\Mateo\Desktop\mtbets\base\templates\base\academia.html (Source does not exist)
# ACADEMIA
#
def academia(request):
    context = {}
    return render(request, 'academia.html', context)

def academiaMB(request):
    context = {}
    return render(request, 'base/academia_mb.html', context)

def academiaSB(request):
    context = {}
    return render(request, 'base/academia_sb.html', context)


#
# SERVICIOS
#
def servicios(request):
    context = {}
    return render(request, 'base/servicios.html', context)

def serviciosMB(request):
    context = {}
    return render(request, 'base/servicio_mb.html', context)

def serviciosSB(request):
    context = {}
    return render(request, 'base/servicio_sb.html', context)


#
# USUARIO
#
def login(request):
    context = {}
    return render(request, 'base/login.html', context)

def register(request):
    context = {}
    return render(request, 'base/registro.html', context)