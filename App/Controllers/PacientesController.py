from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from App.Models.PacientesModel import pacientes_model, RegistrarPaciente, RegistrarDomicilio
from ..models import pacientes, domicilios
from django.contrib import auth

class PacientesController():
    def index(request):
        filtrarpaciente = None
        if request.method == "POST":
            filtrarpaciente = request.POST.get('filtrarpaciente')
        pacientes_list = pacientes_model.pacientes_list(filtrarpaciente)
        paginator = Paginator(pacientes_list,15)#El segundo parametro corresponde a cuántos items se desea ver
        page = request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
                items = paginator.page(paginator.num_pages)
        context_pac = {'pacientes_list': items}
        return render(request, 'views/pacientes/pacientes.html', context_pac)

    def details(request,CURP):
        objects = pacientes_model.getpaciente(CURP)
        context_pac = {'paciente': objects}
        return render(request, 'views/pacientes/detailspac.html',context_pac)

    def registrarpaciente(request):
        dataCURP = None
        template = 'views/pacientes/registrarpaciente.html'
        if request.method == "POST":
            form = RegistrarPaciente(request.POST)
            if form.is_valid():
                CURP = form.cleaned_data.get('CURP')
                CURPpac = pacientes.objects.filter(CURP = CURP)
                for item in CURPpac:
                    dataCURP = item.CURP
                if dataCURP != None:
                    context_pac = {'form': form, 'error':'El paciente ya se encuentra registrado.'}
                    return render(request, template, context_pac)
                else:
                    Nombre_Pac = form.cleaned_data.get('Nombre_Pac')
                    Apellidos_Pac = form.cleaned_data.get('Apellidos_Pac')
                    FechaNac = form.cleaned_data.get('FechaNac')
                    Peso = form.cleaned_data.get('Peso')
                    Talla = form.cleaned_data.get('Talla')
                    CURP = form.cleaned_data.get('CURP')
                    Telefono = form.cleaned_data.get('Telefono')
                    Sexo = form.cleaned_data.get('Sexo')
                    Id_EdoCivil_id = form.cleaned_data.get('Id_EdoCivil_id')
                    Newpaciente = pacientes(Nombre_Pac=Nombre_Pac, Apellidos_Pac=Apellidos_Pac, FechaNac=FechaNac, Peso=Peso, Talla=Talla, CURP=CURP,Telefono=Telefono, Sexo=Sexo, Id_EdoCivil_id=Id_EdoCivil_id)
                    Newpaciente.save()
                    return HttpResponseRedirect('pacientes')
            else:
                context_pac = {'form': form}
                return render(request, template, context_pac)
        else:
            context_pac = {'form': RegistrarPaciente()}
            return render(request, template, context_pac)

    def registrardomicilio(request):
        dataDOM = None
        template = 'views/pacientes/registrardomicilio.html'
        if request.method == "POST":
            form = RegistrarDomicilio(request.POST)
            if form.is_valid():
                CURP = form.cleaned_data.get('CURP')
                CURPdom = domicilios.objects.filter(CURP = CURP)
                for item in CURPdom:
                    dataDOM = item.CURP
                if dataDOM != None:
                    context_domicilio = {'form': form, 'error':'El paciente ya cuenta con domicilio registrado.'}
                    return render(request, template, context_domicilio)
                else:
                    CURP = form.cleaned_data.get('CURP')
                    Calle = form.cleaned_data.get('Calle')
                    NumInt = form.cleaned_data.get('NumInt')
                    NumExt = form.cleaned_data.get('NumExt')
                    Colonia = form.cleaned_data.get('Colonia')
                    CP = form.cleaned_data.get('CP')
                    Municipio = form.cleaned_data.get('Municipio')
                    Estado = form.cleaned_data.get('Estado')
                    Newdomicilio = domicilios()
                    Newdomicilio.CURP = pacientes.objects.get(CURP = request.POST['CURP'])
                    Newdomicilio.save()
                    return HttpResponseRedirect('pacientes')
            else:
                context_domicilio = {'form': form}
                return render(request, template, context_domicilio)
        else:
            context_domicilio = {'form': RegistrarDomicilio()}
            return render(request, template, context_domicilio)