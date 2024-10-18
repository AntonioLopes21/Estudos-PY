opcao1 = int(input('Digite o número inteiro:'))
opcao2 = int(input('Digite o número inteiro:'))
opcao3 = int(input('Digite o número inteiro:'))
opcao4 = int(input('Digite o número inteiro:'))
opcao5 = int(input('Digite o número inteiro:'))

def soma_numeros(n1,n2,n3,n4,n5):
    return f'A soma dos números é:{n1+n2+n3+n4+n5}'
    
def media_numeros(n1,n2,n3,n4,n5):
    return f'A média dos números é:{(n1+n2+n3+n4+n5)/5}'

print(soma_numeros(opcao1, opcao2, opcao3, opcao4, opcao5))
print(media_numeros(opcao1, opcao2, opcao3, opcao4, opcao5))
        