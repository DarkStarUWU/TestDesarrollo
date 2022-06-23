
from sqlite3 import Row
from tkinter import Entry, Frame, Tk, Canvas, Frame, Label, OptionMenu, StringVar, Button, filedialog
import psycopg2


 
class Ventana():
    
    def __init__(self, windows):

        ArrayComercial = ['Vanesa Castaño', 'Jorge Calvo', 'Aniket Kanurkar', 'Gengis Rovi']
        ArrayAsistentes = ['Jessica Prato', 'Juan Perez']

        self.wind = windows
        self.wind.title('Products application')
        self.canvas  = Canvas(self.wind, height=5000, width=5000)
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
        
        self.label = Label(self.frame, text="Asistente")
        self.label.place(x=0, y=310)
        
        self.label = Label(self.frame, text="comprobante de pago")
        self.label.place(x=0, y=380)
        
        self.label = Label(self.frame, text="comprobante de proveedor")
        self.label.place(x=0, y=450)
        
        #Entry
        self.entry_NumeroPresu  = Entry(self.frame)
        self.entry_NumeroPresu.place(x=200, y=30)

        self.entry_Cliente  = Entry(self.frame)
        self.entry_Cliente.place(x=200, y=100)

        self.entryFecha = Entry(self.frame)
        self.entryFecha.place(x=200,y=170)
        self.entryFecha.bind("<Key>", self.FechaEscriba)
        self.entryFecha.bind("<BackSpace>", lambda :self.entryFecha(self.root.END))
        
        self.var1 = StringVar(self.frame)
        self.opcion1 = OptionMenu(self.frame, self.var1, *ArrayComercial, command=self.getOpcion1)
        self.opcion1.config(width=20)
        self.opcion1.place(x=200, y=240)
        
        
        self.var2 = StringVar(self.frame)
        self.opcion2 = OptionMenu(self.frame, self.var2, *ArrayAsistentes, command=self.getOpcion2)
        self.opcion2.config(width=20)
        self.opcion2.place(x=200, y=310)
        
        
        self.botton_ComproPago = Button(self.frame, text="Adjuntar", command=self.AbrirArchivo)
        self.botton_ComproPago.place(x=200, y=380)

        self.botton_ComproProove = Button(self.frame, text="Adjuntar", command=self.AbrirArchivo)
        self.botton_ComproProove.place(x=200, y=450)
        
        self.botton_Guardar = Button(self.frame, text="Guardar", command=lambda:self.GuardarFormulario(
            self.entry_NumeroPresu.get(),
            self.entry_Cliente.get(),
            self.entryFecha.get(),
            self.opcion1,
            self.opcion2,
            self.botton_ComproPago.cget('command'),
            self.botton_ComproProove.cget('command')
            
            ))
        self.botton_Guardar.place(x=200, y=700)
        
    def FechaEscriba(self, event):
        if event.char.isdigit():
            texto = self.entryFecha.get()
            letras = 0
            for i in texto:
                letras += 1
            
            if letras == 2:
                self.entryFecha.insert(2, "/")
            elif letras == 5:
                self.entryFecha.insert(5, "/")
            
            if letras == 10:
                self.entryFecha.insert(10, " ")
            elif letras == 13:
                self.entryFecha.insert(13, ":")
            elif letras == 16:
                self.entryFecha.insert(16, ":")
            if letras == 19 :
                return "break"
        else:
            return "break"
        
    def AbrirArchivo(self):
        archivo = filedialog.askopenfilename(title="abrir", initialdir="C:/", filetypes=[["Archivos de Imagen", "*.jpg"]])
        print(archivo)
        
    def GuardarFormulario(self, Numero_Pres, Cliente, Fecha_Soli, Comercial, Asistente, Compro_Pago, Compro_Proveedor):
        conn = psycopg2.connect(dbname="postgres",
                         user="postgres", 
                         password="SuPer4536", 
                         host="localhost"
                         )
        cursor = conn.cursor()
        query =  "INSERT INTO Formulario(NumeroPresu,Cliente,Fecha_Solic,Comercial,Asistente,Compro_Pago,Compro_Proove) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        info =  Numero_Pres,Cliente,Fecha_Soli,Comercial,Asistente,Compro_Pago,Compro_Proveedor
        cursor.execute(query, info)
        print("save")
        conn.commit()
        conn.close()
        
    def getOpcion1(self):
        global getOpcion1
        getOpcion1 = self.var1
        
    def getOpcion2(self):
        global getOpcion2
        getOpcion2 = self.var2
        

    
def main():
    windows = Tk()
    application = Ventana(windows)
    windows.mainloop()     
      

if __name__ == '__main__':
   main()
   