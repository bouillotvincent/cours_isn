# encode utf8
##-----Importation des Modules-----##
from tkinter import *
from random import *
compteur = 0

##-----Définition des Fonctions-----##
def lancer():
    """ Entrées : Fonction déclenchée par le bouton - pas d'entrée
		Sorties : Simule le lancer d'un dé à 6 faces et affiche le résultat obtenu dans la zone de texte 1."""
    resultat = 0 # ligne à effacer une fois votre fonction completée


def compte():
    global compteur
    """ Entrées : Fonction comptant le nombre de clics de bouton - pas d'entrée
		Sorties : Affiche le nombre de clics total dans la zone de texte 2."""
    resultat = 0 # ligne à effacer une fois votre fonction completée

##-----Création de la fenêtre-----##
fen = Tk()
fen.title('Lancer un dé')

##-----Création des boutons-----##
bouton_lancer = Button(fen, text='Lancer')
bouton_lancer.grid(row = 1, column = 0, padx=5, pady=3)

bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row = 1, column = 1, padx = 5, pady = 3)

##-----Création des zones de texte-----##
texte_affiche1 = Label(fen, text='')
texte_affiche1.grid(row = 0, column = 0)

texte_affiche2 = Label(fen, text='')
texte_affiche2.grid(row = 0, column = 1)
##-----Programme principal-----##
fen.mainloop()                          # Boucle d'attente des événements
