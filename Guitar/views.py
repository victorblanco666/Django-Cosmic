from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='/login/')
def indexadmin(request):
    if not request.user.is_staff:  # Si el usuario no es administrador, redirige a una página de error
        return render(request, 'error.html')
    usuarios = User.objects.all()
    return render(request, 'Guitar/indexadmin.html', {'usuarios': usuarios})

def index(request):
    context= {}
    return render(request,'Guitar/index.html',context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            django_login(request, user)
            return redirect('indexadmin')
        else:
            # Aquí puedes manejar el caso en que la autenticación falla
            pass
    return render(request, 'Guitar/login.html')

def register(request):
    context= {}
    return render(request,'Guitar/register.html',context)

def nivel1(request):
    context={}
    return render(request,'Guitar/nivel-1.html',context)

def nivel2(request):
    context={}
    return render(request,'Guitar/nivel-2.html',context)

def nivel3(request):
    context={}
    return render(request,'Guitar/nivel-3.html',context)
