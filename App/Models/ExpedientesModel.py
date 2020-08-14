from django.db import models
from ..models import pacientes, expedientes
from django import forms

class expedientes_model():
    def expedientes_list(filtrarexpediente):
        if filtrarexpediente == None:
            expedientesvar = expedientes.objects.order_by("CURP_id")
        else:
            expedientesvar = expedientes.objects.filter(Id_Exped__contains=filtrarexpediente)
        return expedientesvar

    def getexpediente(Id_Exped):
        expedientemost = expedientes.objects.get(Id_Exped=Id_Exped)
        return expedientemost

class RegistrarExpediente(forms.Form):
    CURP = forms.CharField(label= 'CURP del Paciente', required=True)
    CURP2 = forms.SelectMultiple()