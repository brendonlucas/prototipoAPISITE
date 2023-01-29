import datetime

from django.db import models

from instituicao.models import Instituicao


class TipoVeiculo(models.Model):
    name = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150, null=True)


def upload_to_image(instance, filename):
    return 'images/' + set_name_image() + filename


class Veiculo(models.Model):
    image = models.FileField(upload_to=upload_to_image, blank=True, default='defaults/ic_car_image.png')
    name = models.CharField(max_length=150)
    qtd_pessoas = models.IntegerField()
    placa = models.CharField(max_length=150)
    tipo = models.ForeignKey(TipoVeiculo, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, null=True)


def set_name_image():
    x = datetime.datetime.now()
    a = str(x)
    name = ''
    for letra in a:
        if letra not in ('-', '.', ',', ':', ' '):
            name += letra
    print(name)
    return name
