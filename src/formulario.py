from cProfile import label
from cgitb import text
from lib2to3.pgen2.token import OP
from re import X
from sqlite3 import Row
from tkinter import Entry, Frame, Tk, Canvas, Frame, Label, OptionMenu, StringVar
from turtle import left
import psycopg2




root = Tk()
root.title('Python & PostgreSQL')

ArrayComercial = ['Vanesa Castaño', 'Jorge Calvo', 'Aniket Kanurkar', 'Gengis Rovi']

#Funciones
def FechaEscriba(event):
    if event.char.isdigit():
        texto = entryFecha.get()
        letras = 0
        for i in texto:
            letras += 1
        
        if letras == 2:
            entryFecha.insert(2, "/")
        elif letras == 5:
            entryFecha.insert(5, "/")
        
        if letras == 10:
            entryFecha.insert(10, " ")
        elif letras == 13:
            entryFecha.insert(13, ":")
        elif letras == 16:
            entryFecha.insert(16, ":")
        if letras == 19 :
             return "break"
    else:
        return "break"
            

canvas  = Canvas(root, height=1000, width=1000)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

#Labels para informacion
label = Label(frame, text='Numero De Presupuesto')
label.place(x=0, y=30)


label = Label(frame, text='Cliente')
label.place(x=0, y=100)

label = Label(frame, text='Fecha de solicitud')
label.place(x=0, y=170)

label = Label(frame, text='Comercial')
label.place(x=0, y=240)


#Entry
entry_NumeroPresu  = Entry(frame)
entry_NumeroPresu.place(x=200, y=30)

entry_Cliente  = Entry(frame)
entry_Cliente.place(x=200, y=100)

entryFecha = Entry(frame)
entryFecha.place(x=200,y=170)

var = StringVar(frame)
opcion = OptionMenu(frame, var, *ArrayComercial)
opcion.config(width=20)
opcion.pack(side='bottom', padx= 200, pady=240,  ipadx = 100, ipady=10)
entry_Comercial  = Entry(frame)



entry_NumeroPresu  = Entry(frame)
entryFecha.bind("<Key>", FechaEscriba)
entryFecha.bind("<BackSpace>", lambda :entryFecha(root.END))



root.mainloop()
