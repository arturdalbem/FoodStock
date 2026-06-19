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
        self.quantidadeMinima = quantityMinima if 'quantityMinima' in locals() else quantidadeMinima # Ajuste caso use o nome em inglês/português
        
        # Tratamento seguro para a data logo na criação do objeto
        if dataValidade and isinstance(dataValidade, str):
            self.dataValidade = datetime.strptime(dataValidade, "%Y-%m-%d")
        else:
            self.dataValidade = dataValidade

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "categoria": self.categoria,
            "quantidade": self.quantidade,
            "unidade": self.unidade.value if hasattr(self.unidade, 'value') else self.unidade,
            "quantidadeAtual": self.quantidadeAtual,
            "quantidadeMinima": self.quantidadeMinima,
            "dataValidade": self.dataValidade.strftime("%Y-%m-%d") if self.dataValidade else None
        }