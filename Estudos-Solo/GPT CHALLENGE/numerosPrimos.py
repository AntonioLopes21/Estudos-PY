def eh_primo():
  valor = int(input('Digite o valor que você quer verificar que é primo:'))
  if valor < 2:
    return f'o valor {valor} não é primo'
  
  for i in range(2, int(valor ** 0.5) + 1):
    if valor % i == 0:
      return f'o valor {valor} não é primo'
  
  return f'O valor {valor} é primo'

print(eh_primo())