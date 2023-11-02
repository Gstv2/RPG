from personagem import Personagem
from tkinter import messagebox

class Anao(Personagem):
  def __init__(self, nome, emoji):
    super().__init__(nome)
    self.machado = 0.0
    self.agilidade = 10
    self.emoji = "A"
    
    
  def equipar(self, forca):
    self.machado = forca
    self.agilidade = 10-self.machado
    self.forca = self.machado*self.agilidade/10

  def comoEstou(self):
    messagebox.showwarning("Anao",self.nome + '\nagilidade: {}\nForça total: '+ str(self.forca).format(self.agilidade))
    print(self.nome)
    print("agilidade: {}".format(self.agilidade))
    print("Força total: " + str(self.forca))

