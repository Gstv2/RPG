from personagem import Personagem
from tkinter import messagebox
from tabuleiro import Tabuleiro
from cavaleiro import Cavaleiro
# from replit import audio
from tkinter import *
from mago import Mago
from anao import Anao
import random
import os


class TabuleiroMedieval(Tabuleiro):
  def __init__(self, num_dados, top_dado, linhas, colunas, master = None):
    print(num_dados)
    self.numdados = num_dados
    self.topdado = top_dado
    self.dimensao = [linhas, colunas]
    self.tabuleiro = []
    self.jogador_vez = None
    self.res = []
    
    bgv = ['#09a164', "#096d64"]
    cor = 0
    for i in range(0, linhas):
      if (i%2 == 0):
        cor = 0
      else:
        cor = 1
      coluna = []
      conteiner = Frame(master)
      conteiner.pack(side = TOP)  
      for j in range(0, colunas):
        label = Label(conteiner, bg=bgv[cor])
        label["width"] = 8
        label["height"] = 4
        label.pack(side=LEFT)
        label["text"] = " "
        coluna.append(label)
        if cor == 0:
          cor = 1
        else:
          cor = 0
      self.tabuleiro.append(coluna)
          

    
    self.j1 = self.__aleatorizarPersonagem__()
    print(self.j1)
    self.j2 = self.__aleatorizarPersonagem__()
    print(self.j2)
    self.jogador_vez = self.j1

    self.item1 = self.__aleatorizarItens__()
    self.item2 = self.__aleatorizarItens__()
    self.item3 = self.__aleatorizarItens__()

    self.conteiner3 = Frame(master)
    self.conteiner3.pack(side = BOTTOM)
    self.botao_esquerda = Button(self.conteiner3,text = '<-')
    self.botao_esquerda['command'] = self.moveEsquerda
    self.botao_esquerda.pack(side = LEFT)
    
    self.botao_baixo = Button(self.conteiner3,text = '\/')
    self.botao_baixo['command'] = self.moveBaixo
    self.botao_baixo.pack(side = LEFT)
    
    self.botao_direita = Button(self.conteiner3,text = '->')
    self.botao_direita['command'] = self.moveDireita
    self.botao_direita.pack(side = LEFT)
    
    self.conteiner2 = Frame(master)
    self.conteiner2.pack(side = BOTTOM)
    self.botao_cima = Button(self.conteiner2,text = "/\ ")
    self.botao_cima['command'] = self.moveCima
    self.botao_cima.pack(side = LEFT)



    self.conteiner4 = Frame(master)
    self.conteiner4.place(relx = 0.0,rely = 1.0, anchor ='sw')
    self.Dados = Button(self.conteiner4,text = "DADOS")
    self.Dados['command'] = self.lancarDados
    self.Dados.pack(side = RIGHT)
    
  def lancarDados(self):
    self.soma = sum(self.res)
    if self.soma != 0:
      messagebox. showwarning("erro","Voce nao pode mas girar o dados")
    if self.soma == 0:
        for i in range(0, self.numdados):
          self.res.append(random.randint(1, self.topdado + 1))
          self.soma = sum(self.res)
          print(self.soma)
        return self.soma


  def __trocaPersonagem__(self):
    if self.jogador_vez == self.j1:
      self.jogador_vez = self.j2
    else:
      self.jogador_vez = self.j1

  

  def __PosicaoAleatoria__(self):
    max_linha = self.dimensao[0] - 1
    max_coluna = self.dimensao[1] - 1
    l = random.randint(0, max_linha)
    c = random.randint(0, max_coluna)

    while self.tabuleiro[l][c]["text"] != ' ':
      l = random.randint(0, max_linha)
      c = random.randint(0, max_coluna)

    return [l, c]



  def __aleatorizarItens__(self):
    itens = random.randint(1,3)
    print(itens)
    pos = self.__PosicaoAleatoria__()
    if itens == 1:
      self.posEspada = []
      self.posEspada = pos
      self.forcaEsp = random.randint(0,4)
      self.emojiEsp = "T"
      self.tabuleiro[self.posEspada[0]][self.posEspada[1]]["text"] = self.emojiEsp
      
    elif itens == 2:
      self.posmagia = []
      self.posMagia = pos
      self.nome_magias = ['tornado','tempestade','bafo de gelo']
      self.forcaMag = random.randint(0,4)
      self.emojiMag = 'o'
      self.tabuleiro[self.posMagia[0]][self.posMagia[1]]["text"] = self.emojiMag
      
    else:
      self.posMachado = []
      self.posMachado = pos
      self.forcaAn = random.randint(0,4)
      self.emojiAn = 'P'
      self.tabuleiro[self.posMachado[0]][self.posMachado[1]]["text"] = self.emojiAn


    
  def __aleatorizarPersonagem__(self):
    personagem = random.randint(1,3)
    pos = self.__PosicaoAleatoria__()
    
    if personagem ==  1:
      Mão = random.randint(1,2)
      if Mão == 1:
        Mão = True
      else:
        Mão =  False
      self.cavaleiro = Cavaleiro("hellboy", Mão, "C")
      self.cavaleiro.posicao = pos
      self.tabuleiro[self.cavaleiro.posicao[0]][self.cavaleiro.posicao[1]]["text"] = self.cavaleiro.emoji
      return self.cavaleiro
      
    if personagem ==  2:
      self.patolino = Mago('patolino',"P")
      self.patolino.posicao = pos
      self.tabuleiro[self.patolino.posicao[0]][self.patolino.posicao[1]]["text"] = self.patolino.emoji
      return self.patolino
      
    else:
      self.nelsinho = Anao('nelsinho',"A")
      self.nelsinho.posicao = pos
      self.tabuleiro[self.nelsinho.posicao[0]][self.nelsinho.posicao[1]]["text"] = self.nelsinho.emoji
      return self.nelsinho


  
  def moveEsquerda(self):
      if self.soma == 0:      
        self.__trocaPersonagem__()
        messagebox. showwarning ("aviso","seus movimentos acabaram vez do outro jogador.\n{} jogue o dado".format(self.jogador_vez.nome))
        del self.res[0]
      else:
        if (self.__checagem__("E") == True):
            self.soma = self.soma -1
            jogador = self.jogador_vez
            jogador.posicao[1] = jogador.posicao[1] - 1
            self.tabuleiro[jogador.posicao[0]][jogador.posicao[1] + 1]["text"] = " "
            if self.tabuleiro[jogador.posicao[0]][jogador.posicao[1]]["text"] != ' ':
              self.__checarLutar__()
              self.__checarEquipar__()
            else:
              self.tabuleiro[jogador.posicao[0]][jogador.posicao[1]]["text"] = jogador.emoji

    
  def moveDireita(self):
      if self.soma == 0:
        self.__trocaPersonagem__()
        messagebox. showwarning ("aviso","seus movimentos acabaram vez do outro jogador.\n{} jogue o dado".format(self.jogador_vez.nome))
        del self.res[0]
      else:
        if (self.__checagem__("D") == True):
  
            self.soma = self.soma -1
            jogador = self.jogador_vez
            jogador.posicao[1] = jogador.posicao[1] + 1
            self.tabuleiro[jogador.posicao[0]][jogador.posicao[1] - 1]["text"] = " "
            if self.tabuleiro[jogador.posicao[0]][jogador.posicao[1]]["text"] != ' ':
              self.__checarEquipar__()
              self.__checarLutar__()
            else:
              self.tabuleiro[jogador.posicao[0]][jogador.posicao[1]]["text"] = jogador.emoji
      

    
  def moveCima(self):  
      if self.soma == 0:      
        self.__trocaPersonagem__()
        messagebox. showwarning ("aviso","seus movimentos acabaram vez do outro jogador.\n{} jogue o dado".format(self.jogador_vez.nome))
        del self.res[0]
      else:
        if (self.__checagem__("C") == True):
  
            self.soma = self.soma -1
            jogador = self.jogador_vez
            jogador.posicao[0] = jogador.posicao[0] - 1
            self.tabuleiro[jogador.posicao[0]+1][jogador.posicao[1]]["text"] = " "
            if self.tabuleiro[jogador.posicao[0]][jogador.posicao[1]]["text"] != ' ':
              self.__checarLutar__()
              self.__checarEquipar__()
            else:
              self.tabuleiro[jogador.posicao[0]][jogador.posicao[1]]["text"] = jogador.emoji


    
  def moveBaixo(self):
      if self.soma == 0:      
        self.__trocaPersonagem__()
        messagebox. showwarning ("aviso","seus movimentos acabaram vez do outro jogador.\n{} jogue o dado".format(self.jogador_vez.nome))
        del self.res[0]
      else:
        if (self.__checagem__("B") == True):
            self.soma = self.soma -1
            jogador = self.jogador_vez
            jogador.posicao[0] = jogador.posicao[0] + 1
            self.tabuleiro[jogador.posicao[0]-1][jogador.posicao[1]]["text"] = " "
            if self.tabuleiro[jogador.posicao[0]][jogador.posicao[1]]["text"] != ' ':
              self.__checarLutar__()
              self.__checarEquipar__()
            else:
              self.tabuleiro[jogador.posicao[0]][jogador.posicao[1]]["text"] = jogador.emoji
    

  
  def __checagem__(self, direcao):
      if direcao == "C":
          if self.jogador_vez.posicao[0] == 0:
              return False
          else:
              return True
      elif direcao == "B":
          if self.jogador_vez.posicao[0] == self.dimensao[0]-1:
              return False
          else:
              return True
      elif direcao == "E":
          if self.jogador_vez.posicao[1] == 0:
              return False
          else:
              return True
      elif direcao == "D":
          if self.jogador_vez.posicao[1] == self.dimensao[1]-1:
              return False
          else:
              return True
      else:
          return False


  
  def __checarLutar__(self):
    jogador = self.jogador_vez
    if self.tabuleiro[jogador.posicao[0]][jogador.posicao[1]]["text"] == "C":

      if jogador == self.j1:
        Personagem.lutar(self,self.j2.nome,self.j1.nome)
      else:
        Personagem.lutar(self,self.j1.nome,self.j2.nome)

    
    if self.tabuleiro[jogador.posicao[0]][jogador.posicao[1]]["text"] == "P":

      if jogador == self.j1:
        Personagem.lutar(self,self.j2.nome,self.j1.nome)
      else:
        Personagem.lutar(self,self.j1.nome,self.j2.nome)

    
    if self.tabuleiro[jogador.posicao[0]][jogador.posicao[1]]["text"] == "A":

      if jogador == self.j1:
        Personagem.lutar(self,self.j2.nome,self.j1.nome)
      else:
        Personagem.lutar(self,self.j1.nome,self.j2.nome)

  
  def __checarEquipar__(self):
    jogador = self.jogador_vez
    
    if jogador.nome == "hellboy":
      if self.tabuleiro[jogador.posicao[0]][jogador.posicao[1]]["text"] == "T":
        self.cavaleiro.equipar(self.cavaleiro.mao,self.forcaEsp)
        print('cavaleiro')
        self.cavaleiro.comoEstou()
        
    if jogador.nome == "nelsinho":
      if self.tabuleiro[jogador.posicao[0]][jogador.posicao[1]]["text"] == "P":
        self.nelsinho.equipar(self.forcaAn)
        print('nelsinho')
        self.nelsinho.comoEstou()
        
    if jogador.nome == "patolino":
      if self.tabuleiro[jogador.posicao[0]][jogador.posicao[1]]["text"] == "o":
        self.patolino.aprenderMagia(self.nome_magias[0],self.forcaMag)
        print('patolino')
        self.patolino.minhasMagias()
    
      