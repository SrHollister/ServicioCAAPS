from django.db import models
from ..models import pacientes, edocivil, domicilios
from django import forms

class pacientes_model():
    def pacientes_list(filtrarpaciente):
        if filtrarpaciente == None:
            pacientesvar = pacientes.objects.order_by("Nombre_Pac")
        else:
            pacientesvar = pacientes.objects.filter(CURP__icontains=filtrarpaciente)
        return pacientesvar
    
    def getpaciente(CURP):
        pacientemost = pacientes.objects.get(CURP=CURP)
        return pacientemost

#class domicilios_model():
#    def domicilios_list():
#        domiciliosvar = domicilios.objects()
#        return domiciliosvar

class RegistrarPaciente(forms.Form):
    Nombre_Pac = forms.CharField(label = 'Nombre')
    Apellidos_Pac = forms.CharField(label = 'Apellidos')
    FechaNac = forms.DateField(label = 'Fecha de Nacimiento')
    Peso = forms.DecimalField(label = 'Peso (Kg)', max_digits=5, decimal_places=2)
    Talla = forms.DecimalField(label = 'Estatura (m)', max_digits=3, decimal_places=2)
    CURP = forms.CharField(label='CURP', max_length=18)
    Telefono = forms.CharField(label = 'Teléfono', max_length=10)
    Sexo = forms.CharField(label= 'Sexo', max_length=1)
    Id_EdoCivil_id = forms.IntegerField(label = 'Estado Civil')

class RegistrarDomicilio(forms.Form):
    CURP = forms.CharField(label = 'CURP del paciente', max_length=18)
    Calle = forms.CharField(label = 'Calle', max_length=100)
    NumInt = forms.IntegerField(label = 'Núm. Interior')
    NumExt = forms.IntegerField(label = 'Núm Exterior')
    Colonia = forms.CharField(label = 'Colonia', max_length=75)
    CP = forms.IntegerField(label = 'Código Postal')
    Municipio = forms.CharField(label = 'Municipio', max_length=100)
    Estado = forms.CharField(label = 'Estado', max_length=50)