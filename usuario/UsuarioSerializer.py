from django.contrib.auth.models import User
from rest_framework import serializers
from usuario.models import Usuario


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name', 'last_name')


class UsuarioSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Usuario
        fields = ('pk', 'name', 'telefone','cargo', 'user')


class UsuarioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('pk', 'name',)


class CreateUserComplementeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name',)


class CreateUserSerializer(serializers.ModelSerializer):
    user = CreateUserComplementeSerializer()

    class Meta:
        model = Usuario
        fields = ('name', 'telefone', 'user')


class CreateFuncionarioSerializer(serializers.ModelSerializer):
    user = CreateUserComplementeSerializer()

    class Meta:
        model = Usuario
        fields = ('name', 'telefone', 'user')


class FuncionarioSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="Funcionario-detail")
    user = UserSerializer()

    class Meta:
        model = Usuario
        fields = ('url', 'pk', 'nome', 'telefone', 'user')
