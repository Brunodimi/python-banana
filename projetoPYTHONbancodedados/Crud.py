from connectDB import cursor,  conexao
 
def create():
    
    nometb = input("qual nome deseja colocar na tabela num1: ")
    nometb1 = input("qual nome deseja colocar na tabela num2: ")
    nometb2 = input("qual nome deseja colocar na tabela num3: ")
    nometb3 = input("qual nome deseja colocar na tabela num4: ")
    nometb4 = input("qual nome deseja colocar na tabela num5: ")

    criarTabela = int(input("deseja criar uma tabela? 1 para sim e 2 para nao: "))
    if criarTabela == 1:
            
            comando_sql0 = f"""
            CREATE TABLE IF NOT EXISTS {nometb}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            DATE,
            TEXT NOT NULL,
            INTEGER
            );"""
            conexao.execute(comando_sql0)
            conexao.commit()
            print("sua tabela foi criada")

            comando_sql1 = f"""
            CREATE TABLE IF NOT EXISTS {nometb1}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            DATE,
            TEXT NOT NULL,
            INTEGER
            );"""
            conexao.execute(comando_sql1)
            conexao.commit()
            print("sua tabela foi criada")

            comando_sql2 = f"""
            CREATE TABLE IF NOT EXISTS {nometb2}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            DATE,
            TEXT NOT NULL,
            INTEGER
            );"""
            conexao.execute(comando_sql2)
            conexao.commit()
            print("sua tabela foi criada")

            comando_sql3 = f"""
            CREATE TABLE IF NOT EXISTS {nometb3}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            DATE,
            TEXT NOT NULL,
            INTEGER
            );"""
            conexao.execute(comando_sql3)
            conexao.commit()
            print("sua tabela foi criada")

            comando_sql4 = f"""
            CREATE TABLE IF NOT EXISTS {nometb3}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            DATE,
            TEXT NOT NULL,
            INTEGER
            );"""
            conexao.execute(comando_sql4)
            conexao.commit()
            print("sua tabela foi criada")
            
    else:
         print("adios")
    
    

def read():
           
            comando = f"SELECT name FROM sqlite_master where type='table';"
            conexao.execute(comando)

            tabelas = cursor.fetchall()

            if tabelas:
                for tabela in tabelas:
                    print("Tabela", tabela[0])
            else:
                print("Nenhuma Tabela encontrada no banco atual")
                print("nenhuma tabela existente")

def update():

    tabela = input("QUAL O NOME DA TABELA QUE VOCÊ DESEJA ATUALIZAR? ")
    coluna = input("Qual coluna deseja alterar? ")
    novo_valor = input("Qual o novo valor? ")
    condicao = input("Atualizar qual linha? (ex: id = 1) ")

    # se o valor for texto, adicionamos aspas automaticamente
    if not (novo_valor.startswith("'") and novo_valor.endswith("'")):
        novo_valor = f"'{novo_valor}'"

    comando_DML_UPDATE = f"""
    UPDATE {tabela}
    SET {coluna} = {novo_valor}
    WHERE {condicao};
    """

    conexao.execute(comando_DML_UPDATE)
    conexao.commit()
    conexao.close()

    print("Dado atualizado com sucesso!")


def delete():
    deletesp = int(input("Gostaria de deletar algo específico? 1 para sim e 2 para não: "))

    if deletesp == 1:
        nome = input("Qual nome da tabela que deseja deletar algo específico? ")
        coluna = input("Qual coluna deseja deletar? ")
        condicao = input("Qual dado deseja deletar desta coluna? ")
  
        comandoddl = f"DELETE FROM {nome} WHERE {coluna} = ?"

        cursor.execute(comandoddl, (condicao,))
        conexao.commit()

        print("Registro deletado com sucesso!")

    elif deletesp == 2:
        deletarTable = int(input("Gostaria de deletar a tabela? 1 sim, 2 não: "))

        if deletarTable == 1:
            tabela = input("Digite o nome da tabela que deseja excluir: ")

            comandoDDL = f"DROP TABLE {tabela} ;"

            conexao.execute(comandoDDL)
            conexao.commit()

            print("Sua tabela foi excluída.")
        else:
            print("Operação cancelada.")
