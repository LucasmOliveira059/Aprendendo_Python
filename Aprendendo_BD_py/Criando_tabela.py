import sqlite3
conexao = sqlite3.connect("agenda_nova.bd")
cursor = conexao.cursor()
cursor.execute('''
            create table agenda_nova(
                nome text,
                telefone text)
            ''')
cursor.execute('''
        insert into agenda_nova(nome, telefone)
        values(?, ?)
       ''', ("Arnaldo", "555-333-7788"))
conexao.commit()
cursor.close()
conexao.close()
