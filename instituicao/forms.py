from django.forms import *
from django import forms


class JoinRoomForm(forms.Form):
    InputCode = forms.CharField(max_length=10)

    def is_valid(self):
        valid = True
        if self.data['InputCode']:
            return valid



class CreateIntituicaoForm(forms.Form):
    NameInst = forms.CharField(max_length=100)
    # Descricao = forms.CharField(max_length=250)
    def is_valid(self):
        valid = True
        return valid