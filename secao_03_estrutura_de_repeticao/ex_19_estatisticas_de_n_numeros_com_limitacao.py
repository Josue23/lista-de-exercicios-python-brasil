"""
Exercício 19 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

    >>> calcular_estatisticas()
    'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    >>> calcular_estatisticas(1)
    'Maior valor: 1. Menor valor: 1. Soma: 1'
    >>> calcular_estatisticas(1, 2)
    'Maior valor: 2. Menor valor: 1. Soma: 3'
    >>> calcular_estatisticas(1, 2, -1)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, -10)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1001)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1198)
    'Somente números de 0 a 1000 são permitidos'

"""


def calcular_estatisticas(*numeros) -> str:
    """Escreva aqui em baixo a sua solução"""
    soma = 0
    if len(numeros) == 0:
        mensagem = f'Maior valor: não existe. Menor valor: não existe. Soma: {soma}'
    else:
        [numeros_list := list(numeros), numeros_list.sort()]
        [menor := numeros_list[0], maior := numeros_list[-1]]
        for numero in numeros_list:
            if menor < 0 or maior > 1000:
                (mensagem := 'Somente números de 0 a 1000 são permitidos')
                break
            else:
                [soma := soma + n for n in numeros_list]
                (mensagem :=
                 f'Maior valor: {maior}. Menor valor: {menor}. Soma: {soma}')
                break

    return mensagem
