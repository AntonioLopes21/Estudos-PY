
def soma_numeros():
  valor = int(input('Digite o valor inteiro:'))
  
  contador = 0
  for i in range(valor + 1):
    contador = contador + i
    print(contador)
  return f'A soma de todos os números até {valor} é: {contador}'


print(soma_numeros())