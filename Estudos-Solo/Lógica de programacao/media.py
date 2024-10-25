nota1 = int(input('Digite a primeira nota:'))
nota2 = int(input('Digite a segunda nota:'))
nota3 = int(input('Digite a terceira nota:'))

def media_numeros():
    media = (nota1 + nota2 + nota3)/3
    
    return media

print(f'A media é {media_numeros()}')