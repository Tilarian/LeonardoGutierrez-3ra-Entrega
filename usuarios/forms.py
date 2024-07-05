from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contrasenia", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contrasenia", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key:'' for key in fields}
        
class ModifyUser(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required=False)
    hobby = forms.CharField(max_length=20,required=False)
    
    class Meta:
        model = User
        fields = ['email','first_name', 'last_name', 'avatar', 'hobby']