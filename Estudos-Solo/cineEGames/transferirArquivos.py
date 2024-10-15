import os

lista_jogos_e_filmes = os.listdir('cineEGames')


for games in lista_jogos_e_filmes:
    
    if 'txt' in games:
        txt = games+'.txt'
        
        
        if "game" in txt:
            os.rename(f"cineEGames/{games}",f"cineEGames/jogos/{games}")
            print("caminho do jogo alterado com sucesso!")
       
        elif 'movie' in txt:
            os.rename(f"cineEGames/{games}",f"cineEGames/filmes/{games}")
            print("caminho do filme alterado com sucesso!")

        else:
            print("nada foi feito")

    else:
        print("essa pasta está vazia")