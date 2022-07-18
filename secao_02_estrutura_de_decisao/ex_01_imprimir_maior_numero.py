"""
Exercício 01 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça dois números e imprima o maior deles.

    >>> maior_de_dois_numeros(2,3)
    3
    >>> maior_de_dois_numeros(-1,-10)
    -1
    >>> maior_de_dois_numeros(-5,3)
    3
    >>> maior_de_dois_numeros(7,-14)
    7
"""


def maior_de_dois_numeros(x, y):
    """Escreva aqui em baixo a sua solução"""
    numero_1 = int(input('Por favor informe um númweo: '))
    numero_2 = int(input('Por favor informe um númweo: '))
    if numero_1 > numero_2:
        print(f'O maior número é: {numero_1}')
    else:
        print(f'O maior número é: {numero_2}')
