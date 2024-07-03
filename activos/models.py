from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    age = models.IntegerField(validators=[MinValueValidator(18)])
    
    def __str__(self):
        return f'{self.name} | {self.surname} | {self.email} | {self.age}'
