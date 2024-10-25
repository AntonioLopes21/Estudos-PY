# Soma de dois números
# Problema: Crie um programa que peça dois números ao usuário e imprima a soma deles.

def soma(): 
    a = int(input('Digite o valor de A:'))
    b = int(input('Digite o valor de B:'))
    
    return a + b

print(soma())


# Par ou Ímpar
# Problema: Escreva um programa que peça um número inteiro e diga se ele é par ou ímpar.

def ehPar(num):
    if num %2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é impar')
        
ehPar(5) 