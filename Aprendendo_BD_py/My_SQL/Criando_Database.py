import sqlite3

conexao = sqlite3.connect("nova_database.bd")
cursor = conexao.cursor()
cursor.execute('''
            create table produtos(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(30),
                preco DECIMAL(3,2))
            ''')
cursor.execute('''
            create table cliente(
                id INT AUTO_INCREMENT PRIMARY KEY,
                primeiro_nome VARCHAR(30),
                ultimo_nome VARCHAR(30),
                celular VARCHAR(13))
            ''')
conexao.commit()
cursor.close()
conexao.close()
