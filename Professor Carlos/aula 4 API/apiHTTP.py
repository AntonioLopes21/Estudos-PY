
#importar a ferramenta

#url da api

#endpoints
#Pontos da api
# Resources
# JSONPlaceholder comes with a set of 6 common resources:

# /posts	100 posts
# /comments	500 comments
# /albums	100 albums
# /photos	5000 photos
# /todos	200 todos
# /users	10 users

# headers = {
#     'Autorization': 'Bearer sdadsadsadsad',
#     'Content-Type': 'application/json',
#     'User-Agent' : 'Mozilla/5.0'
# }


import openpyxl
import requests
#fazendo uma requisição get para a api
import openpyxl


url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)


print(response)


if response.status_code == 200: #truew
    users = response.json()
    
    #criar um arquivo .excel
    workbook = openpyxl.Workbook()
    
    sheet = workbook.active #criar na aba ativa
    
    #adiciona cabeçalhos 
    sheet.append(['ID', 'NOME', 'EMAIL', 'EMPRESA'])
    
    for user in users:
        sheet.append([user['id'], user['name'], user['email'], user['company']['name']])
 
    
    #salvar
    workbook.save('teste proa.xlsx')
    print('salvei o negócio')
    
else:
    print('deu erro:',response.status_code)
    
    
 #percorrendo dados   
    # for i in users:
    #     print(f'Usuário: {i['username']}\nNome: {i['email']}\nEndereço: {i['address']['suite']}\n')






###salvando dados em excel


#É USUAL UMA MATRIZ DE 3 DIMENSÕES PARA ARMAZENAR ESTADOS AO LONGO DO TEMPO?



