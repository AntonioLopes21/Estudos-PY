#crie uma funcao para retornar e exibir a soma de números pares usando o while
def soma_de_pares(args):
    soma = 0
    i = 0
    while i < len(args):
        soma += args[i]
    i+=1
    
    print('A soma dos números pares é', soma)
    
