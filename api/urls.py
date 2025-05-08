from django.urls import path
from .views import PacienteListCreateView,PacienteDeleteView,PacienteUpdateView,EspecialidadListCreateView,EspecialidadDeleteView,EspecialidadUpdateView
from .views import DoctorListCreateView,DoctorDeleteView,DoctorUpdateView,CitaListCreateView,CitaDeleteView,CitaUpdateView
urlpatterns = [
    path('pacientes/',PacienteListCreateView.as_view()),
    path('pacientesEliminar/<int:id>/',PacienteDeleteView.as_view()),
    path('pacienteActualizar/<int:id>/',PacienteUpdateView.as_view()),
    path('especialidades/',EspecialidadListCreateView.as_view()),
    path('especialidadesEliminar/<int:id>/',EspecialidadDeleteView.as_view()),
    path('especialidadesActualizar/<int:id>/',EspecialidadUpdateView.as_view()),
    path('doctores/',DoctorListCreateView.as_view()),
    path('doctoresEliminar/<int:id>/',DoctorDeleteView.as_view()),
    path('doctoresActualizar/<int:id>/',DoctorUpdateView.as_view()),
    path('citas/',CitaListCreateView.as_view()),
    path('citasEliminar/<int:id>/',CitaDeleteView.as_view()),
    path('citasActualizar/<int:id>/',CitaUpdateView.as_view()),
]