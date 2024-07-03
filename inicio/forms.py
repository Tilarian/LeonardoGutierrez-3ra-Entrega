from django import forms
from django.core.validators import MinValueValidator

class CrearFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    correo = forms.CharField(max_length=20)
    edad = forms.IntegerField(validators=[MinValueValidator(18)])
    
class EditarFormulario(CrearFormulario):
    ...
    
class BuscarUsuario(forms.Form):
    nombre= forms.CharField(max_length=20, required=False)