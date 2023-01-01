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
    origem = models.CharField(max_length=252)
    destino = models.CharField(max_length=252)
    data_solicitacao = models.DateField(null=True)
    data_solicitado = models.DateField(null=True, blank=True)
    horario_requirido = models.TimeField(null=True)

    data_marcada = models.DateField(null=True)
    horario_marcado = models.TimeField(null=True)

    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, related_name='ordem_inst')
    motorista = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='motorista_user', null=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='veiculo_ordem', null=True)
    status = models.ForeignKey(StatusOrdem, on_delete=models.CASCADE, related_name='status_ordem', null=True)

    # Ordem(solicitante, descricao, qtd_espaco, data_solicitacao, horario_requirido, data_agendada, origem, destino,
    #       instituicao, motorista, status, veiculo)


def a():
    pass
