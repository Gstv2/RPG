from personagem import Personagem
from tkinter import messagebox

class Cavaleiro(Personagem):
  def __init__(self, nome, destro,emoji):
    super().__init__(nome)
    self.mao_direita = 0
    self.mao_esquerda = 0
    self.destro = destro
    self.emoji = 'C'

  def equipar(self, mao, forca):
    if (mao == "E"):
      if not(self.destro): #True ou False
        forca = (1.5*forca)
      self.forca = self.forca - self.mao_esquerda
      self.mao_esquerda = forca
    else:
      if (self.destro):
        forca = (1.5*forca)
      self.forca = self.forca - self.mao_direita
      self.mao_direita = forca
      
    self.forca = self.forca + forca
    return forca

  def comoEstou(self):
    messagebox.showwarning("caveleiro",self.nome + "Mão Direita: " + str(self.mao_direita) + "Mão Esquerda: " + str(self.mao_esquerda) + "Força total: " + str(self.forca))
    print(self.nome)
    print("Mão Direita: " + str(self.mao_direita))
    print("Mão Esquerda: " + str(self.mao_esquerda))
    print("Força total: " + str(self.forca))