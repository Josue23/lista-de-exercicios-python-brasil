from random import randint
"""
Exercício 18 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador
após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas,
para a computação dos votos. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao
número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada.
Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltar a pedir
outro número. Após o final da votação, o programa deverá exibir:

  a. O total de votos computados;
  b. Os númeos e respectivos votos de todos os jogadores que receberam votos;
  c. O percentual de votos de cada um destes jogadores;
  d. O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual
  de votos dados a ele.


    >>> receber_votos(9, 10, 9, 10, 11, 10, 50, 9, 9, 0)
    Enquete: Quem foi o melhor jogador?
    ---------------------------------------------------------------
    Número do jogador (0=fim): 9
    Número do jogador (0=fim): 10
    Número do jogador (0=fim): 9
    Número do jogador (0=fim): 10
    Número do jogador (0=fim): 11
    Número do jogador (0=fim): 10
    Número do jogador (0=fim): 50
    Informe um valor entre 1 e 23 ou 0 para sair!
    Número do jogador (0=fim): 9
    Número do jogador (0=fim): 9
    Número do jogador (0=fim): 0
    ---------------------------------------------------------------
    Resultado da votação:
    ---------------------------------------------------------------
    Foram computados 8 votos.
    ---------------------------------------------------------------
    Jogador Votos           %
    9               4               50.0%
    10              3               37.5%
    11              1               12.5%
    O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.

"""


def retorna_melhor_jogador(votos_dict, mais_votos):
    for jogador, pontos in votos_dict.items():
        if pontos == mais_votos:
            return jogador


def receber_votos(*voto):
    """Escreva aqui em baixo a sua solução"""
    print('Enquete: Quem foi o melhor jogador?')
    print('---------------------------------------------------------------')
    votos_dict = {}
    for v in voto:
        print(f'Número do jogador (0=fim): {v}')
        if v == 0:
            break
        elif v not in range(1, 24):
            print('Informe um valor entre 1 e 23 ou 0 para sair!')
            continue
        votos_dict[v] = votos_dict.get(v, 0) + 1

    soma = sum(votos_dict.values())

    print('---------------------------------------------------------------')
    print('Resultado da votação:')
    print('---------------------------------------------------------------')
    print(f'Foram computados {soma} votos.')
    print('---------------------------------------------------------------')
    print('Jogador Votos           %               ')

    for k, v in votos_dict.items():
        print(f'{k:<2}               {v}               {v / soma * 100:.1f}% ')

    mais_votos = max(votos_dict.values())
    melhor_jogador = retorna_melhor_jogador(votos_dict, mais_votos)

    print(
        f'O melhor jogador foi o número {melhor_jogador}, com {mais_votos} votos, correspondendo a {int(mais_votos / soma * 100)}% do total de votos.')
