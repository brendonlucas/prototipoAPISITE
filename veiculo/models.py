from django.db import models

from instituicao.models import Instituicao


class TipoVeiculo(models.Model):
    name = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150, null=True)


class Veiculo(models.Model):
    name = models.CharField(max_length=150)
    qtd_pessoas = models.IntegerField()
    placa = models.CharField(max_length=150)
    tipo = models.ForeignKey(TipoVeiculo, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, null=True)


