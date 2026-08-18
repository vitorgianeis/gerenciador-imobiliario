from dataclasses import dataclass
from typing import Optional
from src.imobiliaria.clientes.cliente import Cliente
from src.imobiliaria.imoveis.imovel import Imovel
from src.imobiliaria.contratos.contrato import Contrato  # NOVO IMPORT


@dataclass
class Orcamento:
    """Representa um orçamento de aluguel."""

    _cliente: Optional[Cliente] = None
    _imovel: Optional[Imovel] = None
    _contrato: Optional[Contrato] = None  # NOVO ATRIBUTO
    _valor_aluguel_base: float = 0.0
    _valor_quartos_extras: float = 0.0
    _valor_vagas: float = 0.0
    _valor_desconto: float = 0.0
    _percentual_desconto: float = 0.0
    _valor_aluguel_final: float = 0.0
    _total_mensal: float = 0.0  # NOVO ATRIBUTO (aluguel + parcela contrato)
    _status: str = "RASCUNHO"
    _observacoes: str = ""
    _id: Optional[int] = None

    def __post_init__(self):
        if self._imovel is not None:
            self.imovel = self._imovel

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def cliente(self) -> Optional[Cliente]:
        return self._cliente

    @cliente.setter
    def cliente(self, value: Cliente):
        self._cliente = value

    @property
    def imovel(self) -> Optional[Imovel]:
        return self._imovel

    @imovel.setter
    def imovel(self, value: Imovel):
        self._imovel = value
        if value:
            self._valor_aluguel_base = value.valor_base

    @property
    def contrato(self) -> Optional[Contrato]:
        return self._contrato

    @contrato.setter
    def contrato(self, value: Contrato):
        self._contrato = value

    @property
    def valor_aluguel_base(self) -> float:
        return self._valor_aluguel_base

    @property
    def valor_quartos_extras(self) -> float:
        return self._valor_quartos_extras

    @property
    def valor_vagas(self) -> float:
        return self._valor_vagas

    @property
    def valor_desconto(self) -> float:
        return self._valor_desconto

    @property
    def percentual_desconto(self) -> float:
        return self._percentual_desconto

    @property
    def valor_aluguel_final(self) -> float:
        return self._valor_aluguel_final

    @property
    def total_mensal(self) -> float:
        return self._total_mensal

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str):
        self._status = value

    @property
    def observacoes(self) -> str:
        return self._observacoes

    @observacoes.setter
    def observacoes(self, value: str):
        self._observacoes = value

    def calcular_orcamento(self, contrato: Contrato) -> float:
        """Calcula o valor total do orçamento (aluguel + parcela do contrato)."""
        if not self._imovel or not self._cliente:
            raise ValueError("Imóvel e cliente devem ser definidos")

        self._contrato = contrato

        # Calcula adicionais
        self._valor_quartos_extras = self._imovel.calcular_quartos_extras()
        self._valor_vagas = self._imovel.calcular_vagas()

        # Soma tudo
        aluguel_com_adicionais = (
            self._valor_aluguel_base
            + self._valor_quartos_extras
            + self._valor_vagas
        )

        # Verifica desconto (apenas apartamentos sem crianças)
        tipo_imovel = self._imovel.get_tipo()
        if self._cliente.eh_elegivel_desconto(tipo_imovel):
            self._percentual_desconto = 5.0
            self._valor_desconto = aluguel_com_adicionais * 0.05
        else:
            self._percentual_desconto = 0.0
            self._valor_desconto = 0.0

        # Aluguel final (com desconto)
        self._valor_aluguel_final = aluguel_com_adicionais - self._valor_desconto

        # Adiciona a parcela do contrato
        parcela_contrato = contrato.calcular_parcela(contrato.quantidade_parcelas)
        self._total_mensal = self._valor_aluguel_final + parcela_contrato

        self._status = "FINALIZADO"
        return self._total_mensal

    def exibir_resumo(self) -> dict:
        """Retorna um resumo completo do orçamento."""
        resumo = {
            "cliente": self._cliente.nome if self._cliente else "",
            "cliente_cpf": self._cliente.cpf if self._cliente else "",
            "imovel_tipo": self._imovel.get_tipo() if self._imovel else "",
            "endereco": self._imovel.endereco if self._imovel else "",
            "quartos": self._imovel.quantidade_quartos if self._imovel else 0,
            "quantidade_vagas": self._imovel.quantidade_vagas if self._imovel else 0,
            "valor_base": self._valor_aluguel_base,
            "quartos_extras": self._valor_quartos_extras,
            "valor_vagas": self._valor_vagas,
            "desconto": self._valor_desconto,
            "percentual_desconto": self._percentual_desconto,
            "valor_aluguel_final": self._valor_aluguel_final,
            "possui_criancas": (
                self._cliente.possui_criancas if self._cliente else False
            ),
        }
        
        # Adiciona dados do contrato se existir
        if self._contrato:
            resumo["parcelas"] = self._contrato.quantidade_parcelas
            resumo["valor_parcela"] = self._contrato.valor_parcela
            resumo["total_mensal"] = self._total_mensal
            resumo["status_contrato"] = self._contrato.status
            
        return resumo

    def gerar_csv_parcelas_mensais(self, nome_arquivo: str = "parcelas_mensais.csv"):
        """
        Gera um arquivo CSV com as 12 parcelas mensais do orçamento.
        Cada parcela inclui: aluguel + parcela do contrato.
        """
        import csv
        from datetime import date, timedelta

        if not self._cliente or not self._imovel:
            raise ValueError("Orçamento deve ter cliente e imóvel definidos")

        valor_aluguel = self._valor_aluguel_final
        parcela_contrato = (
            self._contrato.valor_parcela if self._contrato else 0.0
        )
        total_mensal = valor_aluguel + parcela_contrato

        data_atual = date.today()

        with open(nome_arquivo, 'w', newline='', encoding='utf-8-sig') as arquivo:
            writer = csv.writer(arquivo, delimiter=';')

            # Cabeçalho
            writer.writerow([
                'Mês',
                'Aluguel (R$)',
                'Parcela Contrato (R$)',
                'Total Mensal (R$)',
                'Data Vencimento',
                'Status'
            ])

            # Gera 12 parcelas mensais
            for i in range(1, 13):
                data_vencimento = data_atual + timedelta(days=30 * i)
                writer.writerow([
                    f'{i}/12',
                    f'{valor_aluguel:.2f}',
                    f'{parcela_contrato:.2f}',
                    f'{total_mensal:.2f}',
                    data_vencimento.strftime('%d/%m/%Y'),
                    'A PAGAR'
                ])

        print(f"✅ Arquivo '{nome_arquivo}' gerado com sucesso!")