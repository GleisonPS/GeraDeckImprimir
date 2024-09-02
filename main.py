from tkinter import *
import Funcoes
from Funcoes import Init_Baixar
class PlaceholderEntry(Entry):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)
        self._set_placeholder()

    def _set_placeholder(self):
        self.insert(0, self.placeholder)
        self.config(fg='grey', font=('Arial', 15))

    def _on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, END)
            self.config(fg='black', font=('Arial', 15))

    def _on_focus_out(self, event):
        if self.get() == '':
            self._set_placeholder()

# Configuração da janela principal
root = Tk()
root.title("Uploader de Arquivos")
root.geometry("450x250")

choose_file = Button(root, command=Funcoes.upload_file)
choose_file.place(relx=0.1, rely=0.1, relheight=0.15, relwidth=0.1)

choose_file_path = PlaceholderEntry(root, placeholder='Informe o arquivo...')
choose_file_path.place(relx=0.23, rely=0.1, relheight=0.15, relwidth=0.7)

nome_arquivo = PlaceholderEntry(root, placeholder='Digite o nome do arquivo...')
nome_arquivo.place(relx=0.23, rely=0.35, relheight=0.15, relwidth=0.7)

botao_criar = Button(root, text='Criar', font=('Arial', 15, 'bold'), command=lambda: criar_arquivo(choose_file, nome_arquivo))
botao_criar.place(relx=0.35, rely=0.7, relheight=0.2, relwidth=0.3)


root.mainloop()
