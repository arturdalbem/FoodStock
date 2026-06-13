from datetime import datetime
from enums.unidade import Unidade


class Produto:
    def __init__(self, id, nome, categoria, quantidade, unidade, quantidadeAtual, quantidadeMinima, dataValidade):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.unidade = Unidade(unidade)
        self.quantidadeAtual = quantidadeAtual
        self.quantidadeMinima = quantidadeMinima
        self.dataValidade = datetime.strptime(dataValidade, "%Y-%m-%d") # formato: "YYYY-MM-DD"

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "categoria": self.categoria,
            "quantidade": self.quantidade,
            "unidade": self.unidade.value,
            "quantidadeAtual": self.quantidadeAtual,
            "quantidadeMinima": self.quantidadeMinima,
            "dataValidade": self.dataValidade.strftime("%Y-%m-%d") # formato: "YYYY-MM-DD"

        }