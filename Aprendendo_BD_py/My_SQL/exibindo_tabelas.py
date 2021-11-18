import sqlite3
conexao = sqlite3.connect("nova_database.bd")
cursor = conexao.cursor()
cursor.execute("select * from nova_database.bd")
tabelas = cursor.fetchall()
print(tabelas)
cursor.close()
conexao.close()

#Continuar depois criando as funções.py da página 291