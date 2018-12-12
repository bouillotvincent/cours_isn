# Le but de cette application est de voir comment « lier » les mouvements
# de la souris au Canvas afin de récupérer les coordonnées de la souris et
# de les afficher à chaque mouvement (en temps réel) dans la zone de texte.


##----- Importation des Modules -----##
from tkinter import *

##----- Définition des Fonctions -----##
def afficher(event):
    """ Entrées : Un événement de la souris
        Sortie : Affiche en temps réel les coordonnées de la souris dans la zone de texte"""
    abscisse = event.x
    ordonnee = event.y
    print(abscisse,ordonnee)

##----- Création de la fenêtre -----##
fen = Tk()
fen.title('Mouvements de la souris')

##----- Création des boutons -----##
bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row=2, column=1, padx=3, pady=3, sticky=S+W+E)

##---- Création des zones de texte -----##
message = Label(fen, text='Ici du texte.')
message.grid(row=0, column=0, columnspan=2, padx=3, pady=3)

##----- Création du canevas -----##
dessin=Canvas(fen, bg="cyan", width=251, height=251)
dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)

##----- Programme principal -----##


fen.mainloop()                     # Boucle d'attente des événements
