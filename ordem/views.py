import datetime
from datetime import date
from django.contrib import messages
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
    instituicao = Instituicao.objects.get(id=pk)

    veiculos = Veiculo.objects.filter(instituicao_id=pk)

    aguardando = Ordem.objects.filter(instituicao=pk, status=3)

    return render(request, 'show_ordens.html',
                  {'user': get_user_logged(request), 'usuario': get_user(request), 'ordens': ordens,
                   'veiculos': veiculos, 'aguardando': aguardando,
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
                      qtd_espaco=carga, data_solicitado=dados_form['dataD'],
                      origem=dados_form['destino'], destino=dados_form['destino'],
                      instituicao=instituicao, status=StatusOrdem.objects.get(id=3))

            print("-*-*-*-*-*-***-*-*-*-*-*-*-*-*-*-**-*-* ")
            print(a.solicitante.name, a.descricao, a.qtd_espaco, )
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
            pass
            # dados_form = form.data
            # print("-*-*-*-*-*-***-*-*-*-*-*-*-*-*-*-**-*-* ", dados_form)
            # print(dados_form['selectVeiculo' + str(pk_2)])
            # print(dados_form['selectMotorista' + str(pk_2)])
            # print(dados_form['data' + str(pk_2)])
            # print(dados_form['horaa' + str(pk_2)])
            messages.success(request, 'Ordem confirmada como sucesso!')

            return redirect('show_ordens_detail', pk, pk_2)


def recuse_ordem(request):
    pass


def show_ordens_detail(request, pk, pk_2):
    if request.method == 'GET':
        ordem = Ordem.objects.get(id=pk_2)
        instituicao = Instituicao.objects.get(id=pk)
        return render(request, 'Forms/detail_ordem.html',
                      {'user': get_user_logged(request), 'usuario': get_user(request), 'ordem': ordem,'instituicao': instituicao })
    return None


def show_ordems_and_ini(request, pk):
    instituicao = Instituicao.objects.get(id=pk)
    andamento_inicio = Ordem.objects.filter(instituicao=pk, status=2)
    return render(request, 'table_ordens_And_Ini.html',
                  {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicao': instituicao,
                   'andamento_inicio': andamento_inicio, })


def show_ordems_and_cur(request, pk):
    instituicao = Instituicao.objects.get(id=pk)
    andamento_executando = Ordem.objects.filter(instituicao=pk, status=4)
    return render(request, 'table_ordens_And_Cur.html',
                  {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicao': instituicao,
                   'andamento_executando': andamento_executando, })


def show_ordems_final(request, pk):
    instituicao = Instituicao.objects.get(id=pk)
    finalizados = Ordem.objects.filter(instituicao=pk, status=1)
    return render(request, 'table_ordens_finalizados.html',
                  {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicao': instituicao,
                   'ord_finalizdos': finalizados, })
