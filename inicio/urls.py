from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('probando/', views.probando, name="probando"),
    path('usuarios/crear/', views.crear_usuario_v2, name="crear_usuario_v2"),
    path('usuarios/', views.usuarios, name="usuarios"),
    path('usuarios/eliminar/<int:id>', views.eliminar_usuario, name="eliminar_usuario"),
    path('usuarios/editar/<int:id>', views.editar_usuario, name="editar_usuario"),
    path('usuarios/<int:id>', views.ver_usuario, name="ver_usuario"),

]