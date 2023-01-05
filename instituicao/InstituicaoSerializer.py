from rest_framework import serializers

from instituicao.models import Instituicao


class InstituicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituicao
        fields = ('pk', 'nome', 'codigo')


class InstituicaoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituicao
        fields = ('pk', 'name',)


class CreateInstituicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituicao
        fields = ('pk', 'name',)
