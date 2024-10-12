#estrutura de dados 

#estrutura base de uma lista
minha_lista = [1,2,3, 'quatro', True]
#algo que faça sentido para a proposta

lista_vazia = []
lista = [1, 1.5 , True, 'Strings', ['lista', 'lista 2', 1, 2, 3]]
#print(type(lista), lista)
lista = 12

#dicionario



#tupla

lista2 = list((1,2,'3'))
#print(lista2)


lista3 = ['c', 4.56, True, 'true', "vamos aprender", ["outra", "lista", "interna"], lista2]

#print(lista3)

lista4 = ["primeiro", "segundo", "terceiro"]

#fatiamento de listas
#obs -> 
#print(lista3[5][1][3]) # vai trazer a lista
#forma de percorrer sequencias em listas

#start stop stap
#print(lista3[0:3:1])
#print(lista3[3:5:2])

#adicionar elementos na lsita

listax = []

listax.append('Py')
listax.append('Java') #final
listax.append('C#')
#print(listax)

#append adiciona no final

#insert adiciona no começo(0, "titulo")
listax.insert(2, 'C++')
#print(listax)

#insert adiciona em uma posicao especifica

listax.remove("Java")
#print(listax)

#assim como o append

listax.pop()# exclui do final
#print(listax)

#aqui é para saber o indice do elemento
indice = listax.index("C++")
#print(indice)

#percorre a lista e deleta pelo indice
del(listax[1])
print(listax)

#adicionando no final
listax.append('C#')

#editar valor
listax[1] = "Java"
#print(listax)


#inverter posições de valores
listax.reverse()
#print(listax)


listax.append('Ruby')
#sort
#ordena tanto numeros como valores
listax.sort()
#print(listax)


listax.append("A")
listax.append('B')
listax.sort()
#print(listax)


#algorítmo de ordenação
teste3 = [1,5,8,4,7]
teste3.sort()
##print(teste3)


#len -> tamanho
#print(len(lista3))

#verificar valores na lista
#se tiver me diga que está lá o valor

#condicional -> if else e algo que percorra lista

#x = int(input('digite um valor:'))
#if x in teste3:
 #   print("tem aqui!")
#else:
#    print("não tem!")
    
#ler a questão, interpretar e codar

#concatenação de listas

#tuplas são imutáveis

tupla = (1,2,3,"quatro")
print(tupla[0])
print(tupla[3])

print(4 in tupla)
print('quatro' in tupla)

print(tupla.count(4))
#count conta quantas vezes
#aquilo apareceu na tupla


