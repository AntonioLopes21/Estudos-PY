#dado um texto conte para mim quantas vogais existem

#segundo ponto
#preciso saber a quantidade de vogais que se repetem: a:3 e:2

lista_vogais = ['a', 'e', 'i', 'o', 'u']

texto = 'Coelho'

# a = 0
# e = 0
# i = 0
# o = 0
# u = 0

# for i in texto:
#     if i in a:
#         a += 1

        
#     elif i in e:
#         e += 1
    
#     elif i in i:
#         i +=1
        
#     elif i in o:
#         o+=1
        
#     elif i in u:
#         u+=1
#     else:
#         print('não é vogal')



# print(f'Número de vogais na palavra:a {a}, e: {e}, i: {i}, o: {o}, u: {u}')    

texto = 'Paralelepipedo'
contador = 0


vogais = {'a':0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for vogal in texto:
    if vogal in vogais:
        
    print(f'Número de vogais no texto:{vogais}')

for i in texto:
    if i in vogais:
        vogais[i] += 1
        
        
print(f'(a:{vogais['a']}), (e:{vogais['e']}), (i:{vogais['i']}), (o:{vogais['o']}, (u:{vogais['u']}))')

