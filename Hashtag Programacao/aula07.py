#Funções no python

lista_precos = [1500,100,600,3000]
#imposto
#aliquota 1 -> ir - 0.2
#aliquota 2 -> ir - 0.15
#aliquota 3 -> csll -> 0.05

preco = 1500

def calcula_imposto_total(preco):
    if preco <= 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_ir = 0.3 * preco
    imposto_iss = 0.15 * preco
    imposto_csll = 0.05 * preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    
    return imposto_total
    

for preco in lista_precos:
    imposto_total = calcula_imposto_total(preco)
    print(f"imposto total sobre o produto de R${preco}: R$",imposto_total)