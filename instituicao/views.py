import string
import random
from django.shortcuts import render, redirect

from instituicao.forms import JoinRoomForm, CreateIntituicaoForm
from instituicao.models import Instituicao, Cargo, CargosInstituicao
from usuario.models import Usuario


def get_user_logged(request):
    return request.user


def get_user(request):
    return Usuario.objects.get(user=get_user_logged(request))


def show_instituicao(request):
    inst_cargo = (CargosInstituicao.objects.filter(cargo=2, usuario=get_user(request)).order_by('instituicao_id'))
    entradas = (CargosInstituicao.objects.filter(cargo__in=[1,3,4,5], usuario=get_user(request)).order_by('instituicao_id'))

    return render(request, 'inst_options.html',
                  {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicoes': inst_cargo, 'entradas': entradas})


def create_instituicao(request):
    if request.method == 'POST':
        form = CreateIntituicaoForm(request.POST)
        if form.is_valid():
            dados_form = form.data
            codigo_inst = ''.join(
                random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
            print(dados_form['NameInst'], "-*-*-*-*-*-***-*-*-*-*-*-*-*-*-*-**-*-* ", codigo_inst)
            inst = Instituicao(nome=dados_form['NameInst'], codigo=codigo_inst).save()
            instituicao = Instituicao.objects.get(codigo=codigo_inst)
            cargo = Cargo.objects.get(id=2)
            cargoNaIns = CargosInstituicao(cargo=cargo, usuario=get_user(request), instituicao=instituicao).save()

        return redirect('inst_show')


def entrar_intituicao(request):
    if request.method == 'POST':
        form = JoinRoomForm(request.POST)
        if form.is_valid():
            dados_form = form.data
            codigo_inst = dados_form['InputCode']
            user = get_user(request)
            instituicao = Instituicao.objects.filter(codigo=codigo_inst).first()
            if instituicao:
                if CargosInstituicao.objects.filter(usuario=user, instituicao=instituicao).first() is None:
                    cargo = Cargo.objects.get(id=5)
                    CargosInstituicao(cargo=cargo, usuario=user, instituicao=instituicao).save()

        return redirect('inst_show')

    elif request.method == 'GET':
        return redirect('inst_show')


def recuse_solicitacao(request, pk):
    s_request = CargosInstituicao.objects.filter(id=pk).first()
    if s_request:
        id_instituicao = s_request.instituicao.id
        if s_request.cargo.id == 5:
            s_request.delete()
        else:
            print("bad requestttt")

        return redirect('show_funcionario', id_instituicao)
    return redirect('pag')
