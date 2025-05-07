from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad = models.IntegerField()
    cedula = models.CharField(max_length=15, unique=True)
    telefono=models.CharField(max_length=15,unique=True)

class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)

class Doctor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    experiencia = models.IntegerField()
    doctor_especialidad=models.ManyToManyField(Especialidad,through="DoctorEspecialidad")


class DoctorEspecialidad(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=200)

