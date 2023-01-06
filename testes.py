import requests


def main():
    data = {}
    data_user = {"username": "teste2", "password": "123456789"}

    data_user_Complement = {"username": "leomarcos", "password": "123456789", "email": "leomarcos@email.com",
                            "first_name": "leo", "last_name": "marcos"}
    data_user_C = {"name": "leo", "telefone": 99554411, "user": data_user_Complement}

    # v = requests.get('http://127.0.0.1:8000/API/9/veiculos/')
    # p = requests.post('http://127.0.0.1:8000/api-token-auth/', json=data_user)
    # userC = requests.post('http://127.0.0.1:8000/API/create_user/', json=data_user_C)
    # data_put = {'telefone': 123123123}
    # userC = requests.put('http://127.0.0.1:8000/15/API/APIGetUserDetail/', json=data_put)
    # print(userC.text)
    # print(x.text)
    # print(len(x.json()))
    # for part in x.json():
    #     print(part + ':', x.json()[part])

    # data_put = {'solicitante': 12, 'data_solicitado': '2023/01/21', 'horario_requirido': '21:16',
    #             'descricao': "descrição chamativa aqui", 'qtd_espaco': 5, 'origem': 'casa grande',
    #             'destino': 'casa pequena'}
    #
    # fields = ('solicitante', 'data_solicitado', 'horario_requirido', 'descricao', 'qtd_espaco', 'origem', 'destino')
    # data_put = {'solicitante': 12, 'data_solicitado': '2023-01-21', 'horario_requirido': '21:16',
    #             'descricao': "descrição chamativa aqui", 'qtd_espaco': 5, 'origem': 'casa grande',
    #             'destino': 'casa pequena'}
    # userC = requests.post('http://127.0.0.1:8000/9/API/APICreateOrdem/', json=data_put)
    # print(userC.text)
    # confirm ordem 1
    # data_put = {"motorista": 14, "veiculo": 15, "data_marcada": '2023-01-23', "horario_marcado": '21:20'}
    # userC = requests.put('http://127.0.0.1:8000/19/API/APIGConfirmOrdem/', json=data_put)
    # confirm ordem 2
    # data_put = {}
    # userC = requests.put('http://127.0.0.1:8000/19/API/APIGInicioOrdem/', json=data_put)

    userC = requests.delete('http://127.0.0.1:8000/23/API/APICreateOrdem/')
    print(userC.status_code)


if __name__ == '__main__':
    main()
