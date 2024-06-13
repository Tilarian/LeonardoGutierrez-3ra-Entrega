from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('probando/', views.probando, name="probando"),
    path('usuarios/crear/', views.crear_usuario_v2, name="crear_usuario_v2"),
    path('usuarios/', views.usuarios, name="usuarios")
]