import requests
import openpyxl

url = 'https://loteriascaixa-api.herokuapp.com/api/megasena'
response = requests.get(url)

excel = openpyxl.Workbook()

planilha = excel.active
planilha.append(['NUMEROS SORTEADOS', 'DATA SORTEIO'])


if response.status_code == 200:
    megasena = response.json()
    
    for dezenas in megasena:
        dezena = str(dezenas['dezenasOrdemSorteio'])
        data = str(dezenas['data'])
        planilha.append([dezena, data])

        # (f'Dezenas: {dezenas['dezenasOrdemSorteio']}\nData sorteio: {dezenas['data']}\n')
        
        excel.save('dezenas do sorteio.xlsx')
        print('arquivo preenchido com sucesso!')
        
else:
    print('houve um erro:', response.status_code)