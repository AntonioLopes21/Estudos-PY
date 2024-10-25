# Contagem de Palavras

# Problema: Solicite uma frase ao usuário e conte quantas palavras ela contém.


frase = input('digite uma frase:')

frase_dividida = frase.split()
numero_palavras = len(frase_dividida)
print(f'a frase possui:{numero_palavras} palavras')