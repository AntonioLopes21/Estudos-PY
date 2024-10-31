def ehPar():
  valor = int(input('Digite o valor:'))
  if valor % 2 == 0:
    return f'o número {valor} é par'
  else:
    return f'o número {valor} é impar'
  
print(ehPar())