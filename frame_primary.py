from tkinter import *
from tabuleiromedieval1 import TabuleiroMedieval

class Aplication:
  def __init__(self,master = None):

    
    def jogo():
      root = Tk()
      TabuleiroMedieval(1,6,8,8,root)
      root.mainloop()
      
  
    self.conteiner3 = Frame(master)
    self.conteiner3.place(relx = 0.5, rely = 0.5, anchor = 'center')
    self.play = Button(self.conteiner3,text = 'NEW GAME',command = jogo)
    self.play['width'] = 10
    self.play.pack(side = BOTTOM)

   

      
    
    