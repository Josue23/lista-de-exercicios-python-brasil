"""
Exercício 49 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que mostre os n termos da Série a seguir:

    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

    Imprima no final a soma da série.

    ----------------------------------
    | EXEMPLO                         |
    ----------------------------------
    | ENTRADA:                        |
    | n = 5                           |
    | SAIDA:                          |
    | S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 |
    | soma = 3.393650793650793        |
    ----------------------------------


    >>> imprimir_serie(5)
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9
    soma = 3.393650793650793
    >>> imprimir_serie(7)
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + 6/11 + 7/13
    soma = 4.477566877566877
    >>> imprimir_serie(3)
    S = 1/1 + 2/3 + 3/5
    soma = 2.2666666666666666
    >>> imprimir_serie(9)
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + 6/11 + 7/13 + 8/15 + 9/17
    soma = 5.540311975606093

"""


def imprimir_serie(n):  # 5
    """Escreva aqui em baixo a sua solução"""
    dividendos_list = list(range(1, n + 1))  # [1, 2, 3, 4, 5]

    divisor = 1
    divisores_list = []
    while len(divisores_list) < n:
        divisores_list.append(divisor)
        divisor += 2
    # divisores_list [1, 3, 5, 7, 9]

    s = ''
    soma = 0
    # popula dados nas variáveis s e soma a partir das listas dividendos_list e divisores_list
    for x, y in zip(dividendos_list, divisores_list):
        s += f'{x}/{y} + '
        soma += x / y
    s = s[:-3]  # '1/1 + 2/3 + 3/5 + 4/7 + 5/9'

    print(f'S = {s}')  # S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9
    print(f'soma = {soma}')  # soma = 3.393650793650793
