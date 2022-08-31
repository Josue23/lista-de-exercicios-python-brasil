import re
"""
Exercício 08 da seção de funções da Python Brasil:
https://wiki.python.org.br/ExerciciosFuncoes

Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

    >>> imprimir_qtde_digitos_do_inteiro(11235813213455)
    14

    >>> imprimir_qtde_digitos_do_inteiro(14916253649)
    11

    >>> imprimir_qtde_digitos_do_inteiro(-273)
    3

    >>> imprimir_qtde_digitos_do_inteiro(3.14159265359)
    O valor informado não é um inteiro

    >>> imprimir_qtde_digitos_do_inteiro(29011998)
    8

    >>> imprimir_qtde_digitos_do_inteiro(0)
    1

"""


def imprimir_qtde_digitos_do_inteiro(inteiros: int) -> str:
    # ini_string = "123abcjw:, .@! eiw"
    inteiros = str(inteiros)  # converte para str

    # remove todos os caracteres que não são inteiros
    result = re.sub('[^0-9]+', '', inteiros)
    print(len(result))
