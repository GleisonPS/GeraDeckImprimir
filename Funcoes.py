import os
import urllib.request as request

def baixar(card):
    url = "https://images.ygoprodeck.com/images/cards/"
    pasta = "Cards"
    
    # Verifica se a pasta existe, caso contrário, cria
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    
    try:
        request.urlretrieve(f"{url}{card}.jpg", f"{pasta}/{card}.jpg")
    except Exception as ex:
        print(f"Erro ao baixar a imagem: {ex}")

    

def Init_Baixar(Arquivo):
    cards = []
    with open(Arquivo, "r") as arquivo:
        for linha in arquivo:
            if linha.strip() == "#main":
                pass
            else:
                cards.append(linha.strip())

    for codeC in cards:
        baixar(codeC)