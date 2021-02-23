from math import sqrt
import tkinter as tk
"""
h = math.sqrt( a**2 + b**2)
a = math.sqrt( h**2 - b**2)
b = math.sqrt( h**2 - a**2)
"""

def _Hipotenusa(self, a, b):
    h = a**2 + b**2
    hipotenusa = sqrt(h)
    label_hipotenusa = tk.Label(self, text=int(hipotenusa))
    label_hipotenusa.pack()

def _Cateto_opuesto(self, h, b):
    co = h**2 - b**2
    cateto_opuesto = sqrt(co)
    label_opuesto = tk.Label(self, text=int(cateto_opuesto))
    label_opuesto.pack()

def _Cateto_Adyacente(self, h, a):
    ca = h**2 - a**2
    cateto_adyacente = sqrt(ca)
    label_adyacente = tk.Label(self, text=int(cateto_adyacente))
    label_adyacente.pack()
