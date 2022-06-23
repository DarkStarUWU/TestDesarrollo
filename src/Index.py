from cProfile import label
from cgitb import text
from email.mime import application
from lib2to3.pgen2.token import OP
from re import X
from sqlite3 import Row
from tkinter import Entry, Frame, Tk, Canvas, Frame, Label, OptionMenu, StringVar
from turtle import left
import psycopg2

 
 
class Main():
    
    def __init__(self, windows):
        ArrayComercial = ['Vanesa Castaño', 'Jorge Calvo', 'Aniket Kanurkar', 'Gengis Rovi']
        self.wind = windows
        self.wind.title('Products application')
        self.canvas  = Canvas(self.wind, height=1000, width=1000)
        self.canvas.pack()

        self.frame = Frame()
        self.frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.label = Label(self.frame, text='Numero De Presupuesto')
        self.label.place(x=0, y=30)


        self.label = Label(self.frame, text='Cliente')
        self.label.place(x=0, y=100)

        self.label = Label(self.frame, text='Fecha de solicitud')
        self.label.place(x=0, y=170)

        self.label = Label(self.frame, text='Comercial')
        self.label.place(x=0, y=240)
        #Entry
        entry_NumeroPresu  = Entry(self.frame)
        entry_NumeroPresu.place(x=200, y=30)

        entry_Cliente  = Entry(self.frame)
        entry_Cliente.place(x=200, y=100)

        entryFecha = Entry(self.frame)
        entryFecha.place(x=200,y=170)

        var = StringVar(self.frame)
        opcion = OptionMenu(self.frame, var, *ArrayComercial)
        opcion.config(width=20)
        opcion.pack(side='bottom', padx= 200, pady=240,  ipadx = 100, ipady=10)
        entry_Comercial  = Entry(frame)



        entry_NumeroPresu  = Entry(frame)
        entryFecha.bind("<Key>", FechaEscriba)
        entryFecha.bind("<BackSpace>", lambda :entryFecha(root.END))

if __name__ == '__main__':
    windows = Tk()
    application = Main(windows)
    windows.mainloop()