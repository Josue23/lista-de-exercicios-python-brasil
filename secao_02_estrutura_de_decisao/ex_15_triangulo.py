"""
Exercício 15 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

    >>> classificar_triangulo(2, 3, 4)
    'Triângulo Escaleno'
    >>> classificar_triangulo(2, 2, 3)
    'Triângulo Isósceles'
    >>> classificar_triangulo(2, 2, 2)
    'Triângulo Equilátero'
    >>> classificar_triangulo(2, 2, 5)
    'Não é um triângulo'
    >>> classificar_triangulo(5, 2, 2)
    'Não é um triângulo'
    >>> classificar_triangulo(2, 5, 2)
    'Não é um triângulo'

"""


def classificar_triangulo(lado_a: float, lado_b: float, lado_c: float):
    """Escreva aqui em baixo a sua solução"""
    condicao_1 = lado_a + lado_b > lado_c
    condicao_2 = lado_a + lado_c > lado_b
    condicao_3 = lado_b + lado_c > lado_a
    lista_de_condicoes = [condicao_1, condicao_2, condicao_3]

    if all(lista_de_condicoes):
        lista_de_lados_set = set([lado_a, lado_b, lado_c])

        if len(lista_de_lados_set) == 1:  # três lados iguais
            return 'Triângulo Equilátero'
        elif len(lista_de_lados_set) == 2:  # dois lados iguais
            return 'Triângulo Isósceles'
        else:  # três lados diferentes
            return 'Triângulo Escaleno'
    else:
        return 'Não é um triângulo'
