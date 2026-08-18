from src.imobiliaria.models.apartamento import Apartamento
from src.imobiliaria.models.casa import Casa
from src.imobiliaria.models.estudio import Estudio
from src.imobiliaria.clientes.cliente import Cliente
from src.imobiliaria.orcamentos.orcamento import Orcamento
from src.imobiliaria.contratos.contrato import Contrato


import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione ENTER para continuar...")


# ============================================================
# LISTAS DO SISTEMA
# ============================================================

clientes = []
imoveis = []
orcamentos = []


# ============================================================
# VALIDAÇÕES GENÉRICAS
# ============================================================

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



def menu_principal():
    while True:
        limpar_tela()
        print("\n" + "=" * 50)
        print("           SISTEMA IMOBILIÁRIA")
        print("=" * 50)
        print("1 - Clientes")
        print("2 - Imóveis")
        print("3 - Orçamentos")
        print("0 - Sair")
        print("=" * 50)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes()

        elif opcao == "2":
            menu_imoveis()

        elif opcao == "3":
            menu_orcamentos()

        elif opcao == "0":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida!")



def menu_clientes():
    while True:
        limpar_tela()
        print("\n" + "=" * 50)
        print("              CLIENTES")
        print("=" * 50)
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("0 - Voltar")
        print("=" * 50)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nCadastro de cliente")
            print("-" * 50)

            nome = pedir_texto("Nome: ")
            cpf = pedir_cpf("CPF: ")
            telefone = pedir_telefone("Telefone: ")
            email = pedir_email("E-mail: ")
            possui_criancas = pedir_sim_nao("Possui crianças? (s/n): ")

            cliente = Cliente(
                _nome=nome,
                _cpf=cpf,
                _telefone=telefone,
                _email=email,
                _possui_criancas=possui_criancas
            )

            # Salva o cliente na lista
            clientes.append(cliente)

            print("\nCliente cadastrado com sucesso!")
            print(f"Nome: {cliente.nome}")

            pausar()

        elif opcao == "2":
            print("\n" + "=" * 50)
            print("          CLIENTES CADASTRADOS")
            print("=" * 50)

            if not clientes:
                print("Nenhum cliente cadastrado.")
            else:
                for i, cliente in enumerate(clientes, start=1):
                    print(f"\nCliente {i}")
                    print(f"Nome: {cliente.nome}")
                    print(f"CPF: {cliente.cpf}")
                    print(f"Telefone: {cliente.telefone}")
                    print(f"E-mail: {cliente.email}")
                    print(
                        f"Possui crianças: "
                        f"{'Sim' if cliente.possui_criancas else 'Não'}"
                    )
                    print("-" * 50)

                    pausar()

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida!")




def menu_imoveis():
    while True:
        limpar_tela()
        print("\n" + "=" * 50)
        print("               IMÓVEIS")
        print("=" * 50)
        print("1 - Cadastrar apartamento")
        print("2 - Cadastrar casa")
        print("3 - Cadastrar estúdio")
        print("4 - Listar imóveis")
        print("0 - Voltar")
        print("=" * 50)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_apartamento()

        elif opcao == "2":
            cadastrar_casa()

        elif opcao == "3":
            cadastrar_estudio()

        elif opcao == "4":
            print("\nLista de imóveis")
            listar_imoveis()
            pausar()

            

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida!")


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
def listar_clientes_resumido():
    """Lista clientes com índice para seleção."""
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return False
    
    print("\n" + "-" * 50)
    print("Clientes disponíveis:")
    for i, cli in enumerate(clientes, start=1):
        print(f"{i}. {cli.nome} (CPF: {cli.cpf})")
    print("-" * 50)
    return True


