"""
Exercício 09 da seção de strings da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
e indique se é um número válido ou inválido através da validação dos dígitos verificadores
e dos caracteres de formatação.

    >>> validar_cpf('734.289.251-30')
    True


    >>> validar_cpf('732.289.294-10')
    False


    >>> validar_cpf('44986045040')
    True


    >>> validar_cpf('6693171008')
    False


"""


def primeiro_digito_verificador(cpf):
    # Valida o primeiro dígito verificador
    sum_of_products = sum(int(a) * int(b)
                          for a, b in zip(cpf[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if int(cpf[9]) != expected_digit:
        return False
    return True


def segundo_digito_verificador(cpf):
    # Valida o segundo dígito verificador
    sum_of_products = sum(int(a) * int(b)
                          for a, b in zip(cpf[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if int(cpf[10]) != expected_digit:
        return False
    return True


def validar_cpf(cpf):
    """Escreva aqui em baixo a sua solução"""
    # mantém apenas os números do CPF, ignorando pontuações
    cpf = cpf.translate(str.maketrans('', '', '.-'))

    if len(cpf) == 11:
        if primeiro_digito_verificador(cpf) and segundo_digito_verificador(cpf):
            return True
        return False
    else:
        return False
