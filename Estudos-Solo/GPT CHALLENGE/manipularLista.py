permissao_loop = True

#função que soma a média da lista
def somar_media(lista):
  resultado = sum(lista)/len(lista)
  if resultado < 5 :
    situacao_aluno = 'Reprovado'
  elif resultado >= 5 and resultado < 6:
    situacao_aluno = 'Recuperação'
  else:
    situacao_aluno = 'Aprovado'
  
  return f'O resultado da média do aluno é:{resultado:.2f} e o aluno foi {situacao_aluno}'


#loop das notas
while permissao_loop:
  contador = 0
  lista = []
  resposta = int(input('Quantas notas você deseja receber? ou digite -1 para sair do programa:'))
  
  if resposta == -1:
    permissao_loop = False
    break
  
  else:
    for i in range(resposta):
      nota = int(input(f'Digite a nota n°{i + 1}:'))
      lista.append(nota)
      print(lista)
    #chamando a função após o loop
    print(somar_media(lista))

print('Obrigado por utilizar o programa!')     
