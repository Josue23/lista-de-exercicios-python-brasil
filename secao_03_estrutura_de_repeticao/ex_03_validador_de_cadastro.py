"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia e valide as seguintes informações:

  Nome: maior que 3 caracteres;
  Idade: entre 0 e 150;
  Salário: maior que zero;
  Sexo: 'f' ou 'm';
  Estado Civil: 's', 'c', 'v', 'd';

    >>> cadastrar_usuario('Renzo', 39, 2000, 'm', 'c')
    Cadastro realizado com sucesso
    >>> cadastrar_usuario('Gil', 1, 2000.05, 'f', 's')
    Cadastro realizado com sucesso
    >>> cadastrar_usuario('Gi', 150, 2000.05, 'f', 'v')
    Erro: o nome precisa ter 3 letras ou mais, não pode ser Gi
    >>> cadastrar_usuario('Ti', -1, 2000.05, 'f', 'v')
    Erro: o nome precisa ter 3 letras ou mais, não pode ser Ti
    Erro: a idade precisa estar entre 0 e 150, não pode ser -1
    >>> cadastrar_usuario('Mi', 151, 0, 'f', 'v')
    Erro: o nome precisa ter 3 letras ou mais, não pode ser Mi
    Erro: a idade precisa estar entre 0 e 150, não pode ser 151
    Erro: o salário precisa ser positivo, não pode ser 0
    >>> cadastrar_usuario('Mi', 151, 0, 'z', 'v')
    Erro: o nome precisa ter 3 letras ou mais, não pode ser Mi
    Erro: a idade precisa estar entre 0 e 150, não pode ser 151
    Erro: o salário precisa ser positivo, não pode ser 0
    Erro: o sexo precisa ser "m" ou "f", não pode ser "z"
    >>> cadastrar_usuario('Mi', 151, 0, 't', 'p')
    Erro: o nome precisa ter 3 letras ou mais, não pode ser Mi
    Erro: a idade precisa estar entre 0 e 150, não pode ser 151
    Erro: o salário precisa ser positivo, não pode ser 0
    Erro: o sexo precisa ser "m" ou "f", não pode ser "t"
    Erro: o estado civil precisa ser "s", "c", "v" ou "d", não pode ser "p"

"""


def cadastrar_usuario(nome: str, idade: int, salario: float, sexo: str, estado_civil: str):
    """Escreva aqui em baixo a sua solução"""
    cadastro_dict_bool = {
        nome: len(nome) > 2,
        idade: idade in range(151),
        salario: salario > 0,
        sexo: sexo in ['f', 'm'],
        estado_civil: estado_civil in ['s', 'c', 'v', 'd']
    }
    dados_lista = ['nome', 'idade', 'salário', 'sexo', 'estado civil']

    zipped = zip(cadastro_dict_bool.items(), dados_lista)

    for (valor_dado_usuario, booleano), dado_usuario in zipped:
        # if booleano == False:
        if not booleano:
            if dado_usuario == dados_lista[0]:
                print(
                    f'Erro: o {dado_usuario} precisa ter 3 letras ou mais, não pode ser {valor_dado_usuario}')
            elif dado_usuario == dados_lista[1]:
                print(
                    f'Erro: a {dado_usuario} precisa estar entre 0 e 150, não pode ser {valor_dado_usuario}')
            elif dado_usuario == dados_lista[2]:
                print(
                    f'Erro: o {dado_usuario} precisa ser positivo, não pode ser {valor_dado_usuario}')
            elif dado_usuario == dados_lista[3]:
                print(
                    f'Erro: o {dado_usuario} precisa ser "m" ou "f", não pode ser "{valor_dado_usuario}"')
            elif dado_usuario == dados_lista[4]:
                print(
                    f'Erro: o {dado_usuario} precisa ser "s", "c", "v" ou "d", não pode ser "{valor_dado_usuario}"')

    cadastro_valores_lista = list(cadastro_dict_bool.values())
    if all(p is True for p in cadastro_valores_lista):
        print('Cadastro realizado com sucesso')
