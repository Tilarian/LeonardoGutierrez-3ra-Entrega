from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Comment(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    comentario = models.CharField(max_length=50)
    edad = models.IntegerField(validators=[MinValueValidator(18)])
    fecha = models.DateField()
    
    def __str__(self):
        return f'{self.nombre} | {self.apellido} | {self.comentario} | {self.edad} | {self.fecha}'
