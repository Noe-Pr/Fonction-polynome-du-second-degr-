from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
import webbrowser

# Création et personalisation de la fenêtre
fenetre = Tk()
fenetre.title("Polynome du second degré") 
fenetre.geometry("330x220")
fenetre.resizable(width=False, height=False)
fenetre.config(background="#1E1E70")
fenetre.iconbitmap("C:\\Users\\noepr\\Pictures\\NSI\\gh.ico")

# Le titre
titre = Label(fenetre, text="Entrez la fonction :",font=("Courrier", 19), bg="#1E1E70", fg="white")
titre.place(x=57,y=30)


def caracteres_valides(input_str):
    # Vérifie si l'entrée est un nombre valide, autorise les nombres négatifs et décimaux
    if input_str == "-":
        return True
    try:
        float(input_str.replace(",", "."))
        return True
    except ValueError:
        return False

# Les entrees de l'utilisateur
entree_a = Entry(fenetre, font=("Courrier", 15), bg ='white', fg='black', width=3)
entree_a.config(validate="key")
entree_a.place(x=68,y=80)
entree_a.config(validatecommand=(entree_a.register(caracteres_valides), '%P'))


entree_b = Entry(fenetre, font=("Courrier", 15), bg ='white', fg='black', width=3)
entree_b.config(validate="key")
entree_b.place(x=145,y=80)
entree_b.config(validatecommand=(entree_b.register(caracteres_valides), '%P'))

entree_c = Entry(fenetre, font=("Courrier", 15), bg ='white', fg='black', width=3)
entree_c.config(validate="key")
entree_c.place(x=223,y=80)
entree_c.config(validatecommand=(entree_c.register(caracteres_valides), '%P'))

a = entree_a.get()
b = entree_b.get()
c = entree_c.get()

def résolution_eq():
    a = float(entree_a.get().strip())
    b = float(entree_b.get().strip())
    c = float(entree_c.get().strip())
    delta = round(b**2-4*a*c)
    
    # Création d'une nouvelle fenêtre
    fenetre.geometry("700x400")
    fenetre.resizable(width=True, height=True)
    titre.destroy()
    entree_a.destroy()
    entree_b.destroy()
    entree_c.destroy()
    fonction0.destroy()
    fonction0_1.destroy()
    Bouton_résolution.destroy()
    frame1 = Frame(fenetre, bg="#1E1E70")
    
    x0 = None
    x1 = None
    x2 = None
    
    if delta < 0 :
        solution = Label(frame1, text=f"Δ = {delta} donc l'équation {a}x²+{b}x+{c} = 0",font=("Courrier", 19), bg="#1E1E70", fg="white")
        solution.pack()
        solution1 = Label(frame1, text="ne possède pas de solution",font=("Courrier", 19), bg="#1E1E70", fg="white")
        solution1.pack()
        
    elif delta == 0 :
        x0 = round((-b)/2*a,2)
        solution2 = Label(frame1, text=f"Δ = 0 donc l'équation {a}x²+{b}x+{c} = 0 possède",font=("Courrier", 19), bg="#1E1E70", fg="white")
        solution2.pack()
        solution3 = Label(frame1, text=f" une solution : x0 = {x0}",font=("Courrier", 19), bg="#1E1E70", fg="white")
        solution3.pack()
        
    elif delta > 0 :
        x1 = round(((-b)-sqrt(delta))/(2*a),2)
        x2 = round(((-b)+sqrt(delta))/(2*a),2)
        solution4 = Label(frame1, text=f"Δ = {delta} donc l'équation {a}x²+{b}x+{c} = 0 possède",font=("Courrier", 19), bg="#1E1E70", fg="white")
        solution4.pack()
        solution5 = Label(frame1, text=f"deux solutions distinctes : x1 = {x1}, et x2 = {x2}",font=("Courrier", 19), bg="#1E1E70", fg="white")
        solution5.pack()
    
    # Afficher la courbe
    def courbe():
        def f(x):
            return a*x**2+b*x+c
        
        x = np.linspace(-100, 100, 1000)
        y = f(x)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.axhline(0, color='black', lw=1)
        ax.axvline(0, color='black', lw=1)
        ax.set_title(f"Courbe représentative de la fonction {a}x²+{b}x+{c}")
        
        # Afficher les points des racines sur la courbe
        if x1 is not None:
            if x1.imag == 0:
                ax.plot(x1, 0, marker='x', color='r', markersize=12)
                
        if x2 is not None:
            if x2.imag == 0:
                ax.plot(x2, 0, marker='x', color='r', markersize=12)
                
        if x0 is not None:
            if x0.imag == 0:
                ax.plot(x0, 0, marker='x', color='r', markersize=12)
        
        ax.grid(True)
        plt.show()
        
    def bouton_entree1(event):
        courbe()
    
    # Création du bouton de la courbe
    Bouton_courbe = Button(frame1, text = "Courbe représentative",font=("Courrier", 16), fg="#1E1E70", command=courbe)
    Bouton_courbe.pack(pady=45)
    
    # Touche entrée = bouton 
    fenetre.bind('<Return>', bouton_entree1)
    
    frame1.pack(expand=YES)

# Le texte de la fonction
fonction0 = Label(fenetre, text="x²+",font=("Courrier", 19), bg="#1E1E70", fg="white")
fonction0.place(x=105,y=74)
fonction0_1 = Label(fenetre, text="x+",font=("Courrier", 19), bg="#1E1E70", fg="white")
fonction0_1.place(x=186,y=74)

def bouton_entree(event):
    résolution_eq()

# Création du bouton résolution 
Bouton_résolution = Button(fenetre, text = "Résolution de l'équation",font=("Courrier", 16), fg="#1E1E70", command=résolution_eq)
Bouton_résolution.place(x=45,y=135)

#Touche entrée = bouton 
fenetre.bind('<Return>', bouton_entree)

mon_menu = Menu(fenetre)

def aideTkinter():
    webbrowser.open_new("https://waytolearnx.com/2020/06/tutoriels-python.html")

# Création des sous-onglets aide
aide = Menu(mon_menu, tearoff=0)
aide.add_command(label='Aide Tkinter', command=aideTkinter)

# Création d'une barre de menu
mon_menu.add_cascade(label="Aide", menu=aide)

fenetre.config(menu=mon_menu)

# Affichage de la page
fenetre.mainloop()