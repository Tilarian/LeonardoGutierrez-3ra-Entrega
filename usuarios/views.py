from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import FormularioRegistro, ModifyUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import UserDetails

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contrasenia)
            
            django_login(request, user)
            
            UserDetails.objects.get_or_create(user=user)
            
            return redirect('inicio')
    
    return render(request, 'usuarios/login.html', {'formulario': formulario})

def register(request):
    
    formulario = FormularioRegistro()
    
    if request.method =='POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
        
    return render(request, 'usuarios/register.html', {'formulario': formulario})

@login_required
def modify_user(request):
    
    userdetails = request.user.userdetails
    formulario = ModifyUser(initial={'avatar': userdetails.avatar}, instance=request.user)
    
    if request.method == "POST":
        formulario = ModifyUser(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            userdetails.avatar = formulario.cleaned_data.get('avatar')
            userdetails.save()
            formulario.save()
            return redirect('modify_user')
    
    return render(request, 'usuarios/modify_user.html',{'formulario': formulario})


class ModifyPassword(PasswordChangeView):
    template_name = 'usuarios/modify_pass.html'
    success_url = reverse_lazy('modify_user')
    
@login_required
def info_user(request):
    userdetails = request.user.userdetails
    ModifyUser(initial={'avatar': userdetails.avatar}, instance=request.user)
    return render(request, 'usuarios/info_user.html')