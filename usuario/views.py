from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from rest_framework import status, generics
from rest_framework.views import APIView

from instituicao.InstituicaoSerializer import InstituicaoSerializer
from instituicao.models import Instituicao, Cargo, CargosInstituicao
from usuario.UsuarioSerializer import UsuarioSerializer, CreateUserSerializer
from usuario.forms import RegistrarUsuarioForm, ChangeCargoForm, RegisterNewUserForm
from usuario.models import TipoUsuario, Usuario
from veiculo.models import Veiculo, TipoVeiculo

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


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
    return render(request, 'base.html', {'user': get_user_logged(request)})


def create_account(request):
    if request.method == 'GET':
        return redirect('show_home_page')
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            dados_form = form.data
            user = User.objects.create_user(username=dados_form['username'], email=dados_form['email'],
                                            password=dados_form['password'], first_name=dados_form['first_name'],
                                            last_name=dados_form['last_name'], )
            cargo = TipoUsuario.objects.get(id=1)
            usuario_dados = Usuario(telefone=dados_form['telefone'], user=user, name=dados_form['username'],
                                    cargo=cargo)
            usuario_dados.save()
            return redirect('show_home_page')
        return redirect('show_home_page')


def create_account_func(request, pk):
    if request.method == 'GET':
        instituicao = Instituicao.objects.get(id=pk)

        return render(request, 'form_add_user.html',
                      {'user': get_user_logged(request), 'instituicao': Instituicao.objects.get(id=pk), })

    if request.method == 'POST':
        form = RegisterNewUserForm(request.POST)
        if form.is_valid():
            dados_form = form.data
            print("---------------------------------------------------------")
            print(dados_form['username'], dados_form['email'], dados_form['password'], dados_form['first_name'],
                  dados_form['last_name'], dados_form['full_name'])
            print(request.POST.getlist('havepass'), dados_form['cargo'])
            print("---------------------------------------------------------")

            senha = ""
            if len(request.POST.getlist('havepass')) > 0:
                print("tem senha")
                senha = dados_form['password']
            else:
                senha = "123456789"  # make_default_pass

            user = User.objects.create_user(username=dados_form['username'], email=dados_form['email'],
                                            password=senha, first_name=dados_form['first_name'],
                                            last_name=dados_form['last_name'], )

            cargo = TipoUsuario.objects.get(id=dados_form['cargo'])
            usuario_dados = Usuario(user=user, name=dados_form['username'], cargo=cargo)
            usuario_dados.save()

            inst = Instituicao.objects.get(id=pk)
            usuario_inst = Usuario.objects.get(user=user.id)
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-", usuario_inst.name)
            if inst:
                inst.funcionarios.add(usuario_inst)

            messages.success(request, 'Criado com sucesso!')
            return redirect('show_funcionario', pk)

        messages.error(request, 'Dados invalidos!')
        return redirect('register_new_user', pk)


def show_funcionarios_instituicao(request, pk):
    user = get_user_logged(request)

    funcionarios = Instituicao.objects.get(id=pk).funcionarios.all()
    print("--------------------------------------------", funcionarios[0])
    return render(request, 'show_funcionarios.html',
                  {'user': get_user_logged(request), 'funcionarios': funcionarios,
                   'instituicao': Instituicao.objects.get(id=pk)})


def change_cargo_user(request, pk):
    if request.method == 'POST':
        form = ChangeCargoForm(request.POST)
        if form.is_valid():
            print("-----------------------validou------------------------------------")
            dados_form = form.data
            print(dados_form['OptionSelectCargo'], pk)
        return redirect('show_funcionario', pk)