def listar_imoveis_resumido():
    """Lista imóveis com índice para seleção."""
    if not imoveis:
        print("Nenhum imóvel cadastrado.")
        return False
    
    print("\n" + "-" * 50)
    print("Imóveis disponíveis:")
    for i, imv in enumerate(imoveis, start=1):
        print(f"{i}. {imv.get_tipo()} - {imv.endereco}")
        print(f"   Quartos: {imv.quantidade_quartos} | Vagas: {imv.quantidade_vagas}")
        print(f"   Aluguel base: R$ {imv.calcular_aluguel():.2f}")
    print("-" * 50)
    return True


def criar_orcamento():
    """Cria um novo orçamento."""
    limpar_tela()
    print("\n" + "=" * 50)
    print("         NOVO ORÇAMENTO")
    print("=" * 50)
    
    # 1. Selecionar cliente
    print("\nPasso 1: Selecionar cliente")
    if not listar_clientes_resumido():
        print("Cadastre um cliente primeiro!")
        pausar()
        return
    
    try:
        idx_cliente = int(input("\nEscolha o número do cliente: ")) - 1
        if idx_cliente < 0 or idx_cliente >= len(clientes):
            print("Cliente inválido!")
            pausar()
            return
        cliente = clientes[idx_cliente]
        print(f"\n✅ Cliente selecionado: {cliente.nome}")
    except ValueError:
        print("Entrada inválida!")
        pausar()
        return
    
    # 2. Selecionar imóvel
    print("\nPasso 2: Selecionar imóvel")
    if not listar_imoveis_resumido():
        print("Cadastre um imóvel primeiro!")
        pausar()
        return
    
    try:
        idx_imovel = int(input("\nEscolha o número do imóvel: ")) - 1
        if idx_imovel < 0 or idx_imovel >= len(imoveis):
            print("Imóvel inválido!")
            pausar()
            return
        imovel = imoveis[idx_imovel]
        print(f"\n✅ Imóvel selecionado: {imovel.get_tipo()} - {imovel.endereco}")
    except ValueError:
        print("Entrada inválida!")
        pausar()
        return
    
    # 3. Definir parcelas do contrato
    print("\nPasso 3: Definir parcelas do contrato")
    print("O contrato imobiliário tem valor fixo de R$ 2.000,00")
    print("Pode ser parcelado em até 5 vezes.")
    
    while True:
        try:
            parcelas = int(input("\nNúmero de parcelas (1 a 5): "))
            if 1 <= parcelas <= 5:
                break
            print("❌ O número deve ser entre 1 e 5!")
        except ValueError:
            print("❌ Digite um número inteiro!")
    
    # 4. Criar o contrato
    contrato = Contrato()
    contrato.quantidade_parcelas = parcelas  # Isso ativa o setter e calcula a parcela
    
    # 5. Criar o orçamento
    orcamento = Orcamento()
    orcamento.cliente = cliente
    orcamento.imovel = imovel
    
    try:
        # Calcula o total mensal (aluguel + parcela do contrato)
        total_mensal = orcamento.calcular_orcamento(contrato)
    except ValueError as e:
        print(f"❌ Erro ao calcular orçamento: {e}")
        pausar()
        return
    
    # 6. Adiciona à lista de orçamentos
    orcamentos.append(orcamento)
    
    # 7. Exibe o resultado
    exibir_orcamento(orcamento)
    
    pausar()

