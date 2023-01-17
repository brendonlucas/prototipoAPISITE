from django.shortcuts import render, redirect
from rest_framework.views import APIView

from instituicao.models import Instituicao
from ordem.models import Ordem
from usuario.models import Usuario

from veiculo.VeiculoSerializer import *
from veiculo.forms import CreateVeiculo
from veiculo.models import Veiculo, TipoVeiculo

from rest_framework import generics, status, permissions
from rest_framework.response import Response


def get_user_logged(request):
    return request.user


def get_user(request):
    return Usuario.objects.get(user=get_user_logged(request))


def add_veiculo(request, pk):
    if request.method == 'POST':
        form = CreateVeiculo(request.POST)
        if form.is_valid():
            instituicao = Instituicao.objects.filter(id=pk).first()
            if instituicao:
                dados_form = form.data
                tipo = TipoVeiculo.objects.get(id=form.data['tipo'])
                veiculo = Veiculo(name=form.data['name'], qtd_pessoas=form.data['QtdCarga'],
                                  placa=form.data['placa'].upper(), tipo=tipo, instituicao=instituicao).save()
                return redirect('veiculos_show', pk)
        return redirect('veiculos_show', pk)


def edit_veiculo(request):
    pass


def remove_veiculo(request):
    pass


def show_veiculos(request, pk):
    instituicao = Instituicao.objects.get(id=pk)
    veiculos = Veiculo.objects.filter(instituicao=pk)
    return render(request, 'show_veiculos.html',
                  {'user': get_user_logged(request), 'veiculos': veiculos, 'instituicao': instituicao,
                   'usuario': get_user(request)})


def details_veiculo(request, pk, pk_2):
    veiculo = Veiculo.objects.get(id=pk_2, instituicao=pk)
    instituicao = Instituicao.objects.get(id=pk)
    ordens = Ordem.objects.filter(veiculo=pk_2, instituicao=pk, status_id__in=[2, 4, 1]).order_by('data_solicitacao')[
             :5]
    return render(request, 'Details_veiculo.html',
                  {'user': get_user_logged(request), 'veiculo': veiculo, 'instituicao': instituicao,
                   'usuario': get_user(request), 'ordens': ordens})


# APIIIIIIIIIIIIIIIIIIIII

class VeiculoLists(generics.RetrieveUpdateDestroyAPIView):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    name = 'veiculo-list'
    # permission_classes = (permissions.IsAuthenticated,)


class ApiVeiculoList(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, pk):
        try:
            Instituicao.objects.get(id=pk)
        except Instituicao.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_INSTITUICAO"}, status=status.HTTP_404_NOT_FOUND)

        veiculos = Veiculo.objects.filter(instituicao=pk)
        print(request.data)
        file_serializer = VeiculoSerializer(veiculos, many=True)
        return Response(file_serializer.data, status=status.HTTP_200_OK)


class ApiVeiculoDetail(APIView):
    def get(self, request, pk):
        try:
            veiculo = Veiculo.objects.get(id=pk)
        except Veiculo.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_VEICULO"}, status=status.HTTP_404_NOT_FOUND)

        file_serializer = VeiculoSerializer(veiculo)
        return Response(file_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        try:
            veiculo = Veiculo.objects.get(id=pk)
        except Veiculo.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_USER"}, status=status.HTTP_404_NOT_FOUND)

        file_serializer = VeiculoSerializer(veiculo)
        return Response(file_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        try:
            veiculo = Veiculo.objects.get(id=pk)
        except Veiculo.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_USER"}, status=status.HTTP_404_NOT_FOUND)

        # veiculo.delete()
        return Response({'erro': "HTTP_204_NO_CONTENT_USER_REMOVED"}, status=status.HTTP_204_NO_CONTENT)


# class ApiVeiculoDetail(APIView):
#     queryset = Veiculo.objects.all()
#
#     def get(self, request, pk, pk_2):
#         try:
#             Instituicao.objects.get(id=pk)
#         except Instituicao.DoesNotExist:
#             return Response({'erro': "HTTP_404_NOT_FOUND_INSTITUICAO"}, status=status.HTTP_404_NOT_FOUND)
#         try:
#             veiculo = Veiculo.objects.get(id=pk_2, instituicao=pk)
#         except Veiculo.DoesNotExist:
#             return Response({'erro': "HTTP_404_NOT_FOUND_VEICULO"}, status=status.HTTP_404_NOT_FOUND)
#
#         file_serializer = VeiculoSerializer(veiculo)
#         return Response(file_serializer.data, status=status.HTTP_200_OK)


class APICreateVeiculo(APIView):
    queryset = Veiculo.objects.all()

    def post(self, request, pk):
        try:
            instituicao = Instituicao.objects.get(id=pk)
        except Instituicao.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_INSTITUICAO"}, status=status.HTTP_404_NOT_FOUND)

        file_serializer = CreateVeiculoSerializer(data=request.data)
        if file_serializer.is_valid():
            print(request.data['file'])
            # file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
