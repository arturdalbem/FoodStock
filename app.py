from flask import Flask, render_template, request, redirect
import sqlite3
import os

# Cria um caminho absoluto dinâmico para a pasta database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "estoque.db")


app = Flask(__name__)

def criar_tabelas():

    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        lote TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        quantidade_minima INTEGER NOT NULL,
        unidade TEXT NOT NULL,
        data_validade TEXT NOT NULL
    )
    """)

    conexao.commit()
    conexao.close()

    criar_tabelas()

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    conexao = sqlite3.connect(DB_PATH)

    cursor = conexao.cursor()

    cursor.execute("SELECT COUNT(*) FROM produtos")

    total_produtos = cursor.fetchone()[0]

    conexao.close()

    return render_template(
        "dashboard.html",
        total_produtos=total_produtos
    )



@app.route("/produtos", methods=["GET", "POST"])
def produtos():

    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()

    if request.method == "POST":

        nome = request.form["nome"]
        categoria = request.form["categoria"]
        lote = request.form["lote"]
        quantidade = request.form["quantidade"]
        quantidade_minima = request.form["quantidade_minima"]
        unidade = request.form["unidade"]
        data_validade = request.form["data_validade"]

        cursor.execute("""
        INSERT INTO produtos
        (nome, categoria, lote, quantidade, quantidade_minima, unidade, data_validade)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
       (
        nome,
        categoria,
        lote,
        quantidade,
        quantidade_minima,
        unidade,
        data_validade
))

        conexao.commit()

        conexao.close()

        return redirect("/produtos")

    cursor.execute("SELECT * FROM produtos")

    produtos = cursor.fetchall()

    conexao.close()

    return render_template(
        "produtos.html",
        produtos=produtos
    )

@app.route("/excluir_produto/<int:id>")
def excluir_produto(id):

    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))

    conexao.commit()
    conexao.close()

    return redirect("/produtos")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        confirmar_senha = request.form["confirmar_senha"]

        if senha != confirmar_senha:
            return "As senhas não coincidem!"

        conexao = sqlite3.connect(DB_PATH)

        cursor = conexao.cursor()

        cursor.execute("""INSERT INTO usuarios (nome, email, senha)
        VALUES (?, ?, ?)
        """, (nome, email, senha))

        conexao.commit()

        conexao.close()

        return redirect("/")

    return render_template("cadastro.html")

@app.route("/editar_produto/<int:id>", methods=["GET", "POST"])
def editar_produto(id):

    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()

    if request.method == "POST":

        nome = request.form["nome"]
        categoria = request.form["categoria"]
        lote = request.form["lote"]
        quantidade = request.form["quantidade"]
        quantidade_minima = request.form["quantidade_minima"]
        unidade = request.form["unidade"]
        data_validade = request.form["data_validade"]

        cursor.execute("""
            UPDATE produtos
            SET
                nome = ?,
                categoria = ?,
                lote = ?,
                quantidade = ?,
                quantidade_minima = ?,
                unidade = ?,
                data_validade = ?
            WHERE id = ?
        """, (
            nome,
            categoria,
            lote,
            quantidade,
            quantidade_minima,
            unidade,
            data_validade,
            id
        ))

        conexao.commit()
        conexao.close()

        return redirect("/produtos")

    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
    produto = cursor.fetchone()

    conexao.close()

    return render_template(
        "editar_produto.html",
        produto=produto
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
