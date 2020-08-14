from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from App.Models.EntrevistaModel import entrevista_model
from App.Models.ExpedientesModel import expedientes_model, RegistrarExpediente
from ..models import expedientes, pacientes

class ExpedientesController():
    def index(request):
        filtrarexpediente = None
        if request.method == "POST":
            filtrarexpediente = request.POST.get('filtrarexpediente')
        expedientes_list = expedientes_model.expedientes_list(filtrarexpediente)
        paginator = Paginator(expedientes_list,6) #El segundo parametro corresponde a cuántos items se desea ver
        page = request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
                items = paginator.page(paginator.num_pages)
        context_exped = {'expedientes_list': items}
        return render(request, 'views/expedientes/expedientes.html', context_exped)

    def details(request,Id_Exped):
        objects = expedientes_model.getexpediente(Id_Exped)
        context_exped = {'expediente': objects}
        return render(request, 'views/expedientes/detailsexped.html', context_exped)

    def registrarexpediente(request):
        dataCURP = None
        template = 'views/expedientes/registrarexpediente.html'
        if request.method == "POST":
            form = RegistrarExpediente(request.POST)
            if form.is_valid():
                CURP = form.cleaned_data.get('CURP')
                CURPexped = expedientes.objects.filter(CURP = CURP)
                for item in CURPexped:
                    dataCURP = item.CURP
                if dataCURP != None:
                    context_exped = {'form': form, 'error':'El paciente ya cuenta con expediente registrado.'}
                    return render(request, template, context_exped)
                else:
                    CURP = form.cleaned_data.get('CURP')
                    #NewExpediente = expedientes(CURP=CURP)
                    #NewExpediente.save()
                    NewExpediente = expedientes()
                    NewExpediente.CURP = pacientes.objects.get(CURP = request.POST['CURP'])
                    NewExpediente.save()
                    return HttpResponseRedirect('expedientes')
            else:
                context_exped = {'form': form}
                return render(request, template, context_exped)
        else:
            context_exped = {'form': RegistrarExpediente()}
            return render(request, template, context_exped)

class ConsultasController():
    def index(request, Id_Exped):
        consultas_list = entrevista_model.consultas_list(Id_Exped)
        context_con = {'consultas_list': consultas_list}
        return render(request, 'views/expedientes/detailsexped.html', context_con)

    def details(request,Id_Exped):
        objects = entrevista_model.getconsulta(Id_Exped)
        context_con = {'consulta': objects}
        return render(request, 'views/consultas/detailsconsulta.html',context_con)