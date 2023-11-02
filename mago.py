from personagem import Personagem
from tkinter import messagebox

class Mago(Personagem):
  def __init__(self, nome, emoji):
    super().__init__(nome)
    self.magias = []
    self.emoji = "M"

  def aprenderMagia(self, nome, forca):
    if (nome in self.magias):
      print("Já aprendi essa magia")
      return False
    else:
      self.magias.append(nome)
      self.forca += forca
    return self.magias

    
  def minhasMagias(self):
    messagebox.showwarning('Mago','suas magias sao {}\nforca: {}'.format(self.magias,self.forca))

