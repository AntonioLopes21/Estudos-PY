palavra = 'Colombiana'

lista_vogais = ['a','e', 'i', 'o', 'u']

for letras in palavra:
    if letras in lista_vogais:
        
        contador = 0
        print(f'possui a vogal:{letras}')
        

lista_pares = []
lista_impares = []

for numeros in range(101):
    if numeros %2 == 0:
        lista_pares.append(numeros)
    else:
        lista_impares.append(numeros)
        
print(f'Lista de pares:\n{lista_pares}\n\n\n')
print(f'Lista de ímpares:\n{lista_impares}')

conta = 0
for i in lista_impares:
    conta += i

print(f'Conta dos números ímpares:{conta}')

for i in lista_pares:
    conta += i

print(f'Conta dos números Pares:{conta}')
