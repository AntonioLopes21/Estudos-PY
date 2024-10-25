# Soma dos primeiros N números naturais
# Problema: Escreva um programa que peça um número inteiro n e some todos os números naturais até esse valor.

numero_inteiro = int(input('Digite um número inteiro:'))

def soma_naturais(inteiro):
    contador = 0
    for numeros in range(inteiro + 1):
       contador = contador + numeros
           
    return contador

print(f'A soma dos inteiros é:{soma_naturais(numero_inteiro)}')
