from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from .models import User
from django.urls import reverse_lazy

class Users(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'
    
class CreateUser(CreateView):
    model = User
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('users')
    fields = ['name','surname','email','age']
    
class EditUser(UpdateView):
    ...
    
class DisplayUser(DetailView):
    model = User
    template_name = 'users/display_user.html'