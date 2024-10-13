#INPUTS E LISTAS

#inputs
#email_usuario = input('Digite seu email: ')
#nome = input("Digite seu primeiro nome: ")


# convertendo input para float
#faturamento = float(input("Digite o valor do faturamento: "))
#imposto = faturamento * 0.1
#print(imposto)

#email_usuario = input('Digite seu email: ')
#nome = input("Digite seu primeiro nome: ")

#print(f'{nome}, verifique seu email: {email_usuario} que enviamos um link de confirmação')


#print(email_usuario)
#print(nome)






#listas
#lista
vendas = [100, 40, 10, 1234, 203, 10, 4]

#soma dos elementos
total_vendas = sum(vendas)

#print("Valor total de vendas R$:",total_vendas)


#tamanho da lista
quantidade_vendas = len(vendas)
print(f"quantidade de vendas: {quantidade_vendas}")

#max e min
print(max(vendas))
print(min(vendas))

#elemento especifico de vendas
#pegar posicao
print(vendas[5])


#existe elemento?
lista_produtos = ["iphone", "airpod", "ipad", "notebook", 'apple watch']

#produto_procurado = input('Pesquise pelo nome do produto: ')

#filtro_pesquisa = produto_procurado.lower()
#print(filtro_pesquisa in lista_produtos)

#adicionar item na lista
lista_produtos.append('Apple watch')
#print(lista_produtos)

#remover item na lista
lista_produtos.remove('Apple watch')
#print(lista_produtos)
#pelo indice
lista_produtos.pop(0)
#print(lista_produtos)


#editar item na lista
precos = [1000, 1500, 3500]
#precos[0] = 6000

precos[0] = precos[0] * 1.5
#print(precos)



#se tiver repetido contar quantas vezes aparece na lista
nova_lista_produtos = ["iphone", 'iphone', 'Iphone', "airpod", "ipad", "notebook", 'apple watch']

#print('quantidades desse produto:',nova_lista_produtos.count('iphone'))


# ordenar lista

#ao contrario
nova_lista_produtos.reverse()
nova_lista_produtos.sort(reverse=True)
print(nova_lista_produtos)
print('\n\n\n')
#na ordem
nova_lista_produtos.sort()
print(nova_lista_produtos)

#vendas em ordem
vendas.sort()
print(vendas)

#vendas no reverso
vendas.sort(reverse= True)
print(vendas)