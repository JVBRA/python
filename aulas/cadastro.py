#https://www.youtube.com/watch?v=TXlkiMIBlTM
import tkinter as tk
from tkinter import ttk
import datetime as dt

janela = tk.Tk()
#TITULA DA JANELA
janela.title('Ferramenta de cadastro de materiais') #TITULO DO APP

label_descrição = tk.Label(text="Descrição do material")# DESCRIÇÃO DE UMA LABEL
label_descrição.grid(row=1, column=0, padx=10, pady=10, sticky='nswe',columnspan=4)#(norte sul leste oeste)/#MATRIZ ONDE FICARA
entry_descrição = tk.Entry()
entry_descrição.grid(row=2, column=0, padx=10, pady=10, sticky='nswe',columnspan=4)#(norte sul leste oeste)/#MATRIZ ONDE FICARA

janela.mainloop()
