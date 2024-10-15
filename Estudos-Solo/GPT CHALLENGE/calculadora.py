def calculadora(num1, num2, escolha) :
    if escolha == 1:
        return f'O valor da soma de {num1} + {num2} = {num1 + num2}'
    elif escolha == 2:
        return f'O valor da subtração de {num1} - {num2} = {num1 - num2}'
    elif escolha == 3:
        if num1 == 0 or num2 == 0:
            print('Erro! não se pode dividir por zero: infinity')
        else:
            return f'O valor da divisão de {num1} / {num2} = {num1 / num2} e o resto é {num1 % num2}'
    elif escolha == 4:
        return f'O valor da multiplicação de {num1} x {num2} = {num1 * num2}'
    else:
        return 'Não consegui entender o que você está fazendo'
    

num1 = int(input('Digite o seu primeiro valor:'))
num2 = int(input('Agora digite o segundo valor:'))
escolha = int(input ('1. Adição\n2.Subtração\n3.Divisão\n4.Multiplicação'))

print(calculadora(num1,num2,escolha))