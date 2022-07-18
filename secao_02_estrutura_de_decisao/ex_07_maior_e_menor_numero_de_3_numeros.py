"""
Exercício 07 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre o maior e o menor deles.

    >>> calcular_maior_de_3_numeros(2,3, 5)
    Maior: 5
    Menor: 2
    >>> calcular_maior_de_3_numeros(-1, -10, -2)
    Maior: -1
    Menor: -10
    >>> calcular_maior_de_3_numeros(-5, 3, 0)
    Maior: 3
    Menor: -5
    >>> calcular_maior_de_3_numeros(7, -14, 15)
    Maior: 15
    Menor: -14
"""


def calcular_maior_de_3_numeros(numero_1, numero_2, numero_3):
    """Escreva aqui em baixo a sua solução"""
    lista_numeros = [numero_1, numero_2, numero_3]
    lista_numeros_ordenada = sorted(lista_numeros)
    menor = lista_numeros_ordenada[0]
    maior = lista_numeros_ordenada[-1]

    print(f'Maior: {maior}')
    print(f'Menor: {menor}')
