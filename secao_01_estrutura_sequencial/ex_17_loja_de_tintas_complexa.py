"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    area_a_ser_pintada = float(
        input('Por favor informe a área em metros quadrados: '))
    area_a_ser_pintada *= 1.1
    litros_por_metro = 6
    litros_por_lata = 18
    litros_por_galao = 3.6
    litros_de_tinta = int(-(-area_a_ser_pintada // litros_por_metro))

    def apenas_latas(area_a_ser_pintada, litros_por_metro, litros_por_lata, litros_de_tinta):
        # litros_de_tinta = area_a_ser_pintada / litros_por_metro
        # litros_de_tinta = int(-(-area_a_ser_pintada // litros_por_metro))
        # litros_por_lata = 18
        '''math.ceil without importing math module
        https://stackoverflow.com/questions/32558805/ceil-and-floor-equivalent-in-python-3-without-math-module'''
        latas_de_tinta = int(-(-litros_de_tinta // litros_por_lata))
        sobra_de_tinta_em_litros = latas_de_tinta * litros_por_lata - litros_de_tinta
        valor_total = latas_de_tinta * 80
        print(f'Você deve comprar {litros_de_tinta} litros de tinta.')
        print(
            f'Você pode comprar {latas_de_tinta} lata(s) de 18 litros a um custo de R$ {valor_total}. Vão sobrar {sobra_de_tinta_em_litros:.1f} litro(s) de tinta.')
    apenas_latas(area_a_ser_pintada, litros_por_metro,
                 litros_por_lata, litros_de_tinta)

    def apenas_galoes(area_a_ser_pintada, litros_de_tinta, litros_por_galao):
        '''math.ceil without importing math module
        https://stackoverflow.com/questions/32558805/ceil-and-floor-equivalent-in-python-3-without-math-module'''
        # litros_por_galao = 3.6
        galoes_de_tinta = int(-(-litros_de_tinta // litros_por_galao))
        sobra_de_tinta_em_litros = galoes_de_tinta * litros_por_galao - litros_de_tinta

        valor_total = int(galoes_de_tinta * 25)

        print(
            f'Você pode comprar {galoes_de_tinta} lata(s) de 3.6 litros a um custo de R$ {valor_total}. Vão sobrar {sobra_de_tinta_em_litros:.1f} litro(s) de tinta.')
    apenas_galoes(area_a_ser_pintada, litros_de_tinta, litros_por_galao)

    def latas_e_galoes(area_a_ser_pintada, litros_por_metro, litros_de_tinta, litros_por_lata, litros_por_galao):
        if area_a_ser_pintada >= 108:
            latas_de_tinta = litros_de_tinta // litros_por_lata
        else:
            latas_de_tinta = 0

        '''math.ceil without importing math module
        https://stackoverflow.com/questions/32558805/ceil-and-floor-equivalent-in-python-3-without-math-module'''
        # galoes_de_tinta = -(-area_em_metros_restante // litros_de_tinta)
        litros_faltantes = litros_de_tinta % litros_por_lata
        galoes_de_tinta = int(-(-litros_faltantes // litros_por_galao))
        # print(f'galoes_de_tinta: {galoes_de_tinta}')

        # galoes_de_tinta = area_em_metros_restante // litros_de_tinta

        sobra_de_tinta_em_litros = (latas_de_tinta * litros_por_lata) + \
            (galoes_de_tinta * litros_por_galao) - litros_de_tinta
        valor_latas = latas_de_tinta * 80
        valor_galoes = galoes_de_tinta * 25
        valor_total = valor_latas + valor_galoes
        print(f'Para menor custo, você pode comprar {latas_de_tinta} lata(s) de {litros_por_lata} litros e {galoes_de_tinta} galão(ões) de {litros_por_galao} litros a um custo de R$ {valor_total}. Vão sobrar {sobra_de_tinta_em_litros:.1f} litro(s) de tinta.')

    latas_e_galoes(area_a_ser_pintada, litros_por_metro,
                   litros_de_tinta, litros_por_lata, litros_por_galao)
