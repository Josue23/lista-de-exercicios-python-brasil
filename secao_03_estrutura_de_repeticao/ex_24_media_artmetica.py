from _pydecimal import Decimal
"""
Exercício 24 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o mostre a média aritmética de N notas.

    >>> calcular_media()
    'É necessária ao menos uma nota para calcular a média'
    >>> calcular_media(1)
    1
    >>> calcular_media(1, 3)
    2
    >>> calcular_media(1, 3, 3)
    2.3333333333333335

"""


def calcular_media(*notas) -> float:
    """Escreva aqui em baixo a sua solução"""
    if len(notas) == 0:
        return 'É necessária ao menos uma nota para calcular a média'
    else:
        for nota in notas:
            (soma := nota)
        result = str(soma / len(notas))

    '''remove os zeros ao lado direito do ponto decimal, depois remove o ponto decimal'''
    result = result.rstrip('0').rstrip('.') if '.' in result else result

    return result
