# #sintaxe for

# sequencia = ['fila', 'da', 'pauta',1,2,5,6,7,5]

# for variavel in sequencia:
    
#     print(variavel)
    
    
frutas = ['Maçã', 'Framboesa', 'Morango', 'Melancia', 'Banana', 'Laranja']
# print(frutas.index('Framboesa'))

for fruta in frutas:
    indice = frutas.index(fruta)
    print(f'Indice: {indice} Fruta: {fruta}')
    
    
print('\n\n\n\n')

for i in range(1,12,2):
    print(i)
    
nome = 'Valleska'
novoNome = nome.replace('Valleska', 'Mentirinha')
print(novoNome)

##########################
soma = 0

for i in range(1,11):
    soma += i # soma = soma + i  i = 1 i = 2 i = 3
    print('O valor de i:',i)
    print(soma)
print('O resultado da soma é:', soma)




print('\n\n\n\n\n\n')

