# Desafio 3: Ordenar Lista

# Nível: Médio

# Objetivo: Criar um programa que ordene uma lista de números.

# Requisitos:

# 1. Leia 5 números usando input.
# 2. Ordene a lista em ordem crescente.
# 3. Exiba resultado.

lista = [1,54,23,53,2]

def organizar_lista(lista):
    lista.sort()

    return lista

print(organizar_lista(lista))

