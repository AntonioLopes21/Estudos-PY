#TRATAMENTO DE CONDIÇÕES
#vendas = float(input("Digite o valor das suas vendas: "))
meta1 = 1300.0
meta2 = 2000.0
meta3 = 5000.0

#if vendas >= meta3:
    #print('O funcionário merece o bônus!')
    #bonus = 0.5  * vendas #50% bonus
    #print(f"Bônus do vendedor 50% : {bonus}")

#elif vendas >= meta2: 
    #print('O funcionário merece o bônus!')
    #bonus = 0.2  * vendas #20% bonus
    #print(f"Bônus do vendedor 20%: {bonus}")
    
#elif vendas >= meta1: 
    #print('O funcionário merece o bônus!')
    #bonus = 0.1  * vendas #10% bonus
    #print(f"Bônus do vendedor 10%: {bonus}")
    
#else:
    #print('O funcionário não vai ganhar bônus!')
    


#print("Acabou o programa")

## && e || -> no py é and ou or


lista_produtos = ['airpod', 'ipad', 'iphone']

produto_procurado = input("Digite o nome do produto:")

produto_procurado = produto_procurado.lower()

if produto_procurado in lista_produtos:
    print('O produto foi encontrado!')
else:
    print("Adicionaremos o item na lista de produtos em em breve o traremos!")
    lista_produto = lista_produtos.append(produto_procurado)

print(lista_produtos)


