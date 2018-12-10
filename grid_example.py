from tkinter import *

fen = Tk()

fen.title('Vive Windows 98')

tex1 = Label(fen, text = 'Hello, beautiful world! Tkinter looks so promising.')
tex1.grid(row = 0, column=0, columnspan=2, padx = 20, pady = 20)

but1 = Button(fen, text = 'Ne sers à rien')
but2 = Button(fen, text = 'Quitter', command = fen.destroy)

but1.grid(row = 1, column=0, padx = 10, pady = 10, sticky=E)
but2.grid(row = 1, column=1, padx = 10, pady = 10, sticky=W)

fen.mainloop()
