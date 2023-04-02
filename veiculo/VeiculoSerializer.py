from rest_framework import serializers
from veiculo.models import Veiculo, TipoVeiculo


# class TipoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TipoVeiculo
#         fields = ('pk', 'name')


class VeiculoSerializer(serializers.ModelSerializer):
    # tipo = TipoSerializer()
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = Veiculo
        fields = ('pk', 'name', 'placa', 'tipo', 'qtd_pessoas', 'image')

    def get_photo_url(self, car):
        request = self.context.get('request')
        image = car.image.url
        return request.build_absolute_uri(image)


class VeiculoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ('pk', 'name',)


class VeiculoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ('name', 'placa', 'tipo', 'qtd_pessoas',)


class CreateVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ('name', 'placa', 'qtd_pessoas')
