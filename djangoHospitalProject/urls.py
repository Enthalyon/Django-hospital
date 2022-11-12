"""djangoHospitalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from auxiliarApp import views as auxiliar_views
from familiarAsignadoApp import views as familiar_asignado_views
from pacienteApp import views as paciente_views
from profesionalApp import views as profesional_views
from signosVitalesApp import views as signos_vitales_views
from usuariosApp import views as usuarios_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refrescar/', TokenRefreshView.as_view()),
    path('usuario/actualizar/<int:pk>/', usuarios_views.ActualizarUsuarioView.as_view()),
    path('usuario/consultar/<int:pk>/', usuarios_views.ConsultaUsuarioView.as_view()),
    path('usuarios/consultar/', usuarios_views.ConsultaUsuariosView.as_view()),
    path('usuario/consultar/token/', usuarios_views.ConsultaUsuarioPorToken.as_view()),
    path('usuario/registrar/', usuarios_views.CrearUsuarioView.as_view()),
    path('usuario/eliminar/<int:pk>/', usuarios_views.EliminarUsuarioView.as_view()),
    path('auxiliar/actualizar/<int:pk>/', auxiliar_views.ActualizarAuxiliarView.as_view()),
    path('auxiliar/consultar/<int:pk>/', auxiliar_views.ConsultarAuxiliarView.as_view()),
    path('auxiliar/obtener/<int:pk>/', auxiliar_views.ObtenerAuxiliarView.as_view()),
    path('auxiliar/registrar/', auxiliar_views.CrearAuxiliarView.as_view()),
    path('auxiliar/eliminar/<int:pk>/', auxiliar_views.EliminarAuxiliarView.as_view()),
    path('familiar/actualizar/<int:pk>/',familiar_asignado_views.ActualizarFamiliarAsignadoView.as_view()),
    path('familiar/consultar/<int:pk>/', familiar_asignado_views.ConsultarFamiliarAsignadoView.as_view()),
    path('familiar/obtener/<int:pk>/', familiar_asignado_views.ObtenerFamiliarAsignadoView.as_view()),
    path('familiar/registrar/', familiar_asignado_views.CrearFamiliarAsignadoView.as_view()),
    path('familiar/eliminar/<int:pk>/', familiar_asignado_views.EliminarFamiliarAsignadoView.as_view()),
    path('paciente/actualizar/<int:pk>/', paciente_views.ActualizarPacienteView.as_view()),
    path('paciente/consultar/<int:pk>/', paciente_views.ConsultarPacienteView.as_view()),
    path('pacientes/consultar/', paciente_views.ConsultarPacientesView.as_view()),
    path('pacientes/consultar/profesional/<int:pk>/', paciente_views.ConsultarPacientesPorProfesionalMedicoView.as_view()),
    path('pacientes/consultar/familiar/<int:pk>/', paciente_views.ConsultarPacientesPorFamiliar.as_view()),
    path('paciente/obtener/<int:pk>/', paciente_views.ObtenerPacienteView.as_view()),
    path('paciente/registrar/', paciente_views.CrearPacienteView.as_view()),
    path('paciente/eliminar/<int:pk>/', paciente_views.EliminarPacienteView.as_view()),
    path('profesional/actualizar/<int:pk>/', profesional_views.ActualizarProfesionalView.as_view()),
    path('profesional/consultar/<int:pk>/', profesional_views.ConsultarProfesionalView.as_view()),
    path('profesionales/consultar/', profesional_views.ConsultarProfesionalesView.as_view()),
    path('profesional/obtener/<int:pk>/', profesional_views.ObtenerProfesionalView.as_view()),
    path('profesional/registrar/', profesional_views.CrearProfesionalView.as_view()),
    path('profesional/eliminar/<int:pk>/', profesional_views.EliminarProfesionalView.as_view()),
    path('vitalidad/actualizar/<int:pk>/', signos_vitales_views.ActualizarSignosVitalesView.as_view()),
    path('vitalidad/consultar/<int:pk>/', signos_vitales_views.ConsultarSignosVitalesView.as_view()),
    path('vitalidad/consultar/paciente/<int:pk>/', signos_vitales_views.ConsultarSignosVitalesPorPaciente.as_view()),
    path('vitalidad/registrar/', signos_vitales_views.CrearSignosVitalesView.as_view()),
    path('vitalidad/eliminar/<int:pk>/', signos_vitales_views.EliminarSignosVitalesView.as_view()),
    #path('', ),

]
