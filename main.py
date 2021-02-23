import tkinter as tk
import dibujo
from pitagoras.teorema import *
from pitagoras.teorema import _Cateto_opuesto, _Cateto_Adyacente, _Hipotenusa


class Calculadora(tk.Frame):
    def __init__(self, __padre__, *pargs):
        super(Calculadora,self).__init__(__padre__, *pargs)
        self._A_ = tk.IntVar()
        self._B_ = tk.IntVar()
        self._H_ = tk.IntVar()

    def __main__(self):
        label_text = tk.Label(self, text="Hola")
        label_text.pack()

        buton_cateto_opuesto = tk.Button(self, text="cateto_opuesto",
                                  command = lambda : _Cateto_opuesto(self, 6,2))
        buton_cateto_opuesto.pack()

        buton_cateto_adyacente = tk.Button(self, text="cateto_adyacente",
                                  command = lambda : _Cateto_Adyacente(self, 6,2))
        buton_cateto_adyacente.pack()

        buton_hipotenusa = tk.Button(self, text="hipotenusa",
                                  command = lambda : _Hipotenusa(self,5,6))
        buton_hipotenusa.pack()

        buton_dibujar = tk.Button(self, text="Dibujar",
                                  command = lambda : dibujo.Dibujar(80,120,60))
        buton_dibujar.pack()




if __name__ ==  "__main__":
    screen = tk.Tk()
    screen.geometry("300x300")
    screen.title("Pitagoras por Mike")

    objeto = Calculadora(screen)
    objeto.pack()
    objeto.__main__()
    screen.mainloop()
