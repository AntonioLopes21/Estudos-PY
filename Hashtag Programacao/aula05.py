#LAÇO DE REPETIÇÃO FOR

#
lista_vendas = [1000, 500, 700, 1500, 200, 2350]

# lista_vendas.sort()
# print(lista_vendas)

venda = 1500
meta = 1200
percentual_bonus = 0.1


for venda in lista_vendas:

    if venda >= meta: 
        bonus = percentual_bonus * venda
    else:
        bonus = 0
        
    print(f"bônus para funcionário que vendeu:{venda}\n",bonus)
    
print("fora do for")


# for i in range(10):
#     print(i + 1, "vezes")
    
# for venda in lista_vendas:
#     #tudo o que quer que seja executado várias vezes
    
#     print("vendedor x",venda.sort)