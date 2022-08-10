"""
Exercício 33 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

Mostre a média com uma casa decimal.

    >>> calcular_estatisticas()
    'Maior temperatura: não existe. Menor temperatura: não existe. Média: não existe'
    >>> calcular_estatisticas(1)
    'Maior temperatura: 1. Menor temperatura: 1. Média: 1.0'
    >>> calcular_estatisticas(1, 2)
    'Maior temperatura: 2. Menor temperatura: 1. Média: 1.5'
    >>> calcular_estatisticas(1, 2, -1)
    'Maior temperatura: 2. Menor temperatura: -1. Média: 0.7'


"""


def calcular_maior(temperatura, maior):
    if temperatura > maior:
        maior = temperatura
    return maior


def calcular_menor(temperatura, menor):
    if temperatura < menor:
        menor = temperatura
    return menor


def calcular_media(temperaturas):
    return sum(temperaturas) / len(temperaturas)


def calcular_estatisticas(*temperaturas) -> str:
    """Escreva aqui em baixo a sua solução"""
    if len(temperaturas) == 0:
        return 'Maior temperatura: não existe. Menor temperatura: não existe. Média: não existe'
    else:
        maior = temperaturas[0]
        menor = temperaturas[0]
        media = calcular_media(temperaturas)
        for temperatura in temperaturas[1:]:
            maior = calcular_maior(temperatura, maior)
            menor = calcular_menor(temperatura, menor)

    return f'Maior temperatura: {maior}. Menor temperatura: {menor}. Média: {media:.1f}'
