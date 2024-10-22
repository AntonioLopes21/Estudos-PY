media = 0
n1 = n2 = n3 = n4 = 0.1

nome, idade, estado = 'Paulo', 21, True

#função type()
print(type(media))
print(type(n2))
print(type(nome))
print(type(estado))
print(type(1+2j)) #complex -> dado número complexo
#dado utilizado em circuitos elétricos

#função isinstance()
a = 10
b = 'sol'
#intellisense
print(isinstance(a, int)) # retorna True
#verifica se a variável é de um tipo
print(isinstance(b, (int, float))) #retorna false
print(isinstance(b, (int, float, str))) #retorna TRUE 
#é booleano


#ctrl + k + u -> descomenta o código

