#String e funções de texto
#como trabalhar com textos?

#email = "meuemail@gmail.com"

faturamento = 1000.24
custo = 754.23
lucro = faturamento - custo
margem_lucro = lucro / faturamento
#print(faturamento)
#print(custo)

# print("Faturamento da empresa:", faturamento)
# print('Custos da empresa:', custo)
# print('Lucro da empresa')

#print('Faturamento da empresa: {}, custo: {}, Lucro: {}'.format(faturamento, custo, lucro))

#+ recomendado
#print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}")

##########################################

#manipulacao de texto
email_cliente = "emailAleatorio@gmail.com"

#maiusculo
email_cliente = email_cliente.upper()
#print(email_cliente)

#minusculo
email_cliente = email_cliente.lower()
#print(email_cliente)

#encontrar @ dentro do texto
#print(email_cliente.find('@')) #posicao do @ no texto
#posicao 14

# find = -1 não tem @ no email

#tamanho do texto
#print(len(email_cliente)) # tamanho do email
#print(email_cliente[5]) # procurando o index

#print(email_cliente[-1]) # valor final


#########################################

#PEGAR UM PEDAÇO DO TEXTO
#print(email_cliente[14:]) #output: @gmail.com


#TROCAR PEDAÇO DO TEXTO REPLACE
novo_email = email_cliente.replace("gmail.com", "hotmail.com")
#print(novo_email) # emailAleatorio@hotmail.com



nome = "joao lira"
#
#primeira letra maiuscula
###print(nome.capitalize())
#primeira letra de cada palavra maiuscula
###print(nome.title())


#EXERCICIO


#meus métodos
#PEGAR O SERVIDOR DO EMAIL
email_cliente = "emailAleatorio@gmail.com"
servidor_email = email_cliente[15:]
###print(servidor_email)
#PEGAR O PRIOMEIRO NOME
###primeiro_nome = nome[0:4]
###print(primeiro_nome)
#PEGAR O SOBRENOME
sobrenome = nome[5:9]
###print(sobrenome)


#EXERCICIO do professor #dinâmico
posicao_arroba = email_cliente.find("@") + 1
servidor = email_cliente[posicao_arroba:]
print(servidor)

#pegar o primeiro nome
posicao_espaco = nome.find(' ')
primeiro_nome = nome[:posicao_espaco]
print(primeiro_nome)
#sobrenome 
sobrenome = nome[posicao_espaco+1:] #nome sem espaço
print(sobrenome)


#CASOS ESPECIAIS DE FORMATAÕA
#casos de formatação numérica em texto
                        #arredondamento
margem_lucro = round(margem_lucro, 2)  
                            #float 2 casas decimais                                                        #formatação
print(f"Faturamento: R${faturamento:.2f}, Custo: {custo:.2f}, Lucro: {lucro:.2f} margem: {margem_lucro:.0%}")







