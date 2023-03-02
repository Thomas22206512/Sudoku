import tkinter as tk

#----------------variable et constante----------------#

grid = [[j for j in range(1,10)] for i in range(9)]

region = [
    [None,None,None],
    [None,None,None],
    [None,None,None]
]

colonne = [None for j in range(9)]

ligne = [None for i in range(9)]

HEIGHT = 900
WIDTH = HEIGHT

# ---------------fonction d'affichage---------------#

def gui():
    '''cree un les lignes qui forme le grillage (grosse et fine ligne),
    affiche egalement les chiffres présente dans la liste grid, 
    change la couleur d'arrire plan selon l'état de la liste region, colonne et ligne
    et pour finir sur ligne la zone sélection par le joueur'''
    pass

#---------------construction de tkinter---------------#

root = tk.Tk()
root.title("Sudoku")
root.iconbitmap("pastime.ico")
root.resizable(False, False)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

root.mainloop()