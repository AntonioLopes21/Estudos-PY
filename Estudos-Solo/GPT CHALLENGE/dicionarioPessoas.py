# Lição 5: Dicionários e Manipulação de Dados
# Tarefa: Crie um programa que:

# Pergunte ao usuário quantas pessoas ele deseja cadastrar.
# Para cada pessoa, pergunte o nome e a idade.
# Armazene esses dados em um dicionário, onde o nome é a chave e a idade é o valor.
# Exiba todos os nomes e idades cadastrados.
# Calcule e exiba a média das idades.
# Dicas:
# Use um loop para coletar os dados de cada pessoa.
# Utilize um dicionário para armazenar os dados.
# Para calcular a média, você pode usar um loop ou a função sum() junto com len() para as idades.

numero_pessoas = int(input('digite o número de pessoas que você deseja cadastrar:'))

dicionario = {}

for i in range(numero_pessoas):
    nome_pessoa = input('digite o nome da pessoa:')
    idade_pessoa = int(input('Agora digite a idade da pessoa:'))
    dicionario[nome_pessoa] = idade_pessoa
    

for nome_pessoa, idade_pessoa in dicionario.items():
    print(f'{nome_pessoa}: {idade_pessoa}')


calculo_media = sum(dicionario.values()) / len(dicionario)

print(calculo_media)