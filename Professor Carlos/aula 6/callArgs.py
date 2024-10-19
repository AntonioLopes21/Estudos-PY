def somar_todos(*args):
    return sum(args)

print(somar_todos(2,3,23,3,123,32))


def exibir_detalhes(a,b,**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave} : {valor}')
    

exibir_detalhes(a = 2, b = 1,nome = 'Carlos', id = '30', cidade='São Paulo')