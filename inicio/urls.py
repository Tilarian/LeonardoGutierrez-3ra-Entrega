from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('template1/<str:nombre>/<str:apellido>/<int:edad>', views.template1),
    path('template2/<str:nombre>/<str:apellido>/<int:edad>', views.template2),
    path('template3/<str:nombre>/<str:apellido>/<int:edad>', views.template3),
    path('template4/<str:nombre>/<str:apellido>/<int:edad>', views.template4),
    path('probando/', views.probando, name="probando"),
    #path('usuarios/crear/<str:nombre>/<str:apellido>', views.crear_usuario, name="crear_usuario")
    path('usuarios/crear/', views.crear_usuario_v2, name="crear_usuario_v2"),
]