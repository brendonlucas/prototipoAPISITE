from rest_framework import serializers
from veiculo.models import Veiculo, TipoVeiculo


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVeiculo
        fields = ('pk', 'name')


class VeiculoSerializer(serializers.ModelSerializer):
    tipo = TipoSerializer()

    class Meta:
        model = Veiculo
        fields = ('pk', 'name', 'placa', 'tipo', 'qtd_pessoas')


class VeiculoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ('pk', 'name',)


class CreateVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ('name', 'placa', 'qtd_pessoas')
