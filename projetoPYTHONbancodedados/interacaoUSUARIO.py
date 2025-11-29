from time import sleep
from connectDB import (cursor,conexao)
from Crud import read

def menu_interacao():
    igual = "$"*10
    sistema = True
    while sistema != False:

        for animacao in range(10):
            sleep(0.1)
            print("*")
        
        sairsistema = int(input("voce deseja sair do sistema?: 1 para sim e 2 para nao: "))
        criarTabela = int(input("deseja criar uma tabela? 1 para sim e 2 para nao: "))

        if criarTabela == 1:
            sistema = False
            comando_sql = f"""
            CREATE TABLE IF NOT EXISTS bruninho(
            TEXT NOT NULL,
            INTEGER
            )"""
            conexao.execute(comando_sql)
            conexao.commit()
            
        else:
            print("adios")

        if sairsistema == 1:
            sistema = False
            print("voce saiu do sistema")

        elif sairsistema == 2:
            vertabela = int(input("gostari de verificar se existem as tabelas 1 para sim e 2 para nao: "))

                
        
        elif vertabela == 2:
            read()
            sistema = False  
        
        else:
            print('numero digitado invalido')
        
