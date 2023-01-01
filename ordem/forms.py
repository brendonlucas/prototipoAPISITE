from django import forms


class CreateOrdem(forms.Form):
    qtd_carga = forms.IntegerField()
    data = forms.DateField()
    hora = forms.TimeField()
    saida = forms.CharField(max_length=100)
    destino = forms.CharField(max_length=100)
    descricao = forms.CharField(max_length=250)

    def is_valid(self):
        valid = True

        return valid


class ConfirmOrdem(forms.Form):
    veiculo = forms.IntegerField()
    motorista = forms.IntegerField()
    data = forms.DateField()
    hora = forms.TimeField()




    def is_valid(self):
        valid = True

        return valid