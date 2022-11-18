from django.db import models

from usuario.models import Usuario


class Cargo(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)


class Instituicao(models.Model):
    nome = models.CharField(max_length=150)
    # criador = models.OneToOneField(Usuario, on_delete=models.CASCADE, null=True, related_name='criador_inst')
    funcionarios = models.ManyToManyField(Usuario)
    codigo = models.CharField(max_length=10, null=True, default="12345")


class CargosInstituicao(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, null=True)


def cargos():
    c1 = Cargo(nome="sem cargo", descricao="").save()
    c2 = Cargo(nome="Adminstrador", descricao="").save()
    c3 = Cargo(nome="gerente", descricao="").save()
    c4 = Cargo(nome="funcionario", descricao="").save()
