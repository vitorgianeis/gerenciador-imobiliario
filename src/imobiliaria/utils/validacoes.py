def pedir_texto(mensagem):
    """
    Solicita um texto obrigatório.
    Não aceita campo vazio.
    """
    while True:
        valor = input(mensagem).strip()

        if valor:
            return valor

        print("Erro: este campo não pode ficar vazio.")


def pedir_inteiro(mensagem, minimo=0):
    """
    Solicita um número inteiro.
    Permite definir um valor mínimo.
    """
    while True:
        try:
            valor = int(input(mensagem))

            if valor >= minimo:
                return valor

            print(
                f"Erro: digite um número "
                f"maior ou igual a {minimo}."
            )

        except ValueError:
            print("Erro: digite apenas números inteiros.")


def pedir_decimal(mensagem, minimo=0.0):
    """
    Solicita um número decimal.
    Aceita vírgula ou ponto.
    """
    while True:
        try:
            entrada = input(mensagem).strip().replace(",", ".")
            valor = float(entrada)

            if valor >= minimo:
                return valor

            print(
                f"Erro: digite um valor "
                f"maior ou igual a {minimo}."
            )

        except ValueError:
            print("Erro: digite um número válido.")


def pedir_sim_nao(mensagem):
    """
    Solicita uma resposta de sim ou não.
    Retorna True para sim e False para não.
    """
    while True:
        valor = input(mensagem).strip().lower()

        if valor == "s":
            return True

        if valor == "n":
            return False

        print("Erro: digite 's' para sim ou 'n' para não.")


def pedir_cpf(mensagem):
    """
    Solicita um CPF com 11 números.
    Aceita CPF com ou sem pontuação.
    """
    while True:
        valor = input(mensagem).strip()

        cpf = (
            valor
            .replace(".", "")
            .replace("-", "")
            .replace(" ", "")
        )

        if not cpf.isdigit():
            print("Erro: CPF deve conter apenas números.")
            continue

        if len(cpf) != 11:
            print("Erro: CPF deve possuir 11 números.")
            continue

        return valor


def pedir_telefone(mensagem):
    """
    Solicita telefone com 10 ou 11 números.
    Aceita telefone com formatação.
    """
    while True:
        valor = input(mensagem).strip()

        telefone = (
            valor
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )

        if not telefone.isdigit():
            print("Erro: telefone inválido.")
            continue

        if len(telefone) not in (10, 11):
            print(
                "Erro: telefone deve possuir "
                "10 ou 11 números."
            )
            continue

        return valor


def pedir_email(mensagem):
    """
    Solicita um e-mail simples.
    """
    while True:
        valor = input(mensagem).strip()

        if "@" not in valor:
            print("Erro: e-mail deve conter '@'.")
            continue

        usuario, separador, dominio = valor.partition("@")

        if not usuario or not dominio:
            print("Erro: e-mail inválido.")
            continue

        if "." not in dominio:
            print("Erro: e-mail deve possuir um domínio válido.")
            continue

        return valor


def pedir_inteiro_positivo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))

            if valor < 1:
                print("Erro: digite um número maior que zero.")
                continue

            return valor

        except ValueError:
            print("Erro: digite apenas números inteiros.")


def pedir_vagas(mensagem):
    while True:
        try:
            valor = int(input(mensagem))

            if valor < 0:
                print("Erro: a quantidade de vagas não pode ser negativa.")
                continue

            return valor

        except ValueError:
            print("Erro: digite apenas números inteiros.")
