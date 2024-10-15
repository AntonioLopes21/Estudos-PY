#crie um dicionario chamado aluno com as chaves
#nome, idade e nota. preencha com valores apropriados


aluno = {
    'nome': 'Paulin',
    'idade': 21,
    'nota': [10,9,6,9]
}

print(aluno)


#adicione uma nova chave curso ao dicionario 
#com o valor ciencia da computacao

aluno['curso'] = 'Ciência da computação'
print(aluno)

#
#acesse e imprima o valor da chave nome
#no dicionário aluno
#
print(aluno['nome'])
aluno = list(aluno)

print(aluno[0])

#verifique se a chave ''idade está no dicionário e imprima o resultado

print('idade' in aluno) # return true
# if 'idade' in aluno:
#     print('a idade é:', 'idade')
# else:
    