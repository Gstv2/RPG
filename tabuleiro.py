from abc import ABC, abstractmethod

class Tabuleiro(ABC):

  @abstractmethod
  def lancarDados(self):
    pass

  def printTab(self):
      for i in range(0,self.dimensao[0]):
        for j in range(0,self.dimensao[1]):
          print(self.tabuleiro[i][j], end=" ")
        print("")