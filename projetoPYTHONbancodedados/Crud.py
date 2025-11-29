from connectDB import cursor,  conexao
 
def create():
    print("criou tabela")
    

def read():
            sistema = True
            comando = "SELECT name FROM sqlite_master where type='table';"
            conexao.execute(comando)

            tabelas = cursor.fetchall()

            if tabelas:
                for tabela in tabelas:
                    print("Tabela", tabela[0])
            else:
                print("Nenhuma Tabela encontrada no banco atual")
                print("nenhuma tabela existente")

def update():
    print("seu update foi um suscesso")

def delete():
    print("voce deletou um produto")
    pass
