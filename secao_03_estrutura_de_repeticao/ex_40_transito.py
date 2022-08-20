"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""


def calcula_menor_indice(*cidades):
    lista_de_indices = []
    for cidade in cidades:
        lista_de_indices.append(cidade[2] / cidade[1] * 1000)
    lista_de_indices_sorted = sorted(lista_de_indices)
    return lista_de_indices_sorted[0]


def calcula_maior_indice(*cidades):
    lista_de_indices = []
    for cidade in cidades:
        lista_de_indices.append(cidade[2] / cidade[1] * 1000)
    lista_de_indices_sorted = sorted(lista_de_indices)
    return lista_de_indices_sorted[-1]


def mostra_cidade_menor_indice(*cidades, menor_indice):
    for cidade in cidades:
        if menor_indice == cidade[2] / cidade[1] * 1000:
            nome_cidade_menor_indice = cidade[0]
    return nome_cidade_menor_indice


def mostra_cidade_maior_indice(*cidades, maior_indice):
    for cidade in cidades:
        if maior_indice == cidade[2] / cidade[1] * 1000:
            nome_cidade_maior_indice = cidade[0]
    return nome_cidade_maior_indice


def calcula_media_veiculos(*cidades):
    soma = 0
    for cidade in cidades:
        soma += cidade[1]
    media = int(soma / len(cidades))
    return media


def calcula_media_acidentes(*cidades):
    cidades_com_menos_de_150_000_carros = []
    for cidade in cidades:
        if cidade[1] <= 150_000:
            cidades_com_menos_de_150_000_carros.append(cidade[2])
    media = sum(cidades_com_menos_de_150_000_carros) / \
        len(cidades_com_menos_de_150_000_carros)
    return media


def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""

    menor_indice = calcula_menor_indice(*cidades)
    nome_cidade_menor_indice = mostra_cidade_menor_indice(
        *cidades, menor_indice=menor_indice)

    maior_indice = calcula_maior_indice(*cidades)
    nome_cidade_maior_indice = mostra_cidade_maior_indice(
        *cidades, maior_indice=maior_indice)

    media_veiculos_por_cidade = calcula_media_veiculos(*cidades)
    media_acidentes = calcula_media_acidentes(*cidades)

    print(
        f'O maior índice de acidentes é de {nome_cidade_maior_indice}, com {maior_indice:.1f} acidentes por mil carros.')
    print(
        f'O menor índice de acidentes é de {nome_cidade_menor_indice}, com {menor_indice:.1f} acidentes por mil carros.')
    print(
        f'O média de veículos por cidade é de {media_veiculos_por_cidade}.')
    print(
        f'A média de acidentes total nas cidades com menos de 150 mil carros é de {media_acidentes:.1f} acidentes.')
