"""SeapCaaps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from App.Controllers.IndexController import IndexController
from App.Controllers.PacientesController import PacientesController
from App.Controllers.ExpedientesController import ExpedientesController
from App.Controllers.ConsultasController import ConsultasController
from App.Controllers.UserController import UserController

#Definimos los parametros que se ingresan a traves de la URL para ejecutar las vistas segun sea el parametro
urlpatterns = [
    path('admin/', admin.site.urls, name='login'),
    path('', IndexController.index, name='index'),
    path('iniciasesion', UserController.iniciasesion, name='iniciasesion'),
    path('registrarpaciente', PacientesController.registrarpaciente, name='registrarpaciente'),
    path('registrardomicilio', PacientesController.registrardomicilio, name='registrardomicilio'),
    path('registrarexpediente', ExpedientesController.registrarexpediente, name='registrarexpediente'),
    path('pacientes', PacientesController.index, name='pacientes'),
    path('expedientes', ExpedientesController.index, name='expedientes'),
    path('consultas', ConsultasController.index, name='consultas'),
    path('registrarconsulta', ConsultasController.registrarconsulta, name='registrarconsulta'),
    path('mis_consultas', ConsultasController.mis_consultas, name='mis_consultas'),
    path('about', IndexController.about, name='about'),
    #path('detailspac/<str:CURP>/', PacientesController.details, name='detailspac'),
    path('detailsexped/<int:Id_Exped>/', ExpedientesController.details, name='detailsexped'),
    path('detailsconsulta/<int:FolioConsulta>/', ConsultasController.details, name='detailsconsulta'),
    #url(r'^admin/salmonella/', include('salmonella.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
