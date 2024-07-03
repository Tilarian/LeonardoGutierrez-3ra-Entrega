from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Comment
from django.urls import reverse_lazy

class Comments(ListView):
    model = Comment
    template_name = 'comments/comments_list.html'
    context_object_name = 'comments'
    
class CreateComment(CreateView):
    model = Comment
    template_name = 'comments/create_comment.html'
    success_url = reverse_lazy('comments')
    fields = ['nombre','apellido','comentario','edad']
    
class EditComment(UpdateView):
    model = Comment
    template_name = 'comments/edit_comment.html'
    success_url = reverse_lazy('comments')
    fields = ['nombre','apellido','comentario','edad']

class DisplayComment(DetailView):
    model = Comment
    template_name = 'comments/display_comment.html'
    
class DeleteComment(DeleteView):
    model = Comment
    template_name = 'comments/delete_comment.html'
    success_url = reverse_lazy('comments')
