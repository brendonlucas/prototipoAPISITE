import datetime
from datetime import date
from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from instituicao.models import *
from ordem.OrdemSerializer import *
from ordem.forms import CreateOrdem, ConfirmOrdem
from ordem.models import Ordem, StatusOrdem
from usuario.models import Usuario
from veiculo.models import Veiculo

from django.core.paginator import Paginator


def get_user_logged(request):
    return request.user


def get_user(request):
    return Usuario.objects.get(user=get_user_logged(request))


def show_ordems(request, pk):
    instituicao = Instituicao.objects.get(id=pk)
    aguardando = Ordem.objects.filter(instituicao=pk, status=3)

    return render(request, 'show_ordens.html',
                  {'user': get_user_logged(request), 'usuario': get_user(request), 'aguardando': aguardando,
                   'instituicao': instituicao})


def show_detail_ordem(request):
    pass


def create_ordem(request, pk):
    if request.method == 'GET':
        instituicao = Instituicao.objects.get(id=pk)
        return render(request, 'Forms/form_ordem.html',
                      {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicao': instituicao, })

    if request.method == 'POST':
        form = CreateOrdem(request.POST)
        if form.is_valid():
            dados_form = form.data
            instituicao = Instituicao.objects.filter(id=pk).first()
            if dados_form['TypeT'] == 1:  # 1 = pessoas / 2 = carga
                carga = dados_form['carga']
            else:
                carga = 0

            a = Ordem(solicitante=get_user(request), descricao=dados_form['descricao'],
                      data_solicitacao=datetime.date.today(), horario_requirido=dados_form['horaD'],
                      qtd_espaco=carga, data_solicitado=dados_form['dataD'],
                      origem=dados_form['saida'], destino=dados_form['destino'],
                      instituicao=instituicao, status=StatusOrdem.objects.get(id=3))
            a.save()
            messages.success(request, 'Criado com sucesso!')
        return redirect('inst_show')


def edit_ordem(request):
    pass


def remove_ordem(request):
    pass


def confirm_ordem(request, pk, pk_2):
    if request.method == 'GET':
        instituicao = Instituicao.objects.get(id=pk)
        ordem = Ordem.objects.get(id=pk_2)
        veiculos = Veiculo.objects.filter(instituicao_id=pk)
        motoristas = Instituicao.objects.get(id=pk).funcionarios.all().filter(cargo_id=4)
        print("MOtoristas aqui--------------------------------------", veiculos)
        ids_veiculos = []
        for k in range(len(veiculos)):
            ids_veiculos.append(veiculos[k].id)

        ids_motorista = []
        for k in range(len(motoristas)):
            ids_motorista.append(motoristas[k].id)

        return render(request, 'Forms/gerenciar_ordem.html',
                      {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicao': instituicao,
                       'ordem': ordem, 'veiculos': veiculos, 'motoristas': motoristas, 'ids_veiculos': ids_veiculos,
                       'ids_motorista': ids_motorista})

    if request.method == 'POST':
        form = ConfirmOrdem(request.POST)
        if form.is_valid():
            ordem = Ordem.objects.get(id=pk_2)
            dados_form = form.data
            ordem.veiculo = Veiculo.objects.get(id=dados_form['veiculo'])
            ordem.motorista = Usuario.objects.get(id=dados_form['motorista'])
            ordem.data_marcada = dados_form['data']
            ordem.horario_marcado = dados_form['hora']
            ordem.status = StatusOrdem.objects.get(id=2)
            ordem.save()

            print("-*-*-*-*-*-***-*-*-*-*-*-*-*-*-*-**-*-* ", )
            print(dados_form['veiculo'], dados_form['motorista'], dados_form['data'], dados_form['hora'])
            print("-*-*-*-*-*-***-*-*-*-*-*-*-*-*-*-**-*-* ", )

            messages.success(request, 'Ordem confirmada como sucesso!')

            return redirect('show_ordens_detail', pk, pk_2)


def recuse_ordem(request):
    pass


def show_ordens_detail(request, pk, pk_2):
    if request.method == 'GET':
        ordem = Ordem.objects.get(id=pk_2)
        instituicao = Instituicao.objects.get(id=pk)
        return render(request, 'Forms/detail_ordem.html',
                      {'user': get_user_logged(request), 'usuario': get_user(request), 'ordem': ordem,
                       'instituicao': instituicao})


def show_ordems_and_ini(request, pk):
    instituicao = Instituicao.objects.get(id=pk)
    if get_user(request).cargo.id == 4:
        andamento_inicio = Ordem.objects.filter(instituicao=pk, status=2, motorista=get_user(request).id)
    else:
        andamento_inicio = Ordem.objects.filter(instituicao=pk, status=2)

    return render(request, 'table_ordens_And_Ini.html',
                  {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicao': instituicao,
                   'andamento_inicio': andamento_inicio, })


def show_ordems_and_cur(request, pk):
    instituicao = Instituicao.objects.get(id=pk)
    if get_user(request).cargo.id == 4:
        andamento_executando = Ordem.objects.filter(instituicao=pk, status=4, motorista=get_user(request).id)
    else:
        andamento_executando = Ordem.objects.filter(instituicao=pk, status=4)
    return render(request, 'table_ordens_And_Cur.html',
                  {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicao': instituicao,
                   'andamento_executando': andamento_executando, })


def show_ordems_final(request, pk):
    instituicao = Instituicao.objects.get(id=pk)
    if get_user(request).cargo.id == 4:
        finalizados = Ordem.objects.filter(instituicao=pk, status=1, motorista=get_user(request).id)
    else:
        finalizados = Ordem.objects.filter(instituicao=pk, status=1)
    return render(request, 'table_ordens_finalizados.html',
                  {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicao': instituicao,
                   'ord_finalizdos': finalizados, })


def confirm_omi(request, pk, pk_2):
    if request.method == 'GET':
        ordem = Ordem.objects.get(id=pk_2)
        instituicao = Instituicao.objects.get(id=pk)
        return render(request, 'Forms/Form_And_Ini.html',
                      {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicao': instituicao,
                       'ordem': ordem, })

    if request.method == 'POST':
        ordem = Ordem.objects.get(id=pk_2)
        if ordem.status.id == 2:
            ordem.status = StatusOrdem.objects.get(id=4)
            ordem.save()
            return redirect('show_ordens_and_cur', pk)
        else:
            # pagina erro
            pass


def confirm_OMF(request, pk, pk_2):
    if request.method == 'GET':
        ordem = Ordem.objects.get(id=pk_2)
        instituicao = Instituicao.objects.get(id=pk)
        return render(request, 'Forms/Form_And_Cur.html',
                      {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicao': instituicao,
                       'ordem': ordem, })

    if request.method == 'POST':
        ordem = Ordem.objects.get(id=pk_2)
        if ordem.status.id == 4:
            ordem.status = StatusOrdem.objects.get(id=1)
            ordem.save()
            return redirect('show_ordens_final', pk)
        else:
            # pagina erro
            pass


def show_ordens_motorista(request, pk):
    try:
        ordens = Ordem.objects.filter(instituicao=pk)
    except Instituicao.DoesNotExist:
        ordens = None

    instituicao = Instituicao.objects.get(id=pk)
    return render(request, 'Forms/detail_ordem.html',
                  {'user': get_user_logged(request), 'usuario': get_user(request), 'ordem': ordens,
                   'instituicao': instituicao})


# APIIIIIIIIIIIIIIIIIIIIIII
class APIGetAllOrdem(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, *args, **kwargs):
        try:
            instituicao = Instituicao.objects.get(id=pk)
        except Instituicao.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_Instituicao"}, status=status.HTTP_404_NOT_FOUND)

        ordens = Ordem.objects.filter(instituicao=pk)
        serializer_context = {
            'request': request,
        }
        file_serializer = OrdemSerializer(ordens, many=True, context=serializer_context)

        return Response(file_serializer.data, status=status.HTTP_200_OK)


class APIGetOrdenVeiculo(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, *args, **kwargs):
        try:
            veiculo = Veiculo.objects.get(id=pk)
        except Veiculo.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_veiculo"}, status=status.HTTP_404_NOT_FOUND)

        ordens = Ordem.objects.filter(veiculo=pk)
        serializer_context = {
            'request': request,
        }
        file_serializer = OrdemSerializer(ordens, many=True, context=serializer_context)

        return Response(file_serializer.data, status=status.HTTP_200_OK)


class APIGetOrdem(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, *args, **kwargs):
        try:
            ordem = Ordem.objects.get(id=pk)
        except Ordem.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_ORDEM"}, status=status.HTTP_404_NOT_FOUND)
        serializer_context = {
            'request': request,
        }
        file_serializer = OrdemSerializer(ordem, context=serializer_context)
        return Response(file_serializer.data, status=status.HTTP_200_OK)


class APICreateOrdem(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk, *args, **kwargs):
        try:
            instituicao = Instituicao.objects.get(id=pk)
        except Instituicao.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_Instituicao"}, status=status.HTTP_404_NOT_FOUND)

        data = CreateOrdemSerializer(data=request.data)
        if data.is_valid():
            # solicitante = Usuario.objects.get(id=data['solicitante'].value)

            if data['qtd_espaco'].value > 0:  # 1 = pessoas / 2 = carga
                carga = data['qtd_espaco'].value
            else:
                carga = 0

            solicitante = get_user(request)

            ordem = Ordem(solicitante=solicitante, descricao=data['descricao'].value, origem=data['origem'].value,
                          destino=data['destino'].value, data_solicitacao=datetime.date.today(),
                          horario_requirido=data['horario_requirido'].value, qtd_espaco=carga,
                          data_solicitado=data['data_solicitado'].value, instituicao=instituicao,
                          status=StatusOrdem.objects.get(id=3))
            ordem.save()

            return Response(data.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'erro': "HTTP_400_BAD_REQUEST"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        pass

    def delete(self, request, pk, *args, **kwargs):
        try:
            ordem = Ordem.objects.get(id=pk)
        except Ordem.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_Ordem"}, status=status.HTTP_404_NOT_FOUND)

        ordem.delete()
        return Response({'erro': "HTTP_204_NO_CONTENT"}, status=status.HTTP_204_NO_CONTENT)


class APIGConfirmOrdem(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, pk, *args, **kwargs):
        try:
            ordem = Ordem.objects.get(id=pk)
        except Ordem.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_Ordem"}, status=status.HTTP_404_NOT_FOUND)

        data = GConfirmOrdemSerializer(data=request.data)
        if data.is_valid():
            print(request.data)
            ordem = Ordem.objects.get(id=pk)
            dados_form = data
            ordem.veiculo = Veiculo.objects.get(id=dados_form['veiculo'].value)
            ordem.motorista = Usuario.objects.get(id=dados_form['motorista'].value)
            ordem.data_marcada = dados_form['data'].value
            ordem.horario_marcado = dados_form['hora'].value
            ordem.status = StatusOrdem.objects.get(id=2)
            ordem.save()

            return Response(data.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'erro': "HTTP_400_BAD_REQUEST"}, status=status.HTTP_400_BAD_REQUEST)


class APIGInicioOrdem(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, pk, *args, **kwargs):
        try:
            ordem = Ordem.objects.get(id=pk)
        except Ordem.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_Instituicao"}, status=status.HTTP_404_NOT_FOUND)
        data = GInicioOrdemSerializer(data=request.data)
        if data.is_valid():
            return Response(data.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'erro': "HTTP_400_BAD_REQUEST"}, status=status.HTTP_400_BAD_REQUEST)


class APIGFinalizeOrdem(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, pk, *args, **kwargs):
        try:
            ordem = Ordem.objects.get(id=pk)
        except Ordem.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_Instituicao"}, status=status.HTTP_404_NOT_FOUND)
        data = GFinalizeOrdemSerializer(data=request.data)
        if data.is_valid():
            return Response(data.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'erro': "HTTP_400_BAD_REQUEST"}, status=status.HTTP_400_BAD_REQUEST)
