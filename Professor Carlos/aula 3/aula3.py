dic = {}

print(type(dic))

dic_pernambuco = {"Sport": 41, "Santa Cruz": 29, "Nautico":21}
#chaves do lado esquerdo e no direito valores

#dicionários são pares de chaves e valores
print(dic_pernambuco['Sport'])

print(dic_pernambuco)


dic = {} #dicionário vazio
print(type(dic)) # <class 'dict'>

#dicionário tupla
dic_tupla = {"tupla":{"aqui não muda!"}}
#print(dic_tupla)

#           chave com valor de dicionário
dic_times = {"sport": {'estádio': 'ilha do retiro', 'cidade': 'Recife'}, 'lista': [1,2,3,4,5,678]}

dic_times_outro = {'Sport': 49, 'Santa': 21}
print(dic_times_outro)

dic_times_outro['Naútico'] = 19 #add par chave:valor ao dic
print(dic_times_outro)

#insert e append adicionam dados na lista
#LISTA = append, insert

#append adiciona ao fim
#insert adiciona em uma posição específica

# TUPLA NÃO TRABALHA COM INDICE
tupla = (1,2,3,4,5,6)
dicionario = {'painho': 21}
lista = [12, 'melo', 1.5, True]
#tupla sequencia ordenada de valores
print(tupla[1]) # = 2

#se quiser pesquisar valor passa o indice em lista e tupla
#no dicionário tem que passar a chave

#PAGINA 77 DO SLIDE
#ESTRUTURA DE DADOS



#ADICIONAR VALORES 
dic_times_outro['São Paulo'] = 50
print(dic_times_outro)


#RESGATANDO VALORES DE UM DICIONÁRIO

#1 maneira de pegar valores em um dic
qtd_titulos = dic_times_outro.get('Sport')
print(qtd_titulos)

#get retorna valores de um dicionário
#2 maneira de pegar valores de um dic
dic_times_outro['Corinthians'] = 41
print(dic_times_outro)

#no DJANGO UTILIZA MUITO O GET

#retorna uma lista de chaves
print(dic_times_outro.keys())
#retorna valores
print(dic_times_outro.values())

teste = list(dic_times_outro.keys())
teste2 = list(dic_times_outro.values())

print(teste)
print(teste2)

print(teste + teste2)





