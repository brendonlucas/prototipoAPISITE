from django.shortcuts import render, redirect

from instituicao.models import Instituicao
from ordem.models import Ordem
from usuario.models import Usuario
from veiculo.forms import CreateVeiculo
from veiculo.models import Veiculo, TipoVeiculo


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
    ordens = Ordem.objects.filter(veiculo=pk_2, instituicao=pk, status_id__in=[2, 4, 1]).order_by('data_solicitacao')[:5]
    return render(request, 'Details_veiculo.html',
                  {'user': get_user_logged(request), 'veiculo': veiculo, 'instituicao': instituicao,
                   'usuario': get_user(request), 'ordens': ordens})
