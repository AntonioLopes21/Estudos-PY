# import response
import requests

url = 'https://loteriascaixa-api.herokuapp.com/api/megasena'

resposta = requests.get(url)

if resposta.status_code == 200:
    
    dados = resposta.json()
    
    for itens in dados:
        ganhadores = itens['premiacoes']
        regiao = str(itens['local'])
        
        print(f'Local: {regiao}\nGanhadores: {ganhadores}')


