from rest_framework import serializers
from .models import Paciente,Especialidad, Doctor,Cita,DoctorEspecialidad

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = "__all__"

    def validar_nombre(self,value):
        if len(value) < 4:
            raise serializers.ValidationError("El nombre debe tener como minimo 4 caracteres")
        return value
    def validar_apellido(self,value):
        if len(value)<4:
            raise serializers.ValidationError("El apellido debe tener como minimo 4 caracteres")
        return value
    
    
class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = "__all__"

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Doctor
        fields="__all__"

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cita
        fields="__all__"     

class DoctorEspecialidadSeralizer(serializers.ModelSerializer):
    class Meta:
        model=DoctorEspecialidad
        fields="__all__"
