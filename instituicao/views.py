import string
import random
from django.shortcuts import render, redirect

from django.contrib import messages
from instituicao.forms import JoinRoomForm, CreateIntituicaoForm
from instituicao.models import Instituicao, Cargo, CargosInstituicao
from usuario.models import Usuario


def get_user_logged(request):
    return request.user


def get_user(request):
    return Usuario.objects.get(user=get_user_logged(request))


def show_instituicao(request):
    # inst = Instituicao.objects.all().filter(funcionarios = get_user(request).id)

    inst = Instituicao.objects.filter(funcionarios=get_user(request).id)
    print("-------------------------------------------------", inst)
    return render(request, 'inst_options.html',
                  {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicoes': inst})


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
            inst = Instituicao.objects.get(codigo = codigo_inst)
            inst.funcionarios.add(get_user(request))


        messages.success(request, 'Criado com sucesso!')
        return redirect('inst_show')
