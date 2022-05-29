
import tkinter as tk
from tkinter import ttk
# from PIL import Image, ImageTk
# from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import *
from tkinter import *
from IO import *
from Utils import *
from filtres import *
from Utils import *
from contrast import *
(imageMatrix, ndG, nbLines, nbCols) = readImage("./assets/mona.pgm")

moy = moyenne(imageMatrix, ndG, nbLines, nbCols)
ecartType = ecartType(imageMatrix, ndG, nbLines, nbCols)

def updateImage(newimage):
    global imageMatrix
    global moy
    global ecartType
    imageMatrix = newimage
    im.set_data(imageMatrix)
    canvas.draw()
    hist = histogramme(imageMatrix, ndG, nbLines, nbCols)
    ax1.clear()
    ax1.plot(hist)
    bar1.draw()

def reset():
    global imageMatrix
    (newImage, ndG, nbLines, nbCols) = readImage("./assets/mona.pgm")
    imageMatrix = newImage
    im.set_data(imageMatrix)
    canvas.draw()
    hist = histogramme(imageMatrix, ndG, nbLines, nbCols)
    ax1.clear()
    ax1.plot(hist)
    bar1.draw()



fenetre = Tk()
image = plt.figure(1,figsize=(5,4))
im = plt.imshow(imageMatrix, cmap="gray") # later use a.set_data(new_data)
ax = plt.gca()
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.close(1)
# a tk.DrawingArea

canvas = FigureCanvasTkAgg(image, master=fenetre)
canvas.draw()
canvas.get_tk_widget().grid(row=1, column=1,columnspan=3)
moyenneL = tk.Button(fenetre, text="Moyenne = " + str(round(moy, 2)), state=tk.DISABLED).grid(row=2, column=0,columnspan=3)
ecartTypeL = tk.Button(fenetre, text="Ecart Type = " + str(round(ecartType, 2)), state=tk.DISABLED).grid(row=2, column=2,columnspan=3)

hist = histogramme(imageMatrix, ndG, nbLines, nbCols)
histImage = plt.Figure(figsize=(4,2), dpi=100)
ax1 = histImage.add_subplot(111)

bar1 = FigureCanvasTkAgg(histImage, fenetre)
bar1.get_tk_widget().grid(row=3, column=1, columnspan=3)
ax1.plot(hist)

def alert():
    showinfo("alerte", "Bravo!")






menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Ouvrir", command=alert)
menu1.add_command(label="Enregistrer", command=alert)
menu1.add_command(label="reset", command=reset)
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
menu3.add_command(label="Ajouter bruit", command=lambda : updateImage(bruit(imageMatrix, ndG, nbLines, nbCols)))
menu3.add_command(label="filtre moyen", command=lambda: updateImage(filterApply(imageMatrix, ndG, nbLines, nbCols,9,"Moynenneur")))
menu3.add_command(label="filtre guassian", command=lambda : updateImage( filterApply(imageMatrix, ndG, nbLines, nbCols,9,"Gaussian", sigma = 2)))
menu3.add_command(label="filtre median", command=lambda : updateImage(filterMedian(imageMatrix, ndG, nbLines, nbCols,3)))
menu3.add_command(label="filtre passe haut", command=lambda : updateImage(filterApply(imageMatrix, ndG, nbLines, nbCols,3,'passeHaut',number = 1)))
menubar.add_cascade(label="filtres", menu=menu3)

fenetre.config(menu=menubar)




fenetre.mainloop()