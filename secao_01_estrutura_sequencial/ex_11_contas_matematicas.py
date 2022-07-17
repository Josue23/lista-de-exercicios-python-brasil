"""
Exercício 11 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 1) o produto do dobro do primeiro com metade do segundo;
 2) a soma do triplo do primeiro com o terceiro;
 3) o terceiro elevado ao cubo.

 Apresente os resultados com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_11_contas_matematicas
    >>> numeros = ['3.14', '43', '42']
    >>> ex_11_contas_matematicas.input = lambda k: numeros.pop()
    >>> ex_11_contas_matematicas.calcular_formulas()
    O produto do dobro do primeiro com metade do segundo é 1806.00
    A soma do triplo do primeiro com o terceiro é 129.14
    O terceiro elevado ao cubo é 30.96

"""


def calcular_formulas():
    """Escreva aqui em baixo a sua solução"""
    try:
        numero_1 = int(input('Por favor informe um valor inteiro: '))
        numero_2 = int(input('Por favor informe um valor inteiro: '))
        numero_3 = float(input('Por favor informe um valor real : '))
    except EOFError:
        return

    def produto(numero_1: int, numero_2: int):
        '''o produto do dobro do primeiro com metade do segundo . '''
        resultado_produto = (numero_1 * 2) * (numero_2 / 2)
        print(
            f'O produto do dobro do primeiro com metade do segundo é {resultado_produto:.2f}')
    produto(numero_1, numero_2)

    def soma(numero_1: int, numero_3: float):
        '''a soma do triplo do primeiro com o terceiro. '''
        soma_triplo = (numero_1 * 3) + numero_3
        print(
            f'A soma do triplo do primeiro com o terceiro é {soma_triplo:.2f}')
    soma(numero_1, numero_3)

    def cubo(numero_3: float):
        '''o terceiro elevado ao cubo. '''
        numero_3_cubo = numero_3 ** 3
        print(f'O terceiro elevado ao cubo é {numero_3_cubo:.2f}')
    cubo(numero_3)
