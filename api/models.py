from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    cedula = models.CharField(max_length=15,unique=True)


