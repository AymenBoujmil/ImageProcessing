
import tkinter as tk
from tkinter import ttk
# from PIL import Image, ImageTk
# from pandas import DataFrame
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import *
from tkinter import *

# image = readPGM("./assets/portraitWritten.pgm")


def alert():
    showinfo("alerte", "Bravo!")
fenetre = Tk()
menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Ouvrir", command=alert)
menu1.add_command(label="Enregistrer", command=alert)
menu1.add_separator()
menu1.add_command(label="Sortir", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Egalisation", command=alert)
menu2.add_command(label="Transformation lineaire", command=alert)
menu2.add_command(label="Transformation lineaire avec saturation", command=alert)
menu2.add_command(label="Dilatation des zones claires", command=alert)
menu2.add_command(label="Dilatation des zones sombres", command=alert)
menu2.add_command(label="Dilatation des zones milieux", command=alert)
menu2.add_command(label="Inversion de l'image", command=alert)
menubar.add_cascade(label="Contrast", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Ajouter bruit", command=alert)
menu3.add_command(label="filtre moyen", command=alert)
menu3.add_command(label="filtre guassian", command=alert)
menu3.add_command(label="filtre median", command=alert)
menu3.add_command(label="filtre passe haut", command=alert)
menubar.add_cascade(label="filtres", menu=menu3)

fenetre.config(menu=menubar)




fenetre.mainloop()