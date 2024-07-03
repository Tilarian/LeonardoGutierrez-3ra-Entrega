from django.db import models
from django.core.validators import MinValueValidator

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)
    edad = models.IntegerField(validators=[MinValueValidator(18)])
    
    def __str__(self):
        return f'\nNombre: {self.nombre}\nApellido: {self.apellido}\nCorreo: {self.correo}\nEdad: {self.edad}'