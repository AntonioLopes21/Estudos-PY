#Dicionários

#objetivo e como funcionam
lista_produtos = ['airpod', 'ipad', 'iphone', 'macbook']
precos = [2000, 9000, 5000, 11000]

#informações com rótulo as informaçoes 
#USAR DICIONÁRIO

dic_produtos = {"airpod": 2000,
                'ipad': 9000,
                'iphone': 5000,
                'macbook': 11000}


#como pegar elemento #traz info rotulada
#print(dic_produtos['airpod'])


#editar elemento
dic_produtos['iphone'] = dic_produtos['iphone'] * 1.3

#print(dic_produtos)

#quantidade de itens
print(len(dic_produtos))


#remover item do dicionário
#dic_produtos.pop('airpod')
print(dic_produtos)


#adicionar item dicionarioo substitui ou cria
#ele edita ou cria o elemento 
dic_produtos['apple watch'] = 2500
print(dic_produtos)


#VERIFICAR SE ITEM EXISTE NO FUNC

#sempre procura nas chaves do dicionário
if 'iphone' in dic_produtos:
    print('existe produto')
else:
    print('não existe o produto')


#VERIFICAR SE CHAVE EXISTE
if 9000 in dic_produtos.values():
    print('existe o valor')
else:
    print('não existe')

#VERIFICAR SE VALOR EXISTE NOS VALORES DO DICIONARIO

#cadastrar o produto e o novo produto {se o prod existir}
#caso exista ele vai editar o produto

dic_produtos_games = {'watch dogs': 2000}

#nome_produto = input('Nome do produto: ')
#preco_produto = input('Preço do produto: ')

#nome_produto = nome_produto.lower()
#preco_produto = float(preco_produto)

#chave e preco dinâmicos

#cadastrando
#dic_produtos[nome_produto] = preco_produto
#print(dic_produtos)


#alem disso o programa tem que atualizar o preço de todos os produtos para 
#os novos valores -> novos valores = 10% a mais do valor
produto = "airpod"

# print(novo_preco)

# print(dic_produtos)

print('\n\n')
for produto in dic_produtos:
    novo_preco = dic_produtos[produto] * 1.1
    dic_produtos[produto] = novo_preco
    
print(f'{dic_produtos}')

# if cadastro_produto and preco_produto in dic_produtos_cadastrados:
#     print('O produto já se encontra no dicionário')
# else:
#     dic_produtos_cadastrados = dic_produtos_cadastrados.append(cadastro_produto)
#     dic_produtos_cadastrados = dic_produtos_cadastrados.append(preco_produto)
#     preco_produto = preco_produto * 0.1
#     print('produto adicionado com sucesso')
