from flask import Blueprint, request, jsonify
from services.produto_service import criar_produto, dar_saida, listar_produtos, alertaValidade, alertaEstoqueBaixo

produtos_bp = Blueprint('produtos', __name__)

@produtos_bp.route('/produtos', methods=['GET'])
def get_produtos():
    return jsonify(listar_produtos())

@produtos_bp.route('/produtos', methods=['POST'])
def post_produto():
    data = request.json
    produto = criar_produto(data)
    return jsonify(produto), 201 #201 (Created) = requisição bem sucedida e algo foi criado

@produtos_bp.route('/produtos/<int:id>/saida', methods=['POST'])
def saida(id):
    data = request.json
    produto = dar_saida(id, data["quantidade"])

    if produto:
        return jsonify(produto)
    return {"erro": "Produto não encontrado"}, 404 #404 (Not Found) = o servidor não pode encontrar o recurso solicitado

@produtos_bp.route('/produtos/alerta/estoque-baixo', methods=['GET'])
def get_alerta_estoque_baixo():
    return jsonify(alertaEstoqueBaixo())

@produtos_bp.route('/produtos/alerta/validade', methods=['GET'])
def get_alerta_validade():
    dias = request.args.get('dias', default=2, type=int)
    return jsonify(alertaValidade(dias))