#palíndromo é uma palavra que ao contrário é igual
frase_palavra = input('Digite a frase ou palavra:')
#                       palavras curtas -- palavras sem o espaço
palavra_formatada = '' .join(frase_palavra.lower().split(' '))
palavra_invertida = palavra_formatada[::-1]

if palavra_formatada == palavra_invertida:
  print('É um palíndromo!')
else:
  print('Não é um palíndromo.')