def my_profile(request):
    instituicao = Instituicao.objects.filter(funcionarios__id=get_user(request).id).first()
    if not instituicao:
        instituicao = None

    return render(request, 'profile/profile.html',
                  {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicao': instituicao})


def handler404(request, exception):
    response = render(request, "pages_extra/page_404.html")
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    instituicao = Instituicao.objects.get(id=9)
    messages.error(request, "não encontrado")
    response = render(request, 'pages_extra/data_not_found.html',
                      {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicao': instituicao})
    response.status_code = 500
    return response


def handler401(request, *args, **argv):
    instituicao = Instituicao.objects.get(id=9)
    messages.error(request, "não encontrado")
    response = render(request, 'pages_extra/data_not_found.html',
                      {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicao': instituicao})
    response.status_code = 401
    return response


def criar_base_dados(request):
    tv1 = TipoVeiculo(name="Moto", descricao="Motoca veia de trilha").save()
    tv2 = TipoVeiculo(name="Caminhão", descricao="caminhoneta pra levar coisas uma pampa tunada").save()
    tv3 = TipoVeiculo(name="carro", descricao="carrin de 4 portas").save()
    tv4 = TipoVeiculo(name="Onibus", descricao="Escolar pra esola").save()

    c2 = TipoUsuario(nome="Adminstrador", descricao="").save()
    c3 = TipoUsuario(nome="gerente", descricao="").save()
    c4 = TipoUsuario(nome="funcionario", descricao="").save()
    c1 = TipoUsuario(nome="motorista", descricao="").save()

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


def error_data(request):
    instituicao = Instituicao.objects.get(id=9)
    messages.error(request, "não encontrado")
    render(request, 'pages_extra/data_not_found.html',
           {'user': get_user_logged(request), 'usuario': get_user(request), 'instituicao': instituicao})


def error404(request):
    return render(request, 'pages_extra/page_404.html')


# APIIIIIIIIIIII

class APICreateUser(APIView):
    queryset = Usuario.objects.all()

    def post(self, request, *args, **kwargs):
        data = CreateUserSerializer(data=request.data)
        if data.is_valid():
            # if not User.objects.filter(username=data['user']['username'].value).first():
            # user = User.objects.create_user(username=data['user']['username'].value,
            #                                 password=data['user']['password'].value,
            #                                 email=data['user']['email'].value,
            #                                 first_name=data['user']['first_name'].value,
            #                                 last_name=data['user']['last_name'].value)
            # funcionario = Usuario(nome=data['name'].value, telefone=data['telefone'].value, user=user)
            # funcionario.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        else:
            return Response("HTTP_400_BAD_REQUEST", status=status.HTTP_400_BAD_REQUEST)


class APIGetUserDetail(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            user = Usuario.objects.get(id=pk)
        except Usuario.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_USER"}, status=status.HTTP_404_NOT_FOUND)

        file_serializer = UsuarioSerializer(user)
        return Response(file_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        try:
            user = Usuario.objects.get(id=pk)
        except Usuario.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_USER"}, status=status.HTTP_404_NOT_FOUND)

        file_serializer = UsuarioSerializer(user)
        return Response(file_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        try:
            user = Usuario.objects.get(id=pk)
        except Usuario.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_USER"}, status=status.HTTP_404_NOT_FOUND)

        # user.delete()
        return Response({'erro': "HTTP_204_NO_CONTENT_USER_REMOVED"}, status=status.HTTP_204_NO_CONTENT)


class APIGetAllFuncInst(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            funcionarios = Instituicao.objects.get(id=pk).funcionarios.all()
        except Instituicao.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND_INSTITUICAO"}, status=status.HTTP_404_NOT_FOUND)

        file_serializer = UsuarioSerializer(funcionarios, many=True)
        return Response(file_serializer.data, status=status.HTTP_200_OK)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        dados_funcionario = get_object_or_404(Usuario, user=user.id)
        instituicao = Instituicao.objects.filter(funcionarios__id=Usuario.objects.get(user_id=user.id).id).first()
        if instituicao:
            # instituicao = get_object_or_404(Instituicao, funcionarios__id=Usuario.objects.get(user_id=user.id).id)
            inst_serialize = InstituicaoSerializer(instituicao,context={'request': request}).data
        else:
            inst_serialize = None
        usu = UsuarioSerializer(dados_funcionario)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'dados': usu.data,
            'instituicao': inst_serialize
        })
