"""
Exercício 18 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
Arredonde o tempo em minutos

    >>> from secao_01_estrutura_sequencial import ex_18_tempo_de_download
    >>> numeros =['50', '2500']
    >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
    >>> ex_18_tempo_de_download.calcular_tempo_de_download()
    O tempo aproximado do Download é: 7 minuto(s)
    >>> numeros =['100', '2500']
    >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
    >>> ex_18_tempo_de_download.calcular_tempo_de_download()
    O tempo aproximado do Download é: 3 minuto(s)

"""


def calcular_tempo_de_download():
    """Escreva aqui em baixo a sua solução"""
    tamanho_arquivo_em_megabytes = float(
        input('Por favor informe o tamanho do arquivo em megabytes: '))
    velocidade_link_internet = float(
        input('Por favor informe a velocidade da internet: '))
    tamanho_arquivo_em_bits = tamanho_arquivo_em_megabytes * 1.000 * 1.000 * 8

    tempo_aproximado_download_em_segundos = tamanho_arquivo_em_bits / \
        velocidade_link_internet
    minutos = tempo_aproximado_download_em_segundos / 60
    minutos = round(minutos)

    print(f'O tempo aproximado do Download é: {minutos} minuto(s)')
