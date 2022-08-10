import re
from functools import reduce
from operator import mul
"""
Exercício 32 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120

    >>> calcular_fatorial(1)
    Fatorial de 1:
    1! = 1 = 1
    >>> calcular_fatorial(2)
    Fatorial de 2:
    2! = 2 . 1 = 2
    >>> calcular_fatorial(3)
    Fatorial de 3:
    3! = 3 . 2 . 1 = 6
    >>> calcular_fatorial(4)
    Fatorial de 4:
    4! = 4 . 3 . 2 . 1 = 24
    >>> calcular_fatorial(5)
    Fatorial de 5:
    5! = 5 . 4 . 3 . 2 . 1 = 120

"""


def calcular_fatorial(n: int):
    """Escreva aqui em baixo a sua solução"""
    intervalo = list(range(1, n + 1))  # [1, 2, 3, 4, 5]
    fatorial = reduce(mul, intervalo)  # 120
    fatores = [i for i in intervalo[::-1]]  # [5, 4, 3, 2, 1]

    mensagem = f'{n}! = {fatores} = {fatorial}'  # 5! = [5, 4, 3, 2, 1] = 120
    mensagem = re.sub(r'[\[\]]', '', mensagem)
    mensagem = re.sub(', ', ' . ', mensagem)
    print(mensagem)  # 5! = 5 . 4 . 3 . 2 . 1 = 120
