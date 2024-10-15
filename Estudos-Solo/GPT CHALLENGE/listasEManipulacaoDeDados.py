#lista e manipulacao de dados
lista = []
for i in range(5):
    valor = int(input(f'Digite o {i+1}º valor: '))
    lista.append(valor)


#função bonus -> ordenar do menor para o maior
lista.sort()
print(lista)

valor_maximo = max(lista)
valor_minimo = min(lista)

valor_media = 0


#ERRADO
# for i in range(5):
#     if valor_media <= len(lista):
#         i + valor_media
#     if valor_media == len(lista):
#         valor_media/len(lista)

media_lista = sum(lista) / len(lista)
print(f'A média da lista foi:{media_lista}')
print(f'O maior valor foi: {valor_maximo}')
print(f'O menor valor foi: {valor_minimo}')

