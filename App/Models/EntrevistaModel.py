from django.db import models
from ..models import edocivil, consultagral, antescolares, antfamiliares, antpatheredofam, antrecreathab, antsex, acompanantes, exploracionfisica, metanticonceptivos, tipoconsultas#, usuarios

class entrevista_model():
    def consultas_list():
        consultasvar = consultagral.objects.order_by("FolioConsulta")
        return consultasvar
    
    def getconsulta(FolioConsulta):
        consultamost = consultagral.objects.get(FolioConsulta=FolioConsulta)
        return consultamost