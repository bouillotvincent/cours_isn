from tkinter import *
bool = True

def change():
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
    if(not test): tex1.configure(text = "This is getting really messy now.")

fen = Tk()

fen.title('Battle of the clicks')

tex1 = Label(fen, text = 'Welcome to Battle of the Clicks.')
tex2 = Label(fen, text = 'Dessin.')

tex1.grid(row = 0, column=0, columnspan=3, padx=20, pady=20)
tex2.grid(row = 1, column=0, rowspan=5, padx=20, pady=20)

ent1 = Entry(fen, textvariable = StringVar)
ent1.grid(row = 1, column=1, sticky = W)

but1 = Button(fen, text = 'Change', command = change)
but2 = Button(fen, text = 'Inutile', command = lambda x = 0 : do_something(bool, x) )
but3 = Button(fen, text = 'Quitter', command = fen.destroy)
but4 = Button(fen, text = 'Valider ', command = nom_joueur)

but1.grid(row = 2, column=1, columnspan=2)
but2.grid(row = 3, column=1, columnspan=2)
but3.grid(row = 4, column=2, sticky=E)
but4.grid(row = 4, column=1, sticky = W)

fen.mainloop()
