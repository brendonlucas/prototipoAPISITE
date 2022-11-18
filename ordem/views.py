import datetime
from datetime import date

from django.shortcuts import render, redirect

from instituicao.models import Instituicao, CargosInstituicao
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
    # tu1 = StatusOrdem(nome="Concluido", descricao="Ordem Finalizada").save()
    # tu2 = StatusOrdem(nome="Em Andamento", descricao="Em execução de serviço").save()
    # tu3 = StatusOrdem(nome="Aguardando", descricao="Aguarde").save()
    #
    # o1 = Ordem(solicitante=Usuario.objects.get(id=1), descricao='viajem para umas pessoas ai', qtd_espaco=4,
    #            data_solicitacao=date.today(), origem='Barru duro', destino='jacare do mulato',
    #            instituicao=Instituicao.objects.get(id=1), motorista=Usuario.objects.get(id=3),
    #            status=StatusOrdem.objects.get(id=3), veiculo=Veiculo.objects.get(id=1)).save()
    #
    # o2 = Ordem(solicitante=Usuario.objects.get(id=1), descricao='viajem para umas pessoas ai', qtd_espaco=5,
    #            data_solicitacao=date.today(), origem='Limoeiro', destino='louvradouro',
    #            instituicao=Instituicao.objects.get(id=1), motorista=Usuario.objects.get(id=3),
    #            status=StatusOrdem.objects.get(id=3), veiculo=Veiculo.objects.get(id=3)).save()
    #
    # o3 = Ordem(solicitante=Usuario.objects.get(id=2), descricao='viajem para umas pessoas ai', qtd_espaco=3,
    #            data_solicitacao=date.today(), origem='Jarro batidpo', destino='Lomperina',
    #            instituicao=Instituicao.objects.get(id=2), motorista=Usuario.objects.get(id=5),
    #            status=StatusOrdem.objects.get(id=2), veiculo=Veiculo.objects.get(id=5)).save()
    #
    # o4 = Ordem(solicitante=Usuario.objects.get(id=2), descricao='viajem para umas pessoas ai', qtd_espaco=2,
    #            data_solicitacao=date.today(), origem='lambori', destino='Janaiscabar',
    #            instituicao=Instituicao.objects.get(id=2), status=StatusOrdem.objects.get(id=3)).save()
    #

    ordens = Ordem.objects.filter(instituicao=pk)

    if CargosInstituicao.objects.get(instituicao_id=pk, usuario_id=get_user(request).id).cargo.id in (2, 3):
        ordens = Ordem.objects.filter(instituicao=pk)
    elif CargosInstituicao.objects.get(instituicao_id=pk, usuario_id=get_user(request).id).cargo.id == 4:
        ordens = Ordem.objects.filter(instituicao=pk)

    func_motorista = CargosInstituicao.objects.filter(instituicao_id=pk, cargo_id=4)
    veiculos = Veiculo.objects.filter(instituicao_id=pk)

    finalizados = Ordem.objects.filter(instituicao=pk, status=1)
    aguardando = Ordem.objects.filter(instituicao=pk, status=3)
    andamento_inicio = Ordem.objects.filter(instituicao=pk, status=2)
    andamento_executando = Ordem.objects.filter(instituicao=pk, status=4)

    print(andamento_executando, "---------------------------------------------------------------------------------")

    return render(request, 'show_ordens.html',
                  {'user': get_user_logged(request), 'usuario': get_user(request), 'ordens': ordens,
                   'motoristas': func_motorista, 'veiculos': veiculos, 'ord_finalizdos': finalizados,
                   'aguardando': aguardando, 'andamento_inicio': andamento_inicio,
                   'andamento_executando': andamento_executando})


def show_detail_ordem(request):
    pass


def create_ordem(request, pk):
    if request.method == 'POST':
        form = CreateOrdem(request.POST)
        if form.is_valid():
            dados_form = form.data
            print("-*-*-*-*-*-***-*-*-*-*-*-*-*-*-*-**-*-* ")
            instituicao = Instituicao.objects.filter(id=pk).first()
            a = Ordem(solicitante=get_user(request), descricao=dados_form['descricao'], qtd_espaco=dados_form['carga'],
                      data_solicitacao=dados_form['dataD'], origem=dados_form['destino'], destino=dados_form['destino'],
                      instituicao=instituicao, status=StatusOrdem.objects.get(id=3))
            print(a.solicitante.name, a.descricao, a.qtd_espaco, )
            a.save()
        return redirect('inst_show')


def edit_ordem(request):
    pass


def remove_ordem(request):
    pass


def confirm_ordem(request, pk, pk_2):
    if request.method == 'POST':
        form = ConfirmOrdem(request.POST)
        if form.is_valid():
            dados_form = form.data
            print("-*-*-*-*-*-***-*-*-*-*-*-*-*-*-*-**-*-* ",dados_form)
            print(dados_form['selectVeiculo' + str(pk_2)])
            print(dados_form['selectMotorista' + str(pk_2)])
            print(dados_form['data' + str(pk_2)])
            print(dados_form['horaa' + str(pk_2)])

        return redirect('show_ordens', pk)


def recuse_ordem(request):
    pass
