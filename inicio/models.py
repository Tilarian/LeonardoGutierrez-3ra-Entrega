from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)
    sugerencia = models.CharField(max_length=20)
    
    def __str__(self):
        return f'Soy el usuario de {self.nombre} {self.apellido} {self.correo} {self.sugerencia}'