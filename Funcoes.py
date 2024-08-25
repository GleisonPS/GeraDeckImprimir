import os
from tkinter import filedialog
from tkinter import messagebox
import urllib.request as request
from docx import Document
from docx.shared import Inches,Mm


# Função que é chamada quando o botão de upload é clicado
def upload_file():
    # Abre uma caixa de diálogo para seleção de arquivo
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo",
        filetypes=[
            ("Arquivos YDK", "*.ydk"),
            ("Arquivos de Texto", "*.txt")
        ]
    )
    
    if file_path:  # Verifica se um arquivo foi selecionado
        #messagebox.showinfo("Arquivo Selecionado", f"O arquivo {file_path} foi selecionado!")
        Init_Baixar(file_path)
    else:
        messagebox.showwarning("Nenhum arquivo", "Nenhum arquivo foi selecionado.")


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

    

def Init_Baixar(Arquivo,nome="teste"):
    cards = []
    documento = Document()

    #Configurando as margens do documento como 0
    section = documento.sections[0]
    section.left_margin = Mm(0)
    section.right_margin = Mm(0)
    section.top_margin = Mm(0)
    section.bottom_margin = Mm(0)
    documento.element



    with open(Arquivo, "r") as arquivo:
        for linha in arquivo:
            if linha.strip() in ["#created by Toupeira","#main","#extra","!side"]:
                pass
            else:
                cards.append(linha.strip())

    for codeC in cards:
        baixar(codeC)
        try:
            Add_img(documento,codeC)
        except:
            pass

    directory = "deckPronto"
    if not os.path.exists(directory):
        os.makedirs(directory)


    documento.save(f"deckPronto/{nome}.docx")
    messagebox.showinfo("Arquivo Criado", f"O arquivo foi Criado!")


def Add_img(documento,codeCard):
    caminho = f"Cards/{codeCard}.jpg"
    
    # Converte as dimensões de mm para polegadas
    largura_polegadas = 57 / 25.4
    altura_polegadas = 89 / 25.4

    # Insere a imagem com tamanho específico (largura e altura em polegadas)
    documento.add_picture(caminho, width=Inches(largura_polegadas), height=Inches(altura_polegadas))
