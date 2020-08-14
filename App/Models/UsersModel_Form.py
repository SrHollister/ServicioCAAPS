from django import forms

class IniciarSesion(forms.Form):
    first_name = forms.CharField(label = 'Nombre')
    last_name = forms.CharField(label = 'Apellidos')
    user = forms.CharField(label= 'Usuario')
    email = forms.EmailField(label = 'E-Mail')
    password = forms.CharField(widget = forms.PasswordInput)