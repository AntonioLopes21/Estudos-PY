#laço while

contador = 1

while contador <= 5:
    print(contador)
    contador += 1
    
print('\n\n\n\n')
# lista = [1,2,3,4,5,6,7,8,9,10]

# i = 0
# while i < len(lista):
#     if lista[i] <=100:
#         i +=1
#         print(i)


contador = 10

while contador >=1:
    print(contador)
    contador -= 1
    
print('\n\n\n\n\n\n')



# numbers = ['0','1','2','3','4','5','6','7','8','9']

# while True:
#     nome = input('digite o seu nome:')
    
#     if len(nome) == 0 or nome in numbers:
#         print('o nome não pode ser vazio')
#         break
  
  
  ##############################  
# cont = True

# while cont:
#     nome = input('digite o seu nome:')
    
#     if nome == '0':
#         print('o nome não pode ter 0')
#         cont = False
#

#########################################
import random

numero_secreto = random.randint(10)

tentativa = ''

while tentativa != numero_secreto:
    tentativa = int(input('Digite um número:'))
    
print('boa!')