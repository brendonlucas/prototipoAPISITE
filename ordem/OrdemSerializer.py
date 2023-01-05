from rest_framework import serializers

from ordem.models import *
from usuario.UsuarioSerializer import *
from veiculo.VeiculoSerializer import VeiculoSerializer


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusOrdem
        fields = ('pk', 'name')


class OrdemSerializer(serializers.ModelSerializer):
    # solicitante = serializers.HyperlinkedIdentityField(view_name="API-Get-User-Detail")
    # motorista = serializers.HyperlinkedIdentityField(view_name="API-Get-User-Detail")
    # veiculo = serializers.HyperlinkedIdentityField(view_name="veiculo-Detail")
    solicitante = UsuarioSerializer()
    motorista = UsuarioSerializer()
    veiculo = VeiculoSerializer()
    status = StatusOrdem()
    url = serializers.HyperlinkedIdentityField(view_name="API-Get-Ordem")

    class Meta:
        model = Ordem
        fields = ('url', 'pk', 'solicitante', 'motorista', 'veiculo', 'data_solicitacao', 'status')


class OrdemDetailSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="API-Get-User-Detail")
    users = UserSerializer(read_only=True, many=True)
    solicitante = UserSerializer()

    class Meta:
        model = Ordem
        fields = ('pk', 'solicitante', 'user')


class CreateOrdemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordem
        fields = ('solicitante', 'data_solicitado', 'horario_requirido', 'descricao', 'qtd_espaco', 'origem', 'destino')


class GConfirmOrdemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordem
        fields = ('motorista', 'veiculo', 'data_marcada', 'horario_marcado')


class GInicioOrdemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordem
        fields = ()


class GFinalizeOrdemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordem
        fields = ()
