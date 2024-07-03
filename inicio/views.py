from django.shortcuts import render, redirect

from inicio.models import Usuario

from inicio.forms import CrearFormulario, BuscarUsuario, EditarFormulario

import random

def inicio(request):
   # return HttpResponse('Bienvenidos!!')
   return render (request, 'inicio/index.html')

def probando (request):
    
    lista = list(range(500))
    
    numeros = random.choices(lista, k=50)
    print(numeros)
    return render(request, 'probando_if_for.html', {'numeros': numeros})

def crear_usuario_v2(request):
    print('valor de la request:', request)
    print('valor de GET:', request.GET)
    print('valor de POST:', request.POST)
    
    formulario = CrearFormulario()
    
    if request.method == 'POST':
        formulario = CrearFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            usuario = Usuario(nombre=datos.get('nombre'), apellido=datos.get('apellido'), correo=datos.get('correo'), sugerencia=datos.get('sugerencia'))
            usuario.save()
            return redirect('usuarios')
        
    return render(request, 'inicio/crear_usuario_v2.html', {'formulario': formulario})

def usuarios(request):
    
    formulario = BuscarUsuario(request.GET)
    if formulario.is_valid():
        nombre = formulario.cleaned_data['nombre']
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
    
    # usuarios = Usuario.objects.all()
    
    return render(request,'inicio/usuarios.html', {'usuarios': usuarios, 'formulario': formulario})

def eliminar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    
    return redirect('usuarios')

def editar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    
    formulario = EditarFormulario(initial={'nombre': usuario.nombre, 'apellido' :usuario.apellido, 'correo' :usuario.correo, 'sugerencia' :usuario.sugerencia})
    
    if request.method == 'POST':
        formulario = EditarFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            usuario.nombre = info['nombre']
            usuario.apellido = info['apellido']
            usuario.correo = info['correo']
            usuario.sugerencia = info['sugerencia']
            usuario.save()
            return redirect('usuarios')
        
    return render(request, 'inicio/editar_usuario.html', {'formulario': formulario, 'usuario': usuario})

def ver_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, 'inicio/ver_usuario.html', {'usuario': usuario})