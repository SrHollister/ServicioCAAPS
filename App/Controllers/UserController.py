from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from App.Models.UsersModel_Form import IniciarSesion
from django.contrib.auth.models import User
from django.contrib import auth

class UserController():
    def iniciasesion(request):
        dataEmail = None
        template = 'views/user/loginuser.html'
        if request.method == "POST":
            form = IniciarSesion(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                userdb = User.objects.filter(email = email)
                for item in userdb:
                    dataEmail = item.email
                if dataEmail != None:
                    context_user = {'form': form, 'error':'El email ya se encuentra registrado.'}
                    return render(request, template, context_user)
                else:
                    password = form.cleaned_data.get('password')
                    username = form.cleaned_data.get('user')
                    first_name = form.cleaned_data.get('first_name')
                    last_name = form.cleaned_data.get('last_name')
                    User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password, is_staff = 1)
                    #user = auth.authenticate(username = username, password = password)
                    #auth.login(request, user)
                    return HttpResponseRedirect("admin/auth/user/")
            else:
                context_user = {'form': form}
                return render(request, template, context_user)
        else:
            context_user = {'form': IniciarSesion()}
            return render(request, template, context_user)