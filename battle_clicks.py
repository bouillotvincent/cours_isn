from tkinter import *
from random import *
# variable globale
bool = True
compteur = 0
rad_ini = 20
r = rad_ini
color = ['black', 'red', 'yellow', 'blue', 'green', 'magenta', 'cyan']
color_in_use = 'black'
w = 250
h = 250
win = False
X = -10000
Y = -10000

# Fonction changement de couleur quand on clique sur espace.
def change(event):
    global color, color_in_use
    color_in_use = choice(color)
    print(color_in_use)

# Fonction affichant le nombre de clics réussi et appelant la fonction de test du cli.
def compte(event):
    global compteur
    """ Entrées : Fonction comptant le nombre de clics de bouton - pas d'entrée
		Sorties : Affiche le nombre de clics total dans la zone de texte 2."""
    do_something(bool,0)
    test_in(event.x,event.y)

# Fonction appelant le viseur et lançant une boucle infinie.
def viseur(event):
    global compteur, X2, Y2
    X2 = event.x
    Y2 = event.y
    create_viseur()

# Fonction créant le viseur à une coordonnée donnée.
def create_viseur():
    global X2, Y2
    for i in can.find_withtag("viseur"):
        can.delete(i)
    can.create_line(X2+13, Y2, X2-13, Y2, width=2, fill="red", tag="viseur")
    can.create_line(X2,Y2-13, X2, Y2+13, width=2, fill="red", tag="viseur")
    can.create_oval(X2-10, Y2-10, X2+10+1, Y2+10+1, width=2, outline="red", tag="viseur")
    can.after(200,create_viseur) # permet d'assurer un suivi du viseur et son effacement

# Fonction initiant toutes les variables relatives à un nouveau cercle.
def start():
    global rad_ini, win, r
    win = False
    r = rad_ini
    x = randrange(0,w)
    y = randrange(0,h)
    draw_cercle(x, y, r)


# Fonction testant si le clic est à l'intérieur du cercle.
def test_in(x, y):
    global X, Y, r, win, compteur # r est une variable globale
    if (x-X)**2+(y-Y)**2<=r**2:
        compteur += 1
        win = True


# Fonction dessinant un cercle de taille donnée.
def draw_cercle(x, y, r = rad_ini):
    global color, cer, X, Y
    X = x
    Y = y
    cer = can.create_oval(x-r, y-r, x+r+1, y+r+1, width=2, outline = color_in_use)
    minimise()

# Fonction faisant diminuer la taille du cercle.
def minimise():
    global cer, X, Y, r, rad_ini, win
    r = r / 1.2
    if(r < 1):  # Condition 1 : le joueur n'a pas été assez rapide et a manqué le cercle
        r = rad_ini
        can.delete(cer)
        start()
        return
    if(win):    # Condition 2 : le joueur a touché le cercle
        r = rad_ini
        start()
        return
    can.delete(cer)  # Pas de condition : le cercle continue de diminuer de tailler
    cer = can.create_oval(X-r, Y-r, X+r+1, Y+r+1, width=2, outline = color_in_use, fill='black')
    fen.after(300, minimise)


# Fonctions restantes de GUI_03.PY
def swap():
    global bool
    if bool:
        but2.configure(text='Utile')
    else:
        but2.configure(text='Inutile')
    bool = not bool

def nom_joueur():
    nom = ent1.get()
    tex1.configure(text="Welcome " + nom + " to Battle of the Clicks.")

def do_something(test, a):
    if(not test): tex1.configure(text = "{} cibles ont été touchées.".format(compteur))


# Partie graphique

fen = Tk()

fen.title('Battle of the clicks')

tex1 = Label(fen, text = 'Welcome to Battle of the Clicks.')
tex1.grid(row = 0, column=0, columnspan=3, padx=20, pady=20)

ent1 = Entry(fen, textvariable = StringVar())
ent1.grid(row = 1, column=1, sticky = W)

but0 = Button(fen, text = 'Start', command = start)
but1 = Button(fen, text = 'Change', command = swap)
but2 = Button(fen, text = 'Inutile', command = lambda x = 0 : do_something(bool, x) )
but3 = Button(fen, text = 'Quitter', command = fen.destroy)
but4 = Button(fen, text = 'Valider ', command = nom_joueur)

but0.grid(row = 1, column=2)
but1.grid(row = 2, column=1, columnspan=2)
but2.grid(row = 3, column=1, columnspan=2)
but3.grid(row = 4, column=2, sticky=E)
but4.grid(row = 4, column=1, sticky = W)

can = Canvas(fen, width = w, height=h, bg='#e9f7e1')
im = PhotoImage(file ='warclicks.gif', master=fen)
im = im.subsample(2)
can.create_image(w/2, h/2, image=im )
can.grid(row = 1, column=0, rowspan=5, padx=20, pady=20)

can.bind('<Button-1>', compte)
can.bind('<Motion>', viseur)
fen.bind('<space>', change)

fen.mainloop()
