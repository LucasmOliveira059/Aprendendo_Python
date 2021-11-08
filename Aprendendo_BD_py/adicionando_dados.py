import sqlite3

dados = [("Jonatas", "555-333-9999"),
         ("Andressa", "553-442-6789"),
         ("Gláucia", "333-444-9876")]
conexao = sqlite3.connect("agenda_nova.bd")
cursor = conexao.cursor()
cursor.executemany('''
        insert into agenda_nova(nome, telefone)
        values(?, ?)
        ''', dados)
conexao.commit()
cursor.close()
conexao.close()