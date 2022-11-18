from django.forms import *
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Nome', max_length=16)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput, max_length=10)


class RegistrarUsuarioForm(forms.Form):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    telefone = forms.IntegerField(required=True)
    senha = forms.CharField(required=True)
    ConfirmPassword = forms.CharField(required=True)

    def is_valid(self):
        valid = True

        return valid


class ChangeCargoForm(forms.Form):
    cargo = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        return valid