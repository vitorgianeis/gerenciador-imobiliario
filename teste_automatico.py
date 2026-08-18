"""
Script de teste automático - simula o usuário usando o sistema.
Execute: python teste_automatico.py
"""
import sys
from io import StringIO
from unittest.mock import patch

from src.imobiliaria.imoveis.apartamento import Apartamento
from src.imobiliaria.imoveis.casa import Casa
from src.imobiliaria.imoveis.estudio import Estudio
from src.imobiliaria.clientes.cliente import Cliente
from src.imobiliaria.orcamentos.orcamento import Orcamento
from src.imobiliaria.contratos.contrato import Contrato
from src.imobiliaria.ui.menus import (
    clientes, imoveis, orcamentos,
    cadastrar_cliente, cadastrar_apartamento, cadastrar_casa,
    cadastrar_estudio, criar_orcamento, gerar_csv_parcelas,
)


def limpar_listas():
    clientes.clear()
    imoveis.clear()
    orcamentos.clear()


def testar_cadastro_cliente():
    print("=" * 50)
    print("TESTE: Cadastro de Cliente")
    print("=" * 50)

    entradas = ["Maria Silva", "12345678901", "11999999999", "maria@teste.com", "n", ""]
    with patch("builtins.input", side_effect=entradas):
        cadastrar_cliente()

    assert len(clientes) == 1
    assert clientes[0].nome == "Maria Silva"
    assert clientes[0].cpf == "12345678901"
    assert clientes[0].possui_criancas == False
    print("OK: Cliente cadastrado corretamente!\n")


def testar_cadastro_apartamento():
    print("=" * 50)
    print("TESTE: Cadastro de Apartamento (2 quartos, 1 vaga)")
    print("=" * 50)

    entradas = ["Rua das Flores, 100", "2", "1", ""]
    with patch("builtins.input", side_effect=entradas):
        cadastrar_apartamento()

    apt = imoveis[-1]
    assert isinstance(apt, Apartamento)
    assert apt.quantidade_quartos == 2
    assert apt.quantidade_vagas == 1
    # Base 700 + quarto extra 200 + vaga 300 = 1200
    assert apt.calcular_aluguel() == 1200.00
    print("OK: Apartamento cadastrado e valor correto (R$ 1200,00)!\n")


def testar_cadastro_casa():
    print("=" * 50)
    print("TESTE: Cadastro de Casa (3 quartos, 2 vagas)")
    print("=" * 50)

    entradas = ["Rua do Sol, 200", "3", "2", ""]
    with patch("builtins.input", side_effect=entradas):
        cadastrar_casa()

    casa = imoveis[-1]
    assert isinstance(casa, Casa)
    assert casa.quantidade_quartos == 3
    assert casa.quantidade_vagas == 2
    # Base 900 + 2 quartos extras (250 cada) + 2 vagas (300 cada) = 900 + 500 + 600 = 2000
    assert casa.calcular_aluguel() == 2000.00
    print("OK: Casa cadastrada e valor correto (R$ 2000,00)!\n")


def testar_cadastro_estudio():
    print("=" * 50)
    print("TESTE: Cadastro de Estúdio (3 vagas)")
    print("=" * 50)

    entradas = ["Rua da Lua, 300", "3", ""]
    with patch("builtins.input", side_effect=entradas):
        cadastrar_estudio()

    est = imoveis[-1]
    assert isinstance(est, Estudio)
    assert est.quantidade_vagas == 3
    # Base 1200 + 2 vagas base 250 + 1 vaga extra 60 = 1510
    assert est.calcular_aluguel() == 1510.00
    print("OK: Estúdio cadastrado e valor correto (R$ 1510,00)!\n")


def testar_orcamento_apartamento_sem_criancas():
    print("=" * 50)
    print("TESTE: Orçamento Apartamento + Desconto 5%")
    print("=" * 50)

    # Maria não tem crianças -> desconto 5%
    cliente = clientes[0]
    apt = imoveis[0]  # Apartamento 2q 1v = 1200

    contrato = Contrato()
    contrato.quantidade_parcelas = 5  # 2000 / 5 = 400

    orcamento = Orcamento()
    orcamento.cliente = cliente
    orcamento.imovel = apt
    total = orcamento.calcular_orcamento(contrato)

    # Aluguel 1200 - 5% desconto = 1140 + parcela 400 = 1540
    assert total == 1540.00
    assert orcamento._valor_desconto == 60.00
    assert orcamento._valor_aluguel_final == 1140.00

    orcamentos.append(orcamento)

    resumo = orcamento.exibir_resumo()
    print(f"\nResumo:")
    print(f"  Aluguel base: R$ {resumo['valor_base']:.2f}")
    print(f"  Desconto 5%: R$ {resumo['desconto']:.2f}")
    print(f"  Aluguel final: R$ {resumo['valor_aluel_final']:.2f}" if 'valor_aluel_final' in resumo else f"  Aluguel final: R$ {resumo['valor_aluguel_final']:.2f}")
    print(f"  Parcela contrato: R$ {resumo['valor_parcela']:.2f}")
    print(f"  TOTAL MENSAL: R$ {resumo['total_mensal']:.2f}")
    print("OK: Orçamento com desconto calculado corretamente!\n")


def testar_csv():
    print("=" * 50)
    print("TESTE: Geração do CSV")
    print("=" * 50)

    orcamento = orcamentos[0]
    nome_arquivo = "/tmp/teste_estrutura.csv"
    orcamento.gerar_csv_parcelas_mensais(nome_arquivo)

    with open(nome_arquivo, "r", encoding="utf-8-sig") as f:
        linhas = f.readlines()

    # 1 cabeçalho + 12 parcelas
    assert len(linhas) == 13
    print(f"CSV gerado com {len(linhas) - 1} parcelas")
    print("OK: CSV com 12 parcelas mensais!\n")


def main():
    limpar_listas()

    print("\n" + "=" * 60)
    print("   TESTE AUTOMÁTICO - SISTEMA IMOBILIÁRIA R.M")
    print("=" * 60 + "\n")

    try:
        testar_cadastro_cliente()
        testar_cadastro_apartamento()
        testar_cadastro_casa()
        testar_cadastro_estudio()
        testar_orcamento_apartamento_sem_criancas()
        testar_csv()

        print("=" * 60)
        print("   TODOS OS TESTES PASSARAM COM SUCESSO!")
        print("=" * 60)

    except AssertionError as e:
        print(f"\nERRO: Teste falhou - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nERRO INESPERADO: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
