from random import randint
"""
Exercício 13 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule e MOSTRE A MÉDIA ANUAL das temperaturas e MOSTRE TODAS AS TEMPERATURAS ACIMA DA MÉDIA ANUAL,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

-as temperaturas só serão dadas em inteiro
-todos os meses do ano serão passados à funçao, começando de janeiro e terminando em dezembro.
 Todos seguidos de sua temperatura mensal

(Funçoês recomendadas para estudo:
    - .ljust()
    - enumerate()
    - sum()
    - len()


    >>> from secao_04_exercicios_lista import ex_13_media_de_temperaturas_anual

    >>> meses_vs_temperaturas = ['25', '33', '19', '16', '15', '20', '25', '29', '25', '27', '33', '30']
    >>> ex_13_media_de_temperaturas_anual.input = lambda k: meses_vs_temperaturas.pop()
    >>> ex_13_media_de_temperaturas_anual.temperaturas_acima_da_media()
    Média anual: 24.75 Graus
     1 - Janeiro:       30°
     2 - Fevereiro:     33°
     3 - Março:         27°
     4 - Abril:         25°
     5 - Maio:          29°
     6 - Junho:         25°
    11 - Novembro:      33°
    12 - Dezembro:      25°
    >>> meses_vs_temperaturas = ['25', '33', '19', '16', '15', '20', '25', '29', '25', '27', '33', '35']
    >>> ex_13_media_de_temperaturas_anual.input = lambda k: meses_vs_temperaturas.pop()
    >>> ex_13_media_de_temperaturas_anual.temperaturas_acima_da_media()
    Média anual: 25.17 Graus
     1 - Janeiro:       35°
     2 - Fevereiro:     33°
     3 - Março:         27°
     5 - Maio:          29°
    11 - Novembro:      33°

"""


def temperaturas_acima_da_media():
    """Escreva aqui sua solução: """
    meses_lista = ['Janeiro;', 'Fevereiro:', 'Março:', 'Abril:', 'Maio:', 'Junho:',
                   'Julho:', 'Agosto:', 'Setembro:', 'Outubro:', 'Novembro:', 'Dezembro:']
    temperaturas_lista = [randint(0, 40) for mes in range(1, 13)]
    print(f'meses_vs_temperaturas {temperaturas_lista}')

    media_anual = sum(temperaturas_lista) / len(temperaturas_lista)
    print(f'Média anual: {media_anual:.2f} Graus')

    # concatena as duas listas meses_lista e temperaturas_lista e armazena na lista meses_temperaturas
    meses_temperaturas = list(zip(meses_lista, temperaturas_lista))
    for indice, temp in enumerate(meses_temperaturas, start=1):
        if temp[1] > media_anual:
            print(f'{indice:<2} - {temp[0]:<12} {temp[1]}')
