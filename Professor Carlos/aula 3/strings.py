mensagem = 'hello world'

primeiro_nome = 'antonio'
segundo_nome = 'de padua'

nome_completo = primeiro_nome + ' ' + segundo_nome

#rint(nome_completo)

print(nome_completo[0])
print(nome_completo[-1])

#               start:stop: pule de 2 em 2
print(nome_completo[0:7:2])

print(len(mensagem))

print(mensagem.upper())
print(mensagem.lower())
#primeira letra maiuscula
print(mensagem.capitalize())
#maiusculo de cada palavra
print(mensagem.title())
#separa o texto em lista
#cada palavra vida elemento de lista
print(mensagem.split())

mensagem2 = 'o proa é massa'


#separa as palavras de acordo com a virgula
#['o,', 'proa,', 'é,', 'massa']
print(mensagem2.split(' '))

#verificação que retornará palavra de noia
if 'mas' in mensagem2:
    print('palavra de noia')
else: 
    print('tá de boa')



#substitui o massa por foda
mensagemx = mensagem2.replace('massa', 'foda')
print(mensagemx)


#strip
texto2 = '    onde vai usar isso?      '
texto2 = texto2.strip()
print(texto2)











