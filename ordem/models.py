from django.db import models

from instituicao.models import Instituicao
from usuario.models import Usuario
from veiculo.models import Veiculo


class StatusOrdem(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)


class Ordem(models.Model):
    solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitante_user', null=True)
    descricao = models.CharField(max_length=255)
    qtd_espaco = models.IntegerField(null=False)
    data_solicitacao = models.DateField(null=False, auto_now=True)
    data_solicitado = models.DateField(null=True)
    horario_requirido = models.TimeField(null=False, auto_now=True)
    data_agendada = models.DateField(null=False, auto_now_add=True, blank=True)
    origem = models.CharField(max_length=252)
    destino = models.CharField(max_length=252)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, related_name='ordem_inst')
    motorista = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='motorista_user', null=True)
    status = models.ForeignKey(StatusOrdem, on_delete=models.CASCADE, related_name='status_ordem', null=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='veiculo_ordem', null=True)

    # Ordem(solicitante, descricao, qtd_espaco, data_solicitacao, horario_requirido, data_agendada, origem, destino,
    #       instituicao, motorista, status, veiculo)


def a():
    pass
