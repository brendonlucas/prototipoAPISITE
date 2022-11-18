from django.contrib.auth.models import User
from django.db import models

class TipoUsuario(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=255)


class Usuario(models.Model):
    name = models.CharField(max_length=150)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, null=True)
    telefone = models.IntegerField()
    # tipo = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, null=True)
    # instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, null=True, related_name='user_inst')

    @property
    def full_name(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)
