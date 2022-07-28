# from secao_02_estrutura_de_decisao.ex_22_par_ou_impar import decidir_se_eh_par_ou_impar
from secao_02_estrutura_de_decisao.ex_02_positivo_ou_negativo import positivo_ou_negativo
from secao_02_estrutura_de_decisao.ex_23_inteiro_ou_decimal import decidir_se_eh_inteiro_ou_decimal
"""
Exercício 24 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
  par ou ímpar;
  positivo ou negativo;
  inteiro ou decimal.

Mostre o restultado com duas casas decimais

    >>> fazer_operacao_e_classificar(2, 3, '+')
    Resultado: 5.00
    Número é impar, positivo e inteiro.
    >>> fazer_operacao_e_classificar(-4, 2, '/')
    Resultado: -2.00
    Número é par, negativo e inteiro.
    >>> fazer_operacao_e_classificar(0, 2, '*')
    Resultado: 0.00
    Número é par, neutro e inteiro.
    >>> fazer_operacao_e_classificar(-3.14, 2, '*')
    Resultado: -6.28
    Número é negativo e decimal.
    >>> fazer_operacao_e_classificar(3.14, 2, '-')
    Resultado: 1.14
    Número é positivo e decimal.
"""


def decidir_se_eh_par_ou_impar(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    if decidir_se_eh_inteiro_ou_decimal(valor) == 'Inteiro':
        numero_par = valor % 2 == 0
        par_ou_impar = 'par, ' if numero_par else 'impar, '
    else:
        return None

    return par_ou_impar


# def positivo_ou_negativo(n):
#     """Escreva aqui em baixo a sua solução"""
#     resultado = 'positivo' if n > 0 else 'negativo' if n < 0 else 'neutro'
#     return resultado


# def decidir_se_eh_inteiro_ou_decimal(valor: str) -> str:
#     """Escreva aqui em baixo a sua solução"""
#     resultado = 'Inteiro' if float(valor) // 1 == float(valor) else 'Decimal'
#     return resultado


def fazer_operacao_e_classificar(n_1: float, n_2: float, operacao: str):
    """Escreva aqui em baixo a sua solução"""
    operacoes = ['+', '/', '*', '-']
    if operacao in operacoes:
        resultado = n_1+n_2 if operacao == '+' \
            else n_1-n_2 if operacao == '-' \
            else n_1 * n_2 if operacao == '*' \
            else n_1/n_2

    print(f'Resultado: {resultado:.2f}')

    resultados = [decidir_se_eh_par_ou_impar(resultado), positivo_ou_negativo(
        resultado), decidir_se_eh_inteiro_ou_decimal(resultado).lower()]

    mensagem = 'Número é '
    for item in resultados:
        if item is not None:
            if item in ['negativo', 'neutro', 'positivo']:
                item += ' e '
            mensagem += item
    mensagem += '.'
    print(f'{mensagem}')