def exibir_orcamento(orcamento):
    """Exibe os detalhes de um orçamento."""
    resumo = orcamento.exibir_resumo()
    
    print("\n" + "=" * 60)
    print("              RESUMO DO ORÇAMENTO")
    print("=" * 60)
    
    # Dados do cliente
    print(f"\n📋 CLIENTE:")
    print(f"   Nome: {resumo['cliente']}")
    print(f"   CPF: {resumo['cliente_cpf']}")
    print(f"   Possui crianças: {'Sim' if resumo['possui_criancas'] else 'Não'}")
    
    # Dados do imóvel
    print(f"\n🏠 IMÓVEL:")
    print(f"   Tipo: {resumo['imovel_tipo']}")
    print(f"   Endereço: {resumo['endereco']}")
    print(f"   Quartos: {resumo['quartos']}")
    print(f"   Vagas: {resumo['vagas']}")
    
    # Cálculo do aluguel
    print(f"\n💰 ALUGUEL:")
    print(f"   Valor base: R$ {resumo['valor_base']:.2f}")
    if resumo['quartos_extras'] > 0:
        print(f"   + Quartos extras: R$ {resumo['quartos_extras']:.2f}")
    if resumo['vagas'] > 0:
        print(f"   + Vagas: R$ {resumo['vagas']:.2f}")
    if resumo['desconto'] > 0:
        print(f"   - Desconto ({resumo['percentual_desconto']:.0f}%): R$ {resumo['desconto']:.2f}")
    print(f"   ──────────────────────────")
    print(f"   Subtotal aluguel: R$ {resumo['valor_aluguel_final']:.2f}")
    
    # Contrato
    print(f"\n📄 CONTRATO IMOBILIÁRIO:")
    print(f"   Valor total: R$ 2.000,00")
    print(f"   Parcelas: {resumo['parcelas']}x de R$ {resumo['valor_parcela']:.2f}")
    
    # TOTAL
    print(f"\n💵 TOTAL MENSAL:")
    print(f"   Aluguel + Parcela do contrato = R$ {resumo['total_mensal']:.2f}")
    print(f"\n   Status: {resumo.get('status_contrato', 'ATIVO')}")
    
    print("\n" + "=" * 60)

def listar_orcamentos():
    """Lista todos os orçamentos gerados."""
    limpar_tela()
    print("\n" + "=" * 50)
    print("         ORÇAMENTOS GERADOS")
    print("=" * 50)
    
    if not orcamentos:
        print("\nNenhum orçamento gerado ainda.")
        pausar()
        return
    
    print(f"\nTotal de orçamentos: {len(orcamentos)}\n")
    
    for i, orc in enumerate(orcamentos, start=1):
        resumo = orc.exibir_resumo()
        print(f"\n{'='*50}")
        print(f"ORÇAMENTO #{i}")
        print(f"{'='*50}")
        print(f"Cliente: {resumo['cliente']}")
        print(f"Imóvel: {resumo['imovel_tipo']} - {resumo['endereco']}")
        print(f"Aluguel mensal: R$ {resumo['valor_aluguel_final']:.2f}")
        print(f"Parcelas contrato: {resumo['parcelas']}x de R$ {resumo['valor_parcela']:.2f}")
        print(f"TOTAL MENSAL: R$ {resumo['total_mensal']:.2f}")
        print(f"Status: {resumo.get('status_contrato', 'ATIVO')}")
    
    pausar()



def listar_imoveis():
    print("\n" + "=" * 50)
    print("          IMÓVEIS CADASTRADOS")
    print("=" * 50)

    if not imoveis:
        print("Nenhum imóvel cadastrado.")
        return

    for i, imovel in enumerate(imoveis, start=1):
        print(f"\nImóvel {i}")
        print(f"Tipo: {imovel.get_tipo()}")
        print(f"Endereço: {imovel.endereco}")
        print(f"Quartos: {imovel.quantidade_quartos}")
        print(f"Vagas: {imovel.quantidade_vagas}")
        print(f"Valor base: R$ {imovel.valor_base:.2f}")
        print(f"Aluguel: R$ {imovel.calcular_aluguel():.2f}")
        print("-" * 50)


def cadastrar_apartamento():
    print("\n" + "=" * 50)
    print("       CADASTRO DE APARTAMENTO")
    print("=" * 50)

    endereco = input("Endereço: ")
    quartos = pedir_inteiro_positivo("Quantidade de quartos: ")
    vagas = pedir_vagas("Quantidade de vagas: ")

    apartamento = Apartamento(
        _endereco=endereco,
        _quantidade_quartos=quartos,
        _quantidade_vagas=vagas
    )

    imoveis.append(apartamento)

    print("\nApartamento cadastrado!")
    print(f"Endereço: {apartamento.endereco}")
    print(f"Aluguel: R$ {apartamento.calcular_aluguel():.2f}")


