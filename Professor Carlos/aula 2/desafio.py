#solicitar emprestimo ao banco

# se o valor for menor ou igual a 50% do salario
#emprestimo aprovado

# se não o valor do emprestimo for menor ou igual a 75% so salario a situacao
#vai ficar em analise

#se nao o emprestimo não vai ser aprovado


salario = float(input("Qual o seu salário? diga o valor em inteiro"))
emprestimo = float(input("qual o valor do emprestimo?"))


if emprestimo <= salario*0.5:
    print('empréstimo aprovado')

elif emprestimo <= (salario*0.75):
    print("pedido em análise")
    
else:
    print('Empréstimo negado')


