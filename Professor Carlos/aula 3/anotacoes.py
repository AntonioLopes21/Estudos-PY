aluno = {
    'nome': 'Paulin',
    'idade': 21,
    'profissao': 'dev',
    'notas': [9,7,8,9]
}
#só visualiza
print(aluno['idade'])

#armazena valor para futura alteração
teste = aluno['idade']
print(aluno['idade'])

#atualizando valores
aluno['idade'] = 30

print(aluno)


#buscando valores no dicionário

#verifica a existência da chave
#tratamento
print('telefone' in aluno) # retorna falso


consulta = 'idade' 
#tratamento
if consulta in aluno:
    print('tem na lista')
else:
    print('Não tem na lista')


#print(escolha in aluno)#retorna true

#deletar valores
#del não dá para armazenar na variável
###3#####del aluno['notas']
#print(aluno)

#retira o que indica

#pop dá para deletar e armazenar em uma variavel
#delecao =  aluno.pop("idade")
##############print(aluno)
#
#############print(delecao) #mostra o valor deletado
#
#deleta o ultimo

#recomendado não usar o popitem()
aluno.popitem()
#print(aluno)

#fastAPI #### PESQUISAR SOBRE


#verificando valores de chave:valor
exemplo = aluno.items()
print(exemplo) #
#dict_items([('nome', 'Paulin'), ('idade', 30), ('profissao', 'dev')])

#consultando pares
#converter dicionário para lista e pesquisar o indice
print(list(exemplo)[0])



#del d['apples'] #deleta apples
#print('apples' in d) # return false por ter deletado antes

d = {'apples': 14, 'bananas': 34, 'grapes': 12, 'castanha': 11}

#sort é um método de listas
fruits = d.keys()
fruits = list(fruits)
fruits.sort()

#dicionario não tem o método sort

print(fruits)











