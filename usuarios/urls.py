from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('user/modify/', views.modify_user, name='modify_user'),
    path('user/modify/password/', views.ModifyPassword.as_view(), name='modify_pass'),
    
]
