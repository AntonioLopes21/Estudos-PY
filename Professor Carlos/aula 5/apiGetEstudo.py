#diferença do fetch e do axus

import requests

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)


print(response)


if response.status_code == 200: #truew
    users = response.json()
           
    for user in users:
        lista_nome = str(user['name'])
        lista_email = str(user['email'])#percorre dicionário com chaves  
        lista_nome_empresa = str(user['company']['name'])
        
        print(f'Nome: {lista_nome}\nEmail: {lista_email}\nEmpresa: {lista_nome_empresa}\n\n')
    