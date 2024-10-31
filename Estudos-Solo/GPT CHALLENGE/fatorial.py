def formula_fatorial():
  fatorial = int(input('Digite um número inteiro:'))
 
  if fatorial == 0:
    return 'O resultado do fatorial de 0 é: 1'
  
  resultado_fatorial = 1
  for i in range(1, fatorial + 1):
    resultado_fatorial = resultado_fatorial * i

  return f'O valor de fatorial {fatorial} é:{resultado_fatorial}'  

print(formula_fatorial())