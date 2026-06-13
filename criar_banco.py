import sqlite3

conexao = sqlite3.connect("database/estoque.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    quantidade_minima INTEGER NOT NULL,
    unidade TEXT NOT NULL,
    data_validade TEXT NOT NULL
)
""")

conexao.commit()
conexao.close()

print("Tabela produtos criada com sucesso!")