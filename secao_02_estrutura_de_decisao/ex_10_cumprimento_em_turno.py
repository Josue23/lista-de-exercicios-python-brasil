"""
Exercício 10 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

    >>> cumprimentar('M')
    'Bom dia!'
    >>> cumprimentar('m')
    'Bom dia!'
    >>> cumprimentar('V')
    'Boa tarde!'
    >>> cumprimentar('v')
    'Boa tarde!'
    >>> cumprimentar('N')
    'Boa noite!'
    >>> cumprimentar('n')
    'Boa noite!'
    >>> cumprimentar('X')
    'Valor Inválido!'

"""


def cumprimentar(turno: str):
    """Escreva aqui em baixo a sua solução"""
    turnos = ['M', 'm', 'V', 'v', 'N', 'n', 'X']
    if turno in turnos:
        if turno in ['M', 'm']:
            cumprimento = 'Bom dia!'
        elif turno in ['V', 'v']:
            cumprimento = 'Boa tarde!'
        elif turno in ['N', 'n']:
            cumprimento = 'Boa noite!'
        elif turno == 'X':
            cumprimento = 'Valor Inválido!'

        return cumprimento
