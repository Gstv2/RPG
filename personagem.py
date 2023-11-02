from tkinter import messagebox  
import random
import os

class Personagem:
  def __init__(self, nome):
    self.nome = nome
    self.forca = 0.0
    self.posicao = []

  def lutar(self, personagem,player):
    hpm = 10
    hpg = 10
    resposta = messagebox.askquestion("lutar","deseja Atacar {}".format(personagem))
    while hpm > 0 and hpg > 0:
        if resposta == 'yes':
            a = random.randint(1, 6)
            hpm = hpm - a
            if (hpm <= 0):
              os.system('clear')
              print('Você venceu !')
              exit()

            b = random.randint(1, 6)
            hpg = hpg - b  # novo valor do hp_coelho
            messagebox. showwarning ("registro" ,'seu ataque foi de {} pontos,\nele te acertou com {} pontos\n{} tem {}de vidas\n{} tem {}de vidas'.format( a, b,player,hpg,personagem,hpm))
          
            if (hpg <= 0):
              os.system('clear')
              print('voce foi derrotado!!')
              exit('fim de jogo')
        else:
          messagebox. showwarning ("registro" ,"Voce fugi, voce e uma vergonha!!")
          break
          
    
        resposta = messagebox.askquestion("lutar","deseja atacar {}".format(personagem))
    