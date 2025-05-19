from tkinter import *


class App:
    def __init__(self, root):
      self.frame1 = Frame(root)
      self.frame1.pack()
      label(self.frame1,text="Converção de centimetro para Polegada",)
      font=("Verdana","14","bold"), height=3).pack()
      

    Label.(self.frame1,text="Centimetro(s):") pack(slide=LEFT)
    self.centimetro=Entry(self.frame1)
    self.centimetro=focus_force()
    self.centimetro=pack(side=LEFT)
    Button(self.frame1,text="Converter", command=self.converter)

    Label (self.fram1,teste="polegada(s):").pack(side=LEFT)

    self.centimetro.focus_force()
    self.centimetro.pack(side=LEFT)
