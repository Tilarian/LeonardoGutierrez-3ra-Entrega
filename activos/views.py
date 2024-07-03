from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
    model = User
    template_name = 'users/edit_user.html'
    success_url = reverse_lazy('users')
    fields = ['name','surname','email','age']

class DisplayUser(DetailView):
    model = User
    template_name = 'users/display_user.html'
    
class DeleteUser(DeleteView):
    model = User
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('users')
