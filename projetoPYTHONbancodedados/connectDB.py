import sqlite3

conexao = sqlite3.connect("bruninho.sqlite")
cursor = conexao.cursor()
conexao.commit()
