import  sqlite3
conexao = sqlite3.connect("agenda_nova.bd")
cursor = conexao.cursor()
cursor.execute("select * from agenda_nova")
resultado = cursor.fetchall()
for reg in resultado:
    print(f"Nome: {reg[0]}\nTelefone: {reg[1]}")
cursor.close()
conexao.close()