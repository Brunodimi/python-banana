from time import sleep

def menu_interacao():
    igual = "$"*10
    sistema = True
    while sistema != False:

        for animacao in range(10):
            sleep(0.1)
            print("*")
        
        sairsistema = int(input("voce deseja sair do sistema?: 1 para sim e 2 para nao: "))
        
        if sairsistema == 1:
            sistema = False
            print("voce saiu do sistema")

        elif sairsistema == 2:
            vertabela = int(input("gostari de verificar se existem as tabelas 1 para sim e 2 para nao: "))
            
        elif vertabela == 1:
            print("nenhuma tabela existente")
            sair = int(input("deseja sair do sistema?: 1 par sim e 2 para nao: "))
        
        elif vertabela == 2:
            sistema = False
        
        elif sair == 1:
            sistema = False
            print("voce saiu do sistema")
        
        elif sair == 2:
            sistema = True        
        
        else:
             print('numero digitado invalido')
        
            
           
            
       
        
        
    pass

