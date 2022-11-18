from django import forms


class CreateVeiculo(forms.Form):
    name = forms.CharField(max_length=16)
    qtd_carga = forms.IntegerField()
    tipo = forms.IntegerField()
    placa = forms.CharField(max_length=16)

    def is_valid(self):
        valid = True

        return valid
