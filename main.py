import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from Baixar_cards import Init_Baixar

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

# Configuração da janela principal
root = tk.Tk()
root.title("Uploader de Arquivos")
root.geometry("300x150")

# Rótulo de instrução
label = tk.Label(root, text="Clique no botão para fazer upload de um arquivo.")
label.pack(pady=20)

# Botão para abrir o diálogo de upload de arquivo
upload_button = tk.Button(root, text="Upload de Arquivo", command=upload_file)
upload_button.pack(pady=10)

# Inicia o loop principal da interface
root.mainloop()
