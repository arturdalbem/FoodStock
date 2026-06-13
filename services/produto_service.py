from database.db import estoque
from models.produto import Produto
from datetime import datetime, timedelta
from enums.unidade import Unidade


def listar_produtos():
    return [p.to_dict() for p in estoque]

def criar_produto(data):
    try:
        unidade = Unidade(data["unidade"])
    except ValueError:
        raise ValueError(f"Unidade '{data['unidade']}' inválida. Use uma das seguintes: {[u.value for u in Unidade]}")

    novo = Produto(
        id=len(estoque) + 1,
        nome=data["nome"],
        categoria=data["categoria"],
        quantidade=data["quantidade"],
        unidade=data["unidade"],
        quantidadeAtual=data["quantidadeAtual"],
        quantidadeMinima=data["quantidadeMinima"],
        dataValidade=data["dataValidade"]
    )
    estoque.append(novo)
    return novo.to_dict()

def dar_saida(id, quantidade):
    for produto in estoque:
        if produto.id == id:
            produto.quantidade -= quantidade
            return produto.to_dict()
    return None

def alertaEstoqueBaixo():
    produtos_alerta = []

    for produtos in estoque:
        if produtos.quantidadeAtual <= produtos.quantidadeMinima:
            produtos_alerta.append(produtos.to_dict())

    return produtos_alerta

def alertaValidade(dias=2):
    produtos_vencendo = []
    hoje = datetime.today()

    for produto in estoque:
        validade = datetime.strptime(produto.dataValidade, "%Y-%m-%d")
        if validade - hoje <= timedelta(days=dias):
            produtos_vencendo.append(produto.to_dict())
    return produtos_vencendo