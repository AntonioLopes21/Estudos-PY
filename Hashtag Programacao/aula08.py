#linguagem de código aberto

#biblioteca 
#pacote de código instalada no pc ou para ser instalada
#usar funcionalidades já criadas por outras pessoas


#para trabalhar com arquivos de excel
#import pandas #trabalhar em arquivos excel com base de dados
#import openpyxl #editar arquivos em excel

#import pypdf #biblioteca de pdf
#######################################



#print("Hoje é:",datetime.date.today(),"\n\n\n\n")

import os
import datetime

#EXERCÍCIO
lista_arquivos = os.listdir("Hashtag Programacao/aula08/arquivos")

#listando todos os arquivos do diretório
for arquivo in lista_arquivos:
    if ".txt" in arquivo: 
        print("movimentar:",arquivo)
        
        if "22" in arquivo:
                                            #nome antigo                                        #nome novo
            os.rename(f"Hashtag Programacao/aula08/arquivos/{arquivo}", f"Hashtag Programacao/aula08/arquivos/22/{arquivo}")
            print("Movimentado para a pasta 22")
        else: 
            print("Movimentado para a pasta 23")
            os.rename(f"Hashtag Programacao/aula08/arquivos/{arquivo}", f"Hashtag Programacao/aula08/arquivos/23/{arquivo}")

#movimentar arquivos txt sobre as pastas




