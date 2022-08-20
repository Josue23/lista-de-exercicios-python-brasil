"""
Exercício 37 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> from secao_03_estrutura_de_repeticao import ex_37_senso_de_academia
    >>> entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 162.0 centímetros
    Media de peso dos clientes: 81.0 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 177.0 centímetros
    Media de peso dos clientes: 80.5 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.0 centímetros
    Media de peso dos clientes: 90.2 kilos

"""


def mostra_cliente_mais_alto(lista_de_dicionarios_de_clientes, maior_altura):
    for dicionario in lista_de_dicionarios_de_clientes:
        if int(dicionario['altura']) == maior_altura:
            cliente_mais_alto = dicionario['nome']
            return cliente_mais_alto


def mostra_cliente_mais_baixo(lista_de_dicionarios_de_clientes, menor_altura):
    for dicionario in lista_de_dicionarios_de_clientes:
        if int(dicionario['altura']) == menor_altura:
            cliente_mais_baixo = dicionario['nome']
            return cliente_mais_baixo


def mostra_cliente_mais_magro(lista_de_dicionarios_de_clientes, menor_peso):
    for dicionario in lista_de_dicionarios_de_clientes:
        if int(dicionario['peso']) == menor_peso:
            cliente_mais_magro = dicionario['nome']
            return cliente_mais_magro


def mostra_cliente_mais_gordo(lista_de_dicionarios_de_clientes, maior_peso):
    for dicionario in lista_de_dicionarios_de_clientes:
        if int(dicionario['peso']) == maior_peso:
            cliente_mais_gordo = dicionario['nome']
            return cliente_mais_gordo


def rodar_senso():
    """Escreva aqui em baixo a sua solução"""
    lista_de_dicionarios_de_clientes = []
    cliente_lista = []
    cliente_lista_1 = []
    dados_cliente_lista = ['nome', 'altura', 'peso']

    dado = ''
    while dado != '0':
        for count, dado in enumerate(dados_cliente_lista, start=1):
            cliente_lista.append(dado)
            dado = input(f'{dado}: '.capitalize())
            cliente_lista_1.append(dado)
            if count == len(dados_cliente_lista):
                count = 1
                lista_de_dicionarios_de_clientes.append(
                    dict(zip(cliente_lista, cliente_lista_1)))
            elif count == 1 and '0' in dado:
                cliente_lista.pop()
                cliente_lista_1.pop()
                break

    lista_de_alturas = []
    lista_de_pesos = []

    for dicionario in lista_de_dicionarios_de_clientes:
        lista_de_alturas.append(dicionario['altura'])
        lista_de_pesos.append(dicionario['peso'])

    # converte os itens da lista para inteiro
    lista_de_alturas = [int(item) for item in lista_de_alturas]
    lista_de_pesos = [int(item) for item in lista_de_pesos]

    maior_altura = max(lista_de_alturas)
    menor_altura = min(lista_de_alturas)

    maior_peso = max(lista_de_pesos)
    menor_peso = min(lista_de_pesos)

    media_alturas = sum(lista_de_alturas) / len(lista_de_alturas)
    media_pesos = sum(lista_de_pesos) / len(lista_de_pesos)

    cliente_mais_alto = mostra_cliente_mais_alto(
        lista_de_dicionarios_de_clientes, maior_altura)

    cliente_mais_baixo = mostra_cliente_mais_baixo(
        lista_de_dicionarios_de_clientes, menor_altura)

    cliente_mais_magro = mostra_cliente_mais_magro(
        lista_de_dicionarios_de_clientes, menor_peso)

    cliente_mais_gordo = mostra_cliente_mais_gordo(
        lista_de_dicionarios_de_clientes, maior_peso)

    print(
        f'Cliente mais alto: {cliente_mais_alto}, com {int(maior_altura)} centímetros')
    print(
        f'Cliente mais baixo: {cliente_mais_baixo}, com {int(menor_altura)} centímetros')
    print(
        f'Cliente mais magro: {cliente_mais_magro}, com {int(menor_peso)} kilos')
    print(
        f'Cliente mais gordo: {cliente_mais_gordo}, com {int(maior_peso)} kilos')
    print('--------------------------------------------------')
    print(f'Media de altura dos clientes: {media_alturas:.1f} centímetros')
    print(f'Media de peso dos clientes: {media_pesos:.1f} kilos')
