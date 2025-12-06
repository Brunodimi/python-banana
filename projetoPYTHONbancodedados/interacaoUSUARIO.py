from time import sleep
from connectDB import (cursor,conexao)
from Crud import read,create,update,delete

def menu_interacao():
    igual = "$"*10
    sistema = True
    while sistema != False:

        for animacao in range(10):
            sleep(0.1)
            print("*")
        
        
        sistema = int(input("voce deseja sair do sistema?: 1 para sim e 2 para nao: "))

        if sistema == 1:
            sistema = False
            break
            
        elif sistema == 2:
            sistema = True
                
            sistema1 = True
            while sistema1 != False:

                vertabela = int(input("Gostaria de verificar se existem tabelas? 1 para sim e 2 para não: "))

                if vertabela == 1:
                    read()

                create1 = int(input("Gostaria de criar uma tabela? 1 para sim e 2 para não: "))

                if create1 == 1:
                    create()

                elif create1 == 2:
                    deletar = int(input("Gostaria de deletar a tabela? 1 para sim e 2 para não: "))

                    if deletar == 1:
                        delete()
                        break

                    elif deletar == 2:
                        add = int(input("Gostaria de adicionar algo na tabela? 1 para sim e 2 para não: "))

                        if add == 1:
                            update()
                            break

                        elif add == 2:
                            sistema1 = False

                        else:
                            print("Número digitado inválido")

                    else:
                        print("Número digitado inválido")

                else:
                    print("Número digitado inválido")


                b = int(input("Deseja interagir com o banco novamente? 1 = sim / 2 = não: "))

                if b == 1:
                    sistema1 = True

                elif b == 2:
                    sistema1 = False

                else:
                    print("Número digitado inválido")


    

    for animacao in range(10):
                sleep(0.1)
                print("*")
    print("Voce saiu do sistema")
