#crie um programa que continue pedindo para o usuário realizar uma operacao
#dois numeros e operação desejava(+ - / *)
#o laço deve parar quando o user digitar 'sair'
tentativa = True

while tentativa:
    num1 = int(input('Digite o primeiro número:'))
    num2 = int(input('Digite o segundo número:'))
    operacao = input('Digite o valor da operação: +, -, /, * ou digite sair para encerrar o programa:')
    
    if operacao == '+':
        resultado = num1 + num2
        print(resultado)
        
    elif operacao == '-':
        resultado = num1 - num2
        print(resultado)
    elif operacao == '/':
        resultado = num1 / num2
        print(resultado)
        
    elif operacao == '*':
        resultado = num1 * num2
        print(resultado)
        
    elif operacao == 'sair':
        tentativa = False
        
print('programa finalizado')