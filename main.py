import tkinter as tk
import Funcoes
from Funcoes import Init_Baixar


# Configuração da janela principal
root = tk.Tk()
root.title("Uploader de Arquivos")
root.geometry("450x250")

# Rótulo de instrução
label = tk.Label(root, text="Clique no botão para fazer upload de um arquivo.")
label.pack(pady=20)

# Botão para abrir o upload do deck
upload_deck = tk.Button(root, text="Upload de Arquivo do deck", command=Funcoes.upload_file)
upload_deck.pack(pady=10)

#Botão de acessar o Historico
historico = tk.Button(root,text="Historico")


# Inicia o loop principal da interface
root.mainloop()
