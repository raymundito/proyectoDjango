from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import EmpleadoForm
from .forms import UsuarioForm
from .forms import RolForm

from .models import Empleado
from django.contrib import messages
from .models import Usuario
from .models import Rol

#funcion crear empleado
def crear(request):    
    nombre = request.POST['nombreInput']
    genero= request.POST['generoInput']
    edad = request.POST['edadInput']
    telefono = request.POST['telefonoInput']
    cargo = request.POST['cargoInput']
    email = request.POST['emailInput']
    direccion = request.POST['direccionInput']
    usuarioid = request.POST['usuarioIdInput']

    empleados = Empleado.objects.create(
       
        nombre=nombre, 
        genero=genero,
        edad=edad,
        telefono=telefono,
        cargo=cargo,
        email=email,
        direccion=direccion,
        usuarioid_id=usuarioid
        )
    messages.success(request, 'User: ' + nombre +' ¡Save Success !')
    return redirect('empleadoindex')

              


def editar(request, id):
    empleados =Empleado.objects.get(id=id)
    form =EmpleadoForm(instance=empleados)
    if request.method =='POST':
        form =EmpleadoForm(request.POST, instance=empleados)
        if form.is_valid():
            try:
                form.save()
                return redirect('/empleadoindex')
            except:
                pass
    context ={
        'empleado': empleados,
        'form':form
    }
    return render(request, 'editar.html', context)

#Funcion index empleado           


def empleadoindex(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleadoindex.html', {'empleados': empleados}) 

#Funciom eliminar empleado
def eliminar(request,id):
    empleados =Empleado.objects.get(id=id) #Se obtiene el id para eliminar el empleado
    empleados.delete()
    return redirect('/empleadoindex')

#Funcion layout
def layouts(request):
    return render(request, "layout.html")

#Funcion home
def home(request):
    return render(request, "home.html")





#Función crear usuario

def crearUsuario(request):    
    nombre = request.POST['nombreInput']
    contrasenia= request.POST['contraseniaInput']
    idrol_id = request.POST['idrolInput']

    usuarios = Usuario.objects.create(       
        nombre=nombre, 
        contrasenia=contrasenia,
        idrol_id=idrol_id,       
        )
    messages.success(request, 'User: ' + nombre +' ¡Save Success !')
    return redirect('usuarioindex')
#Funcion index del usuario
def usuarioindex(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarioindex.html', {'usuarios': usuarios}) 
#Funcion editar usuario
def editarUsuario(request, id):
    usuarios =Usuario.objects.get(id=id)
    form =UsuarioForm(instance=usuarios)
    if request.method =='POST':
        form =UsuarioForm(request.POST, instance=usuarios)
        if form.is_valid():
            try:
                form.save()
                return redirect('/usuarioindex')
            except:
                pass
    context ={
        'usuario': usuarios,
        'form':form
    }
    return render(request, 'editarUsuario.html', context)
#Funcion eliminar el usuario
def eliminarUsuario(request,id):
    usuarios =Usuario.objects.get(id=id)
    usuarios.delete()
    return redirect('/usuarioindex')       



#Funcion crear Roles
def crearRol(request):    
    tiporol = request.POST['tiporolInput']
    
    usuaroles = Rol.objects.create(       
        tiporol=tiporol,              
        )
    messages.success(request, 'User: ' + tiporol +' ¡Save Success !')
    return redirect('rolindex')
#Funcion index del rol
def rolindex(request):
    roles = Rol.objects.all()
    return render(request, 'rolindex.html', {'roles': roles}) 
#Funcion editar rol
def editarRol(request, id):
    roles =Rol.objects.get(id=id)
    form =RolForm(instance=roles)
    if request.method =='POST':
        form =RolForm(request.POST, instance=roles)
        if form.is_valid():
            try:
                form.save()
                return redirect('/rolindex')
            except:
                pass
    context ={
        'rol': roles,
        'form':form
    }
    return render(request, 'editarRol.html', context)
#Funcion eliminar rol
def eliminarRol(request,id):
    roles =Rol.objects.get(id=id)
    roles.delete()
    return redirect('/rolindex')   