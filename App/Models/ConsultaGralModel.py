from django.db import models
from ..models import edocivil, consultagral, antescolares, antfamiliares, antpatheredofam, antrecreathab, antsex, acompanantes, exploracionfisica, metanticonceptivos, tipoconsultas
from django import forms

class RegistrarConsulta(forms.Form):
    Id_Exped_id = forms.IntegerField(label = 'Expediente')
    FolioConsulta = forms.IntegerField(label = 'Folio')
    FechaConsulta = forms.DateTimeField(label = 'Fecha')
    CURP_id = forms.CharField(label = 'Paciente', max_length=18)
    Id_Acomp_id = forms.IntegerField(label = 'Persona(s) que lo acompaña(n)', max_value=8)
    Id_TipoConsulta_id = forms.IntegerField(label='Tipo de Consulta', max_value=6)
    #UserID = forms.CharField(label = 'A', max_length=10)

class ConsultaGral_model():
    def consultasgral_list(filtrarconsulta):
        if filtrarconsulta == None:
            consultasvar = consultagral.objects.order_by("FolioConsulta")
        else:
            consultasvar = consultagral.objects.filter(FolioConsulta__contains=filtrarconsulta)
        return consultasvar
    
    def getconsultagral(FolioConsulta):
        consultamost = consultagral.objects.get(FolioConsulta=FolioConsulta)
        return consultamost
    
    def mis_consultas_list(request):
        #Metodo propuesto #1
        # consulta = None
        # Consultagral = consultagral.objects.filter(UserID = request.user.id)
        # for item in Consultagral:
        #     consulta = consultagral.objects.filter(FolioConsulta = item.FolioConsulta)
        # return consulta

        #Metodo propuesto #2
        i = 0
        Consultagral = consultagral.objects.filter(UserID = request.user.id)
        consulta = [[]] * len(Consultagral)
        for item in Consultagral:
            consulta[i] = consultagral.objects.get(FolioConsulta = item.FolioConsulta)
            i += 1
        return consulta