def cadastrar_casa():
    print("\n" + "=" * 50)
    print("            CADASTRO DE CASA")
    print("=" * 50)

    endereco = input("Endereço: ")
    quartos = int(input("Quantidade de quartos: "))
    vagas = int(input("Quantidade de vagas: "))

    casa = Casa(
        _endereco=endereco,
        _quantidade_quartos=quartos,
        _quantidade_vagas=vagas
    )

    imoveis.append(casa)

    print("\nCasa cadastrada!")
    print(f"Endereço: {casa.endereco}")
    print(f"Aluguel: R$ {casa.calcular_aluguel():.2f}")


def cadastrar_estudio():
    print("\n" + "=" * 50)
    print("           CADASTRO DE ESTÚDIO")
    print("=" * 50)

    endereco = input("Endereço: ")
    vagas = int(input("Quantidade de vagas: "))

    estudio = Estudio(
        _endereco=endereco,
        _quantidade_quartos=1,
        _quantidade_vagas=vagas
    )

    imoveis.append(estudio)

    print("\nEstúdio cadastrado!")
    print(f"Endereço: {estudio.endereco}")
    print(f"Aluguel: R$ {estudio.calcular_aluguel():.2f}")


def menu_orcamentos():
    """Menu principal de orçamentos."""
    while True:
        limpar_tela()
        print("\n" + "=" * 50)
        print("             ORÇAMENTOS")
        print("=" * 50)
        print("1 - Novo orçamento")
        print("2 - Listar orçamentos")
        print("3 - Gerar CSV das parcelas")  # ← NOVO
        print("0 - Voltar")
        print("=" * 50)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_orcamento()
        elif opcao == "2":
            listar_orcamentos()
        elif opcao == "3":
            gerar_csv_parcelas()  # ← NOVO
        elif opcao == "0":
            break
        else:
            print("\n❌ Opção inválida!")
            pausar()

def gerar_csv_parcelas():
    """Gera um arquivo CSV com as parcelas de um contrato."""
    limpar_tela()
    print("\n" + "=" * 50)
    print("         GERAR CSV DAS PARCELAS")
    print("=" * 50)
    
    if not orcamentos:
        print("\n❌ Nenhum orçamento gerado ainda!")
        pausar()
        return
    
    print("\nOrçamentos disponíveis:")
    for i, orc in enumerate(orcamentos, 1):
        cliente = orc.cliente.nome if orc.cliente else "N/A"
        total = orc.total_mensal if hasattr(orc, 'total_mensal') else 0
        print(f"{i}. Cliente: {cliente} - Total: R$ {total:.2f}")
    
    try:
        idx = int(input("\nEscolha o número do orçamento: ")) - 1
        if idx < 0 or idx >= len(orcamentos):
            print("❌ Opção inválida!")
            pausar()
            return
        
        orcamento = orcamentos[idx]
        contrato = orcamento.contrato
        
        if not contrato:
            print("❌ Este orçamento não tem um contrato associado!")
            pausar()
            return
        
        # Nome do arquivo com cliente e data
        nome_cliente = orcamento.cliente.nome.replace(" ", "_") if orcamento.cliente else "cliente"
        from datetime import datetime
        data_atual = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"parcelas_{nome_cliente}_{data_atual}.csv"
        
        # Gera o CSV
        contrato.gerar_parcelas_csv(nome_arquivo)
        
        print(f"\n📄 Arquivo gerado: {nome_arquivo}")
        print("📂 O arquivo está na pasta do programa!")
        print("💡 Abra com Excel ou Google Sheets")
        
    except ValueError:
        print("❌ Digite um número válido!")
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    pausar()


def main():
    menu_principal()


if __name__ == "__main__":
    main()

