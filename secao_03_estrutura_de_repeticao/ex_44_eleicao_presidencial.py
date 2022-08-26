"""
Exercício 44 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:

O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.


    >>> apurar_votos('1')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1     100.0%
    2                   Luladrão          0       0.0%
    3                   Dilmanta          0       0.0%
    4                   FHC Isentão       0       0.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      50.0%
    2                   Luladrão          1      50.0%
    3                   Dilmanta          0       0.0%
    4                   FHC Isentão       0       0.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      33.3%
    2                   Luladrão          1      33.3%
    3                   Dilmanta          1      33.3%
    4                   FHC Isentão       0       0.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3', '4')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      25.0%
    2                   Luladrão          1      25.0%
    3                   Dilmanta          1      25.0%
    4                   FHC Isentão       1      25.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3', '4', '5')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      20.0%
    2                   Luladrão          1      20.0%
    3                   Dilmanta          1      20.0%
    4                   FHC Isentão       1      20.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       1      20.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3', '4', '5', '6')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      16.7%
    2                   Luladrão          1      16.7%
    3                   Dilmanta          1      16.7%
    4                   FHC Isentão       1      16.7%
    -------------------------------------------------------------------
    5                   Votos Nulos       1      16.7%
    6                   Votos Brancos     1      16.7%
    >>> apurar_votos('1', '2', '3', '4', '5', '6', '5', '6', '5', '6', '5', '6', '5', '6', '5', '6', '5', '6')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1       5.6%
    2                   Luladrão          1       5.6%
    3                   Dilmanta          1       5.6%
    4                   FHC Isentão       1       5.6%
    -------------------------------------------------------------------
    5                   Votos Nulos       7      38.9%
    6                   Votos Brancos     7      38.9%


"""
from collections import Counter


def apurar_votos(*votos):
    """Escreva aqui em baixo a sua solução"""
    # Counter({'5': 7, '6': 7, '1': 1, '2': 1, '3': 1, '4': 1})
    soma_votos = Counter(votos)

    candidatos_nome_id_dict = {
        'Bostonaro': 1,
        'Luladrão': 2,
        'Dilmanta': 3,
        'FHC Isentão': 4,
        'Votos Nulos': 5,
        'Votos Brancos': 6,
    }

    soma_candidatos_votos_dict = {}

    # popula dados no dict soma_candidatos_votos_dict
    for k, v in soma_votos.items():
        for nome, id in candidatos_nome_id_dict.items():
            if int(k) == id:
                soma_candidatos_votos_dict[nome] = v

    total_votos = [int(el) for el in soma_candidatos_votos_dict.values()]
    total_votos = sum(total_votos)

    mensagens_list = []
    print('Código do Candidato Nome do Candidato Votos Porcentagem sobre total')
    for k, v in soma_votos.items():
        for nome, id in candidatos_nome_id_dict.items():
            nome_voto = soma_candidatos_votos_dict.get(nome, 0)
            percento = (100 / total_votos * nome_voto)
            #tamanho_str = len(str(percento))
            tamanho_str = len(str(f'{percento:.1f}'))
            #tamanho_str = f'{tamanho_str:.1f}'
            # for i in range(3, 6):
            if nome == 'Votos Nulos':

                mensagens_list.append(
                    '-------------------------------------------------------------------')
            if tamanho_str == 3:
                mensagens_list.append(
                    f'{id:<19} {nome:<17} {nome_voto:<5}   {percento:<{tamanho_str}.1f}%')

            elif tamanho_str == 4:
                mensagens_list.append(
                    f'{id:<19} {nome:<17} {nome_voto:<5}  {percento:<{tamanho_str}.1f}%')
            else:
                mensagens_list.append(
                    f'{id:<19} {nome:<17} {nome_voto:<5} {percento:-{tamanho_str}.1f}%')
        if id == 6:
            break
    [print(mensagem) for mensagem in mensagens_list]
