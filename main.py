from tkinter import *
from Funcoes import *



# Configuração da janela principal
root = Tk()
root.title("Uploader de Arquivos")
root.geometry("450x250")
imagem = PhotoImage(file='Imgs/pasta(3).png')
choose_file = Button(root, command=lambda: abrir_pasta(choose_file_path,nome_arquivo), image=imagem)
choose_file.place(relx=0.1, rely=0.1, relheight=0.15, relwidth=0.1)

choose_file_path = PlaceholderEntry(root, placeholder='Informe o arquivo...')
choose_file_path.place(relx=0.23, rely=0.1, relheight=0.15, relwidth=0.7)

nome_arquivo = PlaceholderEntry(root, placeholder='Digite o nome do arquivo...')
nome_arquivo.place(relx=0.23, rely=0.35, relheight=0.15, relwidth=0.7)

botao_criar = Button(root, text='Criar', font=('Arial', 15, 'bold'), command=lambda: criar_deck(choose_file_path,nome_arquivo)) #(choose_file, nome_arquivo))
botao_criar.place(relx=0.35, rely=0.7, relheight=0.2, relwidth=0.3)


root.mainloop()
