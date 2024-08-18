from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    userInfo = request.user
    
    context = {'userInfo': userInfo}
    return render(request, 'home.html', context)

#
# AREA PERSONAL
#
@login_required(login_url='login')
def areaPersonal(request):
    context = {}
    return render(request, 'area_personal.html', context)

#
# ACADEMIA
#
def academia(request):
    context = {}
    return render(request, 'academia.html', context)

@login_required(login_url='login')
def academiaMB(request):
    context = {}
    return render(request, 'academia_mb.html', context)

@login_required(login_url='login')
def academiaSB(request):
    context = {}
    return render(request, 'academia_sb.html', context)


#
# SERVICIOS
#
def servicios(request):
    context = {}
    return render(request, 'servicios.html', context)

@login_required(login_url='login')
def serviciosMB(request):
    context = {}
    return render(request, 'servicio_mb.html', context)

@login_required(login_url='login')
def serviciosSB(request):
    context = {}
    return render(request, 'servicio_sb.html', context)


#
# USUARIO
#
def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.object.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username OR password is incorrect")
        
    context = {'page': page}

    return render(request, 'login_registro.html', context)

def registerPage(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)          #  Not commit yet, first filter/normalise the data
            user.username = user.username.lower()   #  Normalise the data
            #  Add more filtration (eg. check the username doesn't exist yet, ...)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration.')

    context= {'page':  page, 'form': form}
    return render(request, 'login_registro.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')