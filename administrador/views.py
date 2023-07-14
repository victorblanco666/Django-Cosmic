from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Guitar.models import Usuario
# Create your views here.


def indexadmin(request):
    if not request.user.is_staff:  
        return render(request, 'error.html')
    usuarios = Usuario.objects.all()
    context={'usuarios':usuarios}
    return render(request, '../templates/indexadmin.html', context)

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def agregarUsuario(request):
    if request.method == 'POST':
        username=request.POST["username"]
        password=request.POST["password"]
        admin=request.POST.get('admin') in ['True', 'true', '1']
        
        # Crear el usuario
        user = User(username=username, password=make_password(password), is_staff=admin, is_superuser=admin)
        user.save()

        context={'mensaje':'OK, datos guardados con éxito'}
        return render(request,'../templates/agregarUsuario.html',context)
    else:
        usu=Usuario.objects.all()
        context={'usu':usu}
        return render(request,'../templates/agregarUsuario.html',context)
def encontrarUsuario(request, pk):
    usuario = Usuario.objects.get(id_usuario=pk)
    if usuario:
        context = {'usuario': usuario}
        return render(request, '../templates/modificarUsuario.html', context)
    else:
        context = {'mensaje': 'Error, id usuario no existe'}
        return render(request, '../templates/indexadmin.html', context)

def modificarUsuario(request):
    if request.method == 'POST':
        idUsuario = request.POST["idUsuario"]
        n_usuario = request.POST["nombreUsuario"]
        contra = request.POST["contraseña"]

        usuario = Usuario.objects.get(id_usuario=idUsuario)
        usuario.usuario = n_usuario
        usuario.contraseña = contra
        usuario.save()

        return redirect('administrador')  # Redirige al usuario a la vista 'administrador'
    else:
        usuarios = Usuario.objects.all()
        context = {'usuarios': usuarios}
        return render(request, '../templates/indexadmin.html', context)






def eliminarUsuario(request,pk):
    context={}
    try:
        usuario=Usuario.objects.get(id_usuario=pk)
        usuario.delete()
        usuario="Ok, Datos eliminados satisfactoriamente"
        usuarios=Usuario.objects.all()
        context={'usuarios':usuarios,'mensaje':mensaje}
        return render(request,'../templates/indexadmin.html',context)
    except:
        mensaje="Error, id usuario no existe"
        usuarios=Usuario.objects.all()
        context={'usuarios':usuarios,'mensaje':mensaje}
        return render(request,'../templates/indexadmin.html',context)



