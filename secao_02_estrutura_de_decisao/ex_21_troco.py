"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 1 real e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""


def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)


def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""

    opcoes_de_notas = [100, 50, 10, 5, 1]

    notas_100, restante = divmod(valor, 100)
    notas_50, restante = divmod(restante, 50)
    notas_10, restante = divmod(restante, 10)
    notas_5, restante = divmod(restante, 5)
    notas_1 = restante

    lista_notas_int = [notas_100, notas_50, notas_10, notas_5, notas_1]
    lista_notas_str = ['notas' if nota !=
                       1 else 'nota' for nota in lista_notas_int]

    mensagem = ''
    for count, value in enumerate(lista_notas_int):
        if value > 0:
            mensagem += f'{lista_notas_int[count]} {lista_notas_str[count]} de R$ {opcoes_de_notas[count]}, '

    mensagem = rreplace(mensagem, ', ', '', 1)

    return f"{rreplace(mensagem, ', ', ' e ', 1)}"
