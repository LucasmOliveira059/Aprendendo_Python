import sqlite3
conexao = sqlite3.connect("agenda_nova.bd")
cursor = conexao.cursor()
cursor.execute("select * from agenda_nova")
resultado = cursor.fetchone()
print(f"Nome: {resultado[0]}\nTelefone : {resultado[1]}")
cursor.close()
conexao.close()