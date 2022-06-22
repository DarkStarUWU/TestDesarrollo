from tkinter import Tk
import tkinter as tk

ventana = Tk()

entryFecha = tk.Entry(ventana)
entryFecha.place(x=30,y=30)

def cuandoEscriba(event):
    if event.char.isdigit():
        texto = entryFecha.get()
        letras = 0
        for i in texto:
            letras +=1

        if letras == 2:
            entryFecha.insert(2,"/")
        elif letras == 5:
            entryFecha.insert(5,"/")
    else:
        return "break"

entryFecha.bind("<Key>", cuandoEscriba)
entryFecha.bind("<BackSpace>", lambda _:entryFecha.delete(tk.END))

ventana.mainloop()