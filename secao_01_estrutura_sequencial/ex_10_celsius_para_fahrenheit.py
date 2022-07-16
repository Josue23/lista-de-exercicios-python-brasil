"""
Exercício 10 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
Mostrar apenas valor inteiro da temperatura

    >>> from secao_01_estrutura_sequencial import ex_10_celsius_para_fahrenheit
    >>> ex_10_celsius_para_fahrenheit.input = lambda k: '0'
    >>> ex_10_celsius_para_fahrenheit.transformar_para_fahrenheit()
    Essa temperatura é de 32 Fahrenheit
    >>> ex_10_celsius_para_fahrenheit.input = lambda k: '21'
    >>> ex_10_celsius_para_fahrenheit.transformar_para_fahrenheit()
    Essa temperatura é de 70 Fahrenheit

"""


def transformar_para_fahrenheit():
    """Escreva aqui em baixo a sua solução"""
    celsius = float(input('Graus em Celsius: '))
    fahrenheit = celsius * 1.8 + 32
    '''ceil equivalent in Python 3 without Math module
    https://stackoverflow.com/questions/32558805/ceil-and-floor-equivalent-in-python-3-without-math-module'''
    fahrenheit = -(-fahrenheit // 1)

    print(f'Essa temperatura é de {fahrenheit} Fahrenheit')
