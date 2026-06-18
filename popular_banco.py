import sqlite3

conexao = sqlite3.connect("database/estoque.db")

cursor = conexao.cursor()

produtos = [

("Vinho Tinto","Bebidas",25,5,"l","2028-06-10"),

("Queijo Cheddar","Laticínios",50,5,"g","2028-06-14"),

("Picanha","Carnes",20,10,"kg","2028-06-21"),

("Peito de Frango","Carnes",35,10,"kg","2028-06-21"),

("Creme de Leite (200ml)","Laticínios",20,10,"ml","2028-06-21")

]

cursor.executemany("""
INSERT INTO produtos
(nome,categoria,quantidade,quantidade_minima,unidade,data_validade)
VALUES (?,?,?,?,?,?)
""", produtos)

conexao.commit()

conexao.close()

print("Produtos inseridos com sucesso!")