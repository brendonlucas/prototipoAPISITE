from django.shortcuts import render, redirect

from instituicao.models import Instituicao
from veiculo.forms import CreateVeiculo
from veiculo.models import Veiculo, TipoVeiculo


def get_user_logged(request):
    return request.user


def add_veiculo(request, pk):
    if request.method == 'POST':
        form = CreateVeiculo(request.POST)

        if form.is_valid():
            instituicao = Instituicao.objects.filter(id=pk).first()
            print("*xczds-*-*-*-*-*-*-*-*-*-*--*--*-*-*-*-*-*-*-*", pk)

            if instituicao:
                dados_form = form.data
                tipo = TipoVeiculo.objects.get(id=form.data['tipo'])

                print(form.data['name'], form.data['QtdCarga'], form.data['placa'], tipo.name, instituicao.nome)

                veiculo = Veiculo(name=form.data['name'], qtd_pessoas=form.data['QtdCarga'], placa=form.data['placa'],
                                  tipo=tipo, instituicao=instituicao).save()
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
                  {'user': get_user_logged(request), 'veiculos': veiculos, 'instituicao': instituicao})


def show_veiculo(request):
    pass
