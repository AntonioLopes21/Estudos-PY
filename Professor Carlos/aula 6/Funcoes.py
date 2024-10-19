#função é um bloco de código que realiza tarefa específica e torna fácil a reutilização de código
# def = define

def saudacao():
    print('Hello world guys')
    
saudacao()

#função recursiva é uma
#função que muda ela mesma

def somar(a, b):
    print(a+b)
    
def subtrair(a, b):
    return a - b 

somar(2,3)

subtrair(3,2)
print(subtrair(2,3))

valor = subtrair(5,10)
print(valor)

print(valor + 10)