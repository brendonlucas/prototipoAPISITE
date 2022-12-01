from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from instituicao.models import Instituicao, Cargo, CargosInstituicao
from usuario.forms import RegistrarUsuarioForm, ChangeCargoForm
from usuario.models import TipoUsuario, Usuario
from veiculo.models import Veiculo, TipoVeiculo


def get_user_logged(request):
    return request.user


def get_user(request):
    return Usuario.objects.get(user=get_user_logged(request))


def show_home_page(request):
    user_logged = get_user_logged(request)
    if user_logged.is_authenticated:
        return render(request, 'home_page/home_page.html', {'user': get_user_logged(request)})
    else:
        return render(request, 'home_page/home_page.html', {'user': get_user_logged(request)})


# @login_required
def pag_home(request):
    # criar_base_dados()
    t = TipoUsuario(nome='admin', descricao='Todo poderioso')
    # id_t = TipoUsuario.objects.get(id=11)
    #
    # u = User.objects.create_user(username="tomas", email="luiz@gmail.com", password="123456", first_name="jhon",
    #                              last_name="travolta")
    # uu = Usuario(name="Thonas travolta", user=u, telefone=99556641, tipo=id_t)
    # uu.save()
    return render(request, 'base.html', {'user': get_user_logged(request)})


def login_pag(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'index.html')


def add_user(request):
    pass


def show_users(request):
    pass


def show_user(request):
    pass


def chang_pass(request):
    pass


def help(request):
    pass


def create_account(request):
    if request.method == 'GET':
        print("-------------------------------------------------")
        return redirect('show_home_page')

    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            print("-----------------------validou------------------------------------")
            dados_form = form.data
            print(dados_form['username'], dados_form['first_name'], dados_form['last_name'], dados_form['email'],
                  dados_form['telefone'],
                  dados_form['password'],
                  dados_form['ConfirmPassword'])
            # tipo = TipoUsuario.objects.get(id=1)
            user = User.objects.create_user(username=dados_form['username'], email=dados_form['email'],
                                            password=dados_form['password'], first_name=dados_form['first_name'],
                                            last_name=dados_form['last_name'], )

            usuario_dados = Usuario(telefone=dados_form['telefone'], user=user, nome=dados_form['username'])
            usuario_dados.save()

            return redirect('show_home_page')

        return redirect('show_home_page')


def show_funcionarios_instituicao(request, pk):
    user = get_user_logged(request)

    funcionarios = CargosInstituicao.objects.filter(instituicao_id=pk)
    cargos = Cargo.objects.all()
    solicitacoes = CargosInstituicao.objects.filter(instituicao_id=pk, cargo_id=5)

    return render(request, 'show_funcionarios.html',
                  {'user': get_user_logged(request), 'funcionarios': funcionarios, 'cargos': cargos,
                   'solicitacoes': solicitacoes})


def change_cargo_user(request, pk):
    if request.method == 'POST':
        form = ChangeCargoForm(request.POST)
        if form.is_valid():
            print("-----------------------validou------------------------------------")
            dados_form = form.data
            print(dados_form['OptionSelectCargo'], pk)
        return redirect('show_funcionario', pk)


def my_profile(request):
    return render(request, 'profile/profile.html', {'user': get_user_logged(request), 'usuario': get_user(request)})


def handler404(request, exception):
    response = render("page_404.html")
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render("page_404.html")
    response.status_code = 500
    return response


def criar_base_dados(request):
    tu1 = TipoUsuario(nome="Criado", descricao="pode tudo").save()
    tu2 = TipoUsuario(nome="Chefe", descricao="Controla as ordens").save()
    tu3 = TipoUsuario(nome="motorista", descricao="Dirige os carro").save()
    tu4 = TipoUsuario(nome="Solicitante", descricao="Pode solicitar ordens").save()

    tv1 = TipoVeiculo(name="Motoca", descricao="Motoca veia de trilha").save()
    tv2 = TipoVeiculo(name="Caminhoneta", descricao="caminhoneta pra levar coisas uma pampa tunada").save()
    tv3 = TipoVeiculo(name="carru", descricao="carrin de 4 portas").save()
    tv4 = TipoVeiculo(name="onibus", descricao="Escolar pra esola").save()

    c1 = Cargo(nome="sem cargo", descricao="").save()
    c2 = Cargo(nome="Adminstrador", descricao="").save()
    c3 = Cargo(nome="gerente", descricao="").save()
    c4 = Cargo(nome="funcionario", descricao="").save()
    c4 = Cargo(nome="Solicitante", descricao="").save()

    # user admins
    userADV1 = User.objects.create_user(username="alan", email="emai5l@gmail.com", password=123456, first_name="alan",
                                        last_name="delon")
    user1 = Usuario(name="alandelon", user=userADV1, telefone=123456789).save()  # adm 1

    userADV2 = User.objects.create_user(username="adori", email="emai4l@gmail.com", password=123456, first_name="adori",
                                        last_name="mano")
    user2 = Usuario(name="Adomiran", user=userADV2, telefone=123456789).save()  # adm 2

    # instituições
    inst1 = Instituicao(nome="Casinha pequena do lago LTDA").save()
    print("------*-*-*-*-*-*-*-*-*-*-*-*-*-*  ", Usuario.objects.get(id=1).name)
    # Instituicao.objects.get(id=1).funcionarios.add(Usuario.objects.get(id=1))
    cargo = Cargo.objects.get(id=2)
    CargosInstituicao(cargo=cargo, usuario=Usuario.objects.get(id=1), instituicao=Instituicao.objects.get(id=1)).save()

    inst2 = Instituicao(nome="Xinforinfula LTDA").save()
    # Instituicao.objects.get(id=2).funcionarios.add(Usuario.objects.get(id=2))
    cargo = Cargo.objects.get(id=2)
    CargosInstituicao(cargo=cargo, usuario=Usuario.objects.get(id=2), instituicao=Instituicao.objects.get(id=2)).save()

    # motoristas
    userADV3 = User.objects.create_user(username="jon", email="emai3l@gmail.com", password=123456,
                                        first_name="jonnnnnn",
                                        last_name="nesbar")
    user3 = Usuario(name="Jhonnesbar", user=userADV3, telefone=123456789).save()  #
    # Instituicao.objects.get(id=1).funcionarios.add(Usuario.objects.get(id=3))
    cargo = Cargo.objects.get(id=4)
    CargosInstituicao(cargo=cargo, usuario=Usuario.objects.get(id=3), instituicao=Instituicao.objects.get(id=1)).save()

    userADV4 = User.objects.create_user(username="jane", email="email2@gmail.com", password=123456,
                                        first_name="janesss",
                                        last_name="temtem")
    user4 = Usuario(name="Janestesis", user=userADV4, telefone=123456789).save()  #
    # Instituicao.objects.get(id=1).funcionarios.add(Usuario.objects.get(id=4))
    cargo = Cargo.objects.get(id=4)
    CargosInstituicao(cargo=cargo, usuario=Usuario.objects.get(id=4), instituicao=Instituicao.objects.get(id=1)).save()

    userADV5 = User.objects.create_user(username="klemi", email="email1@gmail.com", password=123456,
                                        first_name="klemil",
                                        last_name="tomtom")
    user5 = Usuario(name="Klemilton", user=userADV5, telefone=123456789).save()  #
    # Instituicao.objects.get(id=2).funcionarios.add(Usuario.objects.get(id=5))
    cargo = Cargo.objects.get(id=4)
    CargosInstituicao(cargo=cargo, usuario=Usuario.objects.get(id=5), instituicao=Instituicao.objects.get(id=2)).save()

    # chefe de controle
    userADV6 = User.objects.create_user(username="forlan", email="email11@gmail.com", password=123456,
                                        first_name="forlan",
                                        last_name="neston")
    user6 = Usuario(name="Forlan", user=userADV6, telefone=123456789).save()  #
    # Instituicao.objects.get(id=1).funcionarios.add(Usuario.objects.get(id=6))
    cargo = Cargo.objects.get(id=3)
    CargosInstituicao(cargo=cargo, usuario=Usuario.objects.get(id=6), instituicao=Instituicao.objects.get(id=1)).save()

    userADV7 = User.objects.create_user(username="diego", email="email11@gmail.com", password=123456,
                                        first_name="Diego",
                                        last_name="maston")
    user7 = Usuario(name="Diegomar", user=userADV7, telefone=123456789).save()  #
    # Instituicao.objects.get(id=2).funcionarios.add(Usuario.objects.get(id= 7))
    cargo = Cargo.objects.get(id=3)
    CargosInstituicao(cargo=cargo, usuario=Usuario.objects.get(id=7), instituicao=Instituicao.objects.get(id=2)).save()

    # Veiculos
    veiculo1 = Veiculo(name="pampa 4 portas", qtd_pessoas=3, placa="plg123", tipo=TipoVeiculo.objects.get(id=1),
                       instituicao=Instituicao.objects.get(id=1)).save()
    veiculo2 = Veiculo(name="jangada mista", qtd_pessoas=10, placa="plg789", tipo=TipoVeiculo.objects.get(id=2),
                       instituicao=Instituicao.objects.get(id=1)).save()
    veiculo3 = Veiculo(name="Bike kaloy", qtd_pessoas=6, placa="plg528", tipo=TipoVeiculo.objects.get(id=3),
                       instituicao=Instituicao.objects.get(id=1)).save()

    veiculo4 = Veiculo(name="pampa 6 portas", qtd_pessoas=4, placa="plg753", tipo=TipoVeiculo.objects.get(id=1),
                       instituicao=Instituicao.objects.get(id=2)).save()
    veiculo5 = Veiculo(name="Motoca raio laser", qtd_pessoas=2, placa="plg452", tipo=TipoVeiculo.objects.get(id=2),
                       instituicao=Instituicao.objects.get(id=2)).save()
    veiculo6 = Veiculo(name="Limosine preta e azul", qtd_pessoas=5, placa="plg159", tipo=TipoVeiculo.objects.get(id=3),
                       instituicao=Instituicao.objects.get(id=2)).save()

# def criar_base_dados():
#     tu1 = TipoUsuario(nome="Criado", descricao="pode tudo").save()
#     tu2 = TipoUsuario(nome="Chefe", descricao="Controla as ordens").save()
#     tu3 = TipoUsuario(nome="motorista", descricao="Dirige os carro").save()
#     tu4 = TipoUsuario(nome="Solicitante", descricao="Pode solicitar ordens").save()
#
#     tv1 = TipoVeiculo(name="Motoca", descricao="Motoca veia de trilha").save()
#     tv2 = TipoVeiculo(name="Caminhoneta", descricao="caminhoneta pra levar coisas uma pampa tunada").save()
#     tv3 = TipoVeiculo(name="carru", descricao="carrin de 4 portas").save()
#     tv4 = TipoVeiculo(name="onibus", descricao="Escolar pra esola").save()
#
#     # user admins
#     userADV1 = User.objects.create_user(username="alan", email="emai5l@gmail.com", password=123456, first_name="alan",
#                                         last_name="delon")
#     user1 = Usuario(name="alandelon", user=userADV1, telefone=123456789,
#                     tipo=TipoUsuario.objects.get(id=1)).save()  # adm 1
#     userADV2 = User.objects.create_user(username="adori", email="emai4l@gmail.com", password=123456, first_name="adori",
#                                         last_name="mano")
#     user2 = Usuario(name="Adomiran", user=userADV2, telefone=123456789,
#                     tipo=TipoUsuario.objects.get(id=1)).save()  # adm 2
#
#     # instituições
#     inst1 = Instituicao(nome="Casinha pequena do lago LTDA", funcionarios=Usuario.objects.get(id=1)).save()
#     inst2 = Instituicao(nome="Xinforinfula LTDA",funcionarios=Usuario.objects.get(id=2)).save()
#
#     # motoristas
#     userADV3 = User.objects.create_user(username="jon", email="emai3l@gmail.com", password=123456,
#                                         first_name="jonnnnnn",
#                                         last_name="nesbar")
#     user3 = Usuario(name="Jhonnesbar", user=userADV3, telefone=123456789, tipo=TipoUsuario.objects.get(id=3),
#                     instituicao=Instituicao.objects.get(id=1)).save()  #
#     userADV4 = User.objects.create_user(username="jane", email="email2@gmail.com", password=123456,
#                                         first_name="janesss",
#                                         last_name="temtem")
#     user4 = Usuario(name="Janestesis", user=userADV4, telefone=123456789, tipo=TipoUsuario.objects.get(id=3),
#                     instituicao=Instituicao.objects.get(id=1)).save()  #
#     userADV5 = User.objects.create_user(username="klemi", email="email1@gmail.com", password=123456,
#                                         first_name="klemil",
#                                         last_name="tomtom")
#     user5 = Usuario(name="Klemilton", user=userADV5, telefone=123456789, tipo=TipoUsuario.objects.get(id=3),
#                     instituicao=Instituicao.objects.get(id=2)).save()  #
#
#     # chefe de controle
#     userADV6 = User.objects.create_user(username="forlan", email="email11@gmail.com", password=123456,
#                                         first_name="forlan",
#                                         last_name="neston")
#     user6 = Usuario(name="Forlan", user=userADV6, telefone=123456789, tipo=TipoUsuario.objects.get(id=2),
#                     instituicao=Instituicao.objects.get(id=1)).save()  #
#     userADV7 = User.objects.create_user(username="diego", email="email11@gmail.com", password=123456,
#                                         first_name="Diego",
#                                         last_name="maston")
#     user7 = Usuario(name="Diegomar", user=userADV7, telefone=123456789, tipo=TipoUsuario.objects.get(id=2),
#                     instituicao=Instituicao.objects.get(id=2)).save()  #
#
#     # Veiculos
#     veiculo1 = Veiculo(name="pampa 4 portas", qtd_pessoas=3, placa="plg123", tipo=TipoVeiculo.objects.get(id=1),
#                        instituicao=Instituicao.objects.get(id=1)).save()
#     veiculo2 = Veiculo(name="jangada mista", qtd_pessoas=10, placa="plg789", tipo=TipoVeiculo.objects.get(id=2),
#                        instituicao=Instituicao.objects.get(id=1)).save()
#     veiculo3 = Veiculo(name="Bike kaloy", qtd_pessoas=6, placa="plg528", tipo=TipoVeiculo.objects.get(id=3),
#                        instituicao=Instituicao.objects.get(id=1)).save()
#
#     veiculo4 = Veiculo(name="pampa 6 portas", qtd_pessoas=4, placa="plg753", tipo=TipoVeiculo.objects.get(id=1),
#                        instituicao=Instituicao.objects.get(id=2)).save()
#     veiculo5 = Veiculo(name="Motoca raio laser", qtd_pessoas=2, placa="plg452", tipo=TipoVeiculo.objects.get(id=2),
#                        instituicao=Instituicao.objects.get(id=2)).save()
#     veiculo6 = Veiculo(name="Limosine preta e azul", qtd_pessoas=5, placa="plg159", tipo=TipoVeiculo.objects.get(id=3),
#                        instituicao=Instituicao.objects.get(id=2)).save()
