import string
import random
from django.shortcuts import render, redirect

from django.contrib import messages
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from instituicao.InstituicaoSerializer import *
from instituicao.forms import JoinRoomForm, CreateIntituicaoForm
from instituicao.models import Instituicao, Cargo, CargosInstituicao
from usuario.models import Usuario


def get_user_logged(request):
    return request.user


def get_user(request):
    return Usuario.objects.get(user=get_user_logged(request))


def show_instituicao(request):
    # inst = Instituicao.objects.all().filter(funcionarios = get_user(request).id)
    try:
        inst = Instituicao.objects.get(funcionarios=get_user(request).id)
    except Instituicao.DoesNotExist:
        inst = None

    print("-------------------------------------------------", inst)
    return render(request, 'inst_options.html',
                  {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicao': inst})


def create_instituicao(request):
    if request.method == 'POST':
        form = CreateIntituicaoForm(request.POST)
        if form.is_valid():
            dados_form = form.data
            while True:
                codigo_inst = ''.join(
                    random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
                tem_inst = Instituicao.objects.filter(codigo=codigo_inst).first()
                if tem_inst is None:
                    break

            print(dados_form['NameInst'], "-*-*-*-*-*-***-*-*-*-*-*-*-*-*-*-**-*-* ", codigo_inst)

            Instituicao(nome=dados_form['NameInst'], codigo=codigo_inst).save()
            inst = Instituicao.objects.get(codigo=codigo_inst)
            inst.funcionarios.add(get_user(request))

        messages.success(request, 'Criado com sucesso!')
        return redirect('inst_show')


def config_relatorios(request):
    if request.method == 'GET':

        try:
            inst = Instituicao.objects.get(funcionarios=get_user(request).id)
        except Instituicao.DoesNotExist:
            inst = None

        return render(request, 'conf_relatorios.html',
                      {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicao': inst})



# APIIIIIIIIIIIIIIIIIIIII

class APIGerentInstituicao(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, pk, *args, **kwargs):
        try:
            instituicao = Instituicao.objects.get(id=pk)
        except Instituicao.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_Instituicao"}, status=status.HTTP_404_NOT_FOUND)
        serializer_context = {
            'request': request,
        }
        data_serializer = InstituicaoSerializer(instituicao, context=serializer_context)
        return Response(data_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, pk, *args, **kwargs):
        try:
            instituicao = Instituicao.objects.get(id=pk)
        except Instituicao.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_Instituicao"}, status=status.HTTP_404_NOT_FOUND)

        instituicao.delete()
        return Response({'fim': "removido"}, status=status.HTTP_200_OK)

class APIGInstituicao(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        data = CreateInstituicaoSerializer(data=request.data)
        if data.is_valid():
            while True:
                codigo_inst = ''.join(
                    random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
                tem_inst = Instituicao.objects.filter(codigo=codigo_inst).first()
                if tem_inst is None:
                    break

            print(data['nome'].value, "-*-*-*-*-*-***-*-*-*-*-*-*-*-*-*-**-*-* ", codigo_inst)

            Instituicao(nome=data['nome'].value, codigo=codigo_inst).save()
            inst = Instituicao.objects.get(codigo=codigo_inst)
            inst.funcionarios.add(get_user(request))
            inst.save()
            inst = Instituicao.objects.get(codigo=codigo_inst)
            serializer_context = {
                'request': request,
            }
            inst_serialize = InstituicaoSerializer(inst, context=serializer_context)

            return Response(inst_serialize.data, status=status.HTTP_201_CREATED)
        else:
            print(data.data)
            return Response({'erro': "HTTP_400_BAD_REQUEST"}, status=status.HTTP_400_BAD_REQUEST)


