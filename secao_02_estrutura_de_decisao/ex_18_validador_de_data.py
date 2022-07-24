from secao_02_estrutura_de_decisao.ex_17_ano_bissexto import eh_ano_bissexto

"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""
    if '/' in data:
        lista_de_datas = data.split('/')
        lista_de_datas = [int(data) for data in lista_de_datas]
        dia, mes, ano = [x for x in lista_de_datas]

        if eh_ano_bissexto(ano):
            if mes == 2:
                if dia in range(1, 30):
                    return 'Data válida'
                else:
                    return 'Data inválida'
        else:
            if mes == 2:
                if dia in range(1, 29):
                    return 'Data válida'
                else:
                    return 'Data inválida'

        if dia in range(1, 32):
            if mes in range(1, 13):
                if ano in range(-5000, 5000):
                    return 'Data válida'
            else:
                return 'Data inválida'

    else:
        return 'Data inválida'
