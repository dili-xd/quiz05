from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Paciente, Especialidad, Doctor, Cita
from .serializers import PacienteSerializer,EspecialidadSerializer,DoctorSerializer,CitaSerializer
# Vistas para Paciente
# Vista pacientes mostrar y crear
class PacienteListCreateView(ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
# Vista pacientes mostrar, actualizar y eliminar
class PacienteUpdateView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
class PacienteDeleteView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id' # es para identificarlo, lo hace por el id
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
# Vistas para Especialidad
# Vista especialidades mostrar y crear
class EspecialidadListCreateView(ListCreateAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
# Vista especialidades actualizar y eliminar
class EspecialidadUpdateView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
class EspecialidadDeleteView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
# Vistas para Doctor
# Vista doctores mostrar y crear
class DoctorListCreateView(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
# Vista doctores actualizar y eliminar
class DoctorUpdateView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
class DoctorDeleteView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
# Vistas para Cita
# Vista citas mostrar y crear
class CitaListCreateView(ListCreateAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
# Vista citas actualizar y eliminar
class CitaUpdateView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
class CitaDeleteView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer