from rest_framework import serializers

from instituicao.models import Instituicao


class InstituicaoSerializer(serializers.ModelSerializer):
    veiculos = serializers.HyperlinkedIdentityField(view_name="veiculo-list")
    funcionario = serializers.HyperlinkedIdentityField(view_name="API-Get-All-Func-Inst")

    class Meta:
        model = Instituicao
        fields = ('pk', 'nome', 'codigo', 'veiculos', 'funcionario')


class InstituicaoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituicao
        fields = ('pk', 'name',)


class CreateInstituicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituicao
        fields = ('pk', 'name',)
