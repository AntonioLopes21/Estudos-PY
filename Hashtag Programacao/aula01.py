#print na tela

#executa programa de cima para baixo

# print('Hello world!')
#print("Eu tenho", 21, "anos de idade")
#############################################
#variaveis


#faturamento = 1000
#custo = 700
#lucro = faturamento - custo
#print("O faturamento foi de", faturamento, "\nO custo foi de", custo,"\nAo final de tudo o lucro que a empresa obteve foi de", lucro)
#############################################

###tipos de variaveis

#faturamento = 1200 # INT -> numero inteiro

#custo = 750.23 # FLOAT ->  numeros com casa decimal

###STRING
#usuario = input("Digite o seu nome de usuário:")
#mensagem = print("Bem vindo,", usuario,"!")
#print(mensagem)

###
#teve_lucro = True;

faturamento = 1200
custo = 750
imposto = faturamento * 0.1

lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento


#arredondamento                           variavel     casas decimais
#print("A margem de lucro foi de:", round(margem_lucro, 2))

#percentual
#MOD -> % resto da divisão
#print(10 % 3)

#========================================
#TEMPO DE CONTRATO
meses = 170
tempo_contrato = meses 
tempo_anos = meses / 12
tempo_meses = meses % 12
print("Tempo em anos:",int(tempo_anos))
print("Tempo em meses:", tempo_meses)

