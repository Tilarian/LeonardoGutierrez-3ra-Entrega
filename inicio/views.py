from django.shortcuts import render, redirect

from inicio.models import Usuario

from inicio.forms import CrearFormulario

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
    
    if request.method == 'POST':
        formulario = CrearFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            usuario = Usuario(nombre=datos.get('nombre'), apellido=datos.get('apellido'), correo=datos.get('correo'), sugerencia=datos.get('sugerencia'))
            usuario.save()
            return redirect('usuarios')
        
    formulario = CrearFormulario()
    return render(request, 'inicio/crear_usuario_v2.html', {'formulario': formulario})

def usuarios(request):
    
    usuarios = Usuario.objects.all()
    
    return render(request,'inicio/usuarios.html', {'usuarios': usuarios})