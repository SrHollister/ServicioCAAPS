from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from App.Models.ConsultaGralModel import RegistrarConsulta,ConsultaGral_model
from App.Models.EntrevistaModel import entrevista_model


class ConsultasController():
    def index(request):
        #Nuevo metodo
        filtrarconsulta = None
        if request.method == "POST":
            filtrarconsulta = request.POST.get('filtrarconsulta')
        consultas_list = ConsultaGral_model.consultasgral_list(filtrarconsulta)
        #Antiguo metodo
        # consultas_list = ConsultaGral_model.consultasgral_list()
        context_con = {'consultas_list': consultas_list}
        return render(request, 'views/consultas/consultas.html', context_con)

    def details(request,FolioConsulta):
        objects = ConsultaGral_model.getconsultagral(FolioConsulta)
        context_con = {'consulta': objects}
        return render(request, 'views/consultas/detailsconsulta.html',context_con)

    def registrarconsulta(request):
        template = 'views/consultas/registrarconsulta.html'
        if request.method == "POST":
            if request.user.is_authenticated:
                form = RegistrarConsulta(request.POST)
                userid = request.POST['userid']
                userid = request.user.id
                model = Newconsultagral(
                    Id_Exped_id = Id_Exped_id,
                    FolioConsulta = FolioConsulta,
                    FechaConsulta = datetime.today(),
                    CURP_id = CURP_id,
                    Id_Acomp_id = Id_Acomp_id,
                    Id_TipoConsulta_id = Id_TipoConsulta_id,
                    UserID = userid
                )
                model.save()
                #Id_Exped_id=form.cleaned_data.get('Id_Exped_id')
                return HttpResponseRedirect('mis_consultas')
            else:
                context_consulta = {'form': form}
                return render(request, template, context_consulta)
    
    def mis_consultas(request):
        consultasgral_list = ConsultaGral_model.mis_consultas_list(request)
        paginator = Paginator(consultasgral_list,1)#El segundo parametro corresponde a cuántos items se desea ver
        page = request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
                items = paginator.page(paginator.num_pages)
        context_consulta = {
            #'meta_description':'',
            #'meta_keywords':'',
            'items':items,
        }
        return render(request, "views/consultas/mis_consultas.html", context_consulta)