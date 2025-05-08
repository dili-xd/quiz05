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
    def validar_especialidad(self,value):
        if len(value)<4:
            raise serializers.ValidationError("La especialidad debe tener como minimo 4 caracteres")
        return value
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Doctor
        fields="__all__"
    def validar_nombre(self,value):
        if len(value) <2:
            raise serializers.ValidationError("El nombre debe tener como minimo 2 caracteres")
        return value
    def validar_apellido(self,value):
        if len(value) < 1:
            raise serializers.ValidationError("El apellido debe tener como minimo 2 caracteres")
        return value
    def validar_experiencia(self,value):
        if value < 0:
            raise serializers.ValidationError("La experiencia no puede ser negativa")
        return value
class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cita
        fields="__all__"
    def validar_hora(self,value):
        if value < 0:
            raise serializers.ValidationError("La hora no puede ser negativa")
        return value
    def validar_fecha(self,value):
        if value < 0:
            raise serializers.ValidationError("La fecha no puede ser negativa")
        return value
class DoctorEspecialidadSeralizer(serializers.ModelSerializer):
    class Meta:
        model=DoctorEspecialidad
        fields="__all__"