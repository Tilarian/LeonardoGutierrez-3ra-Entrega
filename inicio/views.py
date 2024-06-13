from django.shortcuts import render, redirect
from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader

from inicio.models import Usuario

from inicio.forms import CrearFormulario

import random

def inicio(request):
   # return HttpResponse('Bienvenidos!!')
   return render (request, 'inicio/index.html')

def template1(request, nombre, apellido, edad):
    fecha = datetime.now()
    suma = 4 + edad
    
    return HttpResponse (f'<h1>Mi template1</h1> -- fecha: {fecha} -- Buenas {nombre} {apellido} {edad}')

def template2(request, nombre, apellido, edad):
    
    archivo_abierto = open(r'C:\Users\Tila\Desktop\Proyecto\templates\template2.html')
    # archivo_abierto = open('templates\template2.html')
    
    template = Template(archivo_abierto.read())
    
    archivo_abierto.close()
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha,
        'nombre': nombre,
        'apellido':apellido,
        'edad': edad,
        }
    
    contexto = Context(datos)
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)


def template3(request, nombre, apellido, edad):

    template = loader.get_template('template3.html')
    
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha,
        'nombre': nombre,
        'apellido':apellido,
        'edad': edad,
        }
    
    template_renderizado = template.render(datos)
    
    return HttpResponse(template_renderizado)


def template4(request, nombre, apellido, edad):

    fecha = datetime.now()
    
    datos = {
        'fecha': fecha,
        'nombre': nombre,
        'apellido':apellido,
        'edad': edad,
        }

    return render(request, 'template2.html', datos)

def probando (request):
    
    lista = list(range(500))
    
    numeros = random.choices(lista, k=50)
    print(numeros)
    return render(request, 'probando_if_for.html', {'numeros': numeros})

def crear_usuario(request, nombre, apellido):
    usuario = Usuario(nombre=nombre, apellido=apellido)
    usuario.save()
    return render(request, 'usuario_templates/creacion.html', {"usuario": usuario})

def crear_usuario_v2(request):
    
    #V1
    #print('valor de la request:', request)
    #print('valor de GET:', request.GET)
    #print('valor de POST:', request.POST)
    
    #if request.method == 'POST':
    #    usuario = Usuario(nombre=request.POST.get('nombre'), apellido=request.POST.get('apellido'), correo=request.POST.get('correo'), sugerencia=request.POST.get('sugerencia'))
    #    usuario.save()
    
    #return render(request, 'inicio/crear_usuario_v2.html')
    
    #V2
    print('valor de la request:', request)
    print('valor de GET:', request.GET)
    print('valor de POST:', request.POST)
    
    if request.method == 'POST':
        formulario = CrearFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            usuario = Usuario(nombre=datos.get('nombre'), apellido=datos.get('apellido'), correo=datos.get('correo'), sugerencia=datos.get('sugerencia'))
            usuario.save()
            return redirect('inicio')
        
    formulario = CrearFormulario()
    return render(request, 'inicio/crear_usuario_v2.html', {'formulario': formulario})