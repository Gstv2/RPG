from tabuleiromedieval1 import TabuleiroMedieval
from frame_primary import Aplication
from personagem import Personagem
from tabuleiro import Tabuleiro
from cavaleiro import Cavaleiro
from anao import Anao
from mago import Mago
from tkinter import *



root = Tk()
root.title("Menu")
root.geometry("775x600") 

bg = PhotoImage(file = "tela_de_inicio.png")
canvas1 = Canvas(root, width = 100, height = 100)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")
canvas1.create_text( 217, 98, text = "", font = 'Arial, 35', fill = 'silver')
canvas1.pack(fill = "both", expand = True)

sair = Button(root,text = 'EXIT',command = root.destroy)
sair.place(relx = 0.5, rely = 0.55, anchor = 'center')
sair['width'] = 10


Aplication(root)

root.mainloop()


