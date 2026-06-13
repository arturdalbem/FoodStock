from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    conexao = sqlite3.connect("database/estoque.db")

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

    conexao = sqlite3.connect("database/estoque.db")
    cursor = conexao.cursor()

    if request.method == "POST":

        nome = request.form["nome"]
        categoria = request.form["categoria"]
        quantidade = request.form["quantidade"]
        quantidade_minima = request.form["quantidade_minima"]
        unidade = request.form["unidade"]
        data_validade = request.form["data_validade"]

        cursor.execute("""
        INSERT INTO produtos
        (nome, categoria, quantidade, quantidade_minima, unidade, data_validade)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            nome,
            categoria,
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

if __name__ == "__main__":
    app.run(debug=True)
