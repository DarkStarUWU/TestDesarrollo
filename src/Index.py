
#Importar Librerias
from tkinter import END, Entry, Frame, Tk, Canvas, Frame, Label, OptionMenu, StringVar, Button, filedialog, simpledialog
import psycopg2



 
class Ventana():


    def __init__(self, windows):
        #Declaracion de las tuplas
        ArrayComercial = ['Vanesa Castano', 'Jorge Calvo', 'Aniket Kanurkar', 'Gengis Rovi']
        ArrayAsistentes = ['Jessica Prato', 'Juan Perez']

        #Creacion de la ventana
        self.wind = windows
        self.wind.title('Products application')
        self.canvas  = Canvas(self.wind, height=5000, width=5000)
        self.canvas.pack()

        self.frame = Frame()
        self.frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        #Creacion de los cuadros de texto no editables
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
        
        #Creacion de textos Editablas
        self.entry_NumeroPresu  = Entry(self.frame)
        self.entry_NumeroPresu.place(x=200, y=30)

        self.entry_Cliente  = Entry(self.frame)
        self.entry_Cliente.place(x=200, y=100)

        self.entryFecha = Entry(self.frame)
        self.entryFecha.place(x=200,y=170)
        self.entryFecha.bind("<Key>", self.FechaEscriba)
        self.entryFecha.bind("<BackSpace>", lambda :self.entryFecha(self.root.END))
        
        #Creacion de los Menus Desplegables
        self.var1 = StringVar(self.frame)
        self.var1.set("Elegir Comercial")
        self.opcion1 = OptionMenu(self.frame, self.var1, *ArrayComercial)
        self.opcion1.config(width=20)
        self.opcion1.place(x=200, y=240)
        

        self.var2 = StringVar(self.frame)
        self.var2.set("Elegir Asisitente")
        self.opcion2 = OptionMenu(self.frame, self.var2, *ArrayAsistentes)
        self.opcion2.config(width=20)
        self.opcion2.place(x=200, y=310)
        
        #Creacion de los botones para capturar la imagen
        self.botton_ComproPago = Button(self.frame, text="Adjuntar", command=self.AbrirArchivo1)
        self.botton_ComproPago.place(x=200, y=380)

        self.botton_ComproProove = Button(self.frame, text="Adjuntar", command=self.AbrirArchivo2)
        self.botton_ComproProove.place(x=200, y=450)
        
        self.botton_Guardar = Button(self.frame, text="Guardar", command=lambda:self.GuardarFormulario())
        self.botton_Guardar.config(width=20, height=5)
        self.botton_Guardar.place(x=200, y=500)
    #Funcion Para formato de fecha
    def FechaEscriba(self, event):
        if event.char.isdigit():
            texto = self.entryFecha.get()
            letras = 0
            for i in texto:
                letras += 1
            
            if letras == 4:
                self.entryFecha.insert(4, "-")
            elif letras == 7:
                self.entryFecha.insert(7, "-")
            
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
    #Funciones Para Abrir la ventana de windows y adjuntar las imagenes
    def AbrirArchivo1(self):
        global p
        archivo = filedialog.askopenfilename(title="abrir", initialdir="C:/", filetypes=[["Archivos de Imagen", "*.jpg"]])
        with open(archivo, "rb") as omage:
            image = omage.read()
            p = bytearray(image)
        return p

    def AbrirArchivo2(self):
        global b
        archivo = filedialog.askopenfilename(title="abrir", initialdir="C:/", filetypes=[["Archivos de Imagen", "*.jpg"]])
        with open(archivo, "rb") as omage:
            image = omage.read()
            b = bytearray(image)
        return b
    

    #Guardar La informacion con la base de datos
    def GuardarFormulario(self,*args):
        
        try:
            conn = psycopg2.connect(dbname="postgres",
                            user="postgres", 
                            password="pass", 
                            host="localhost"
                            )
            print("Connection Successful!")
        except: 
            print("Unable to connect to database")
        try:
           
            cursor = conn.cursor()
            query =  "INSERT INTO Formulario(NumeroPresu,Cliente,Fecha_Solic,Comercial,Asistente,Compro_Pago, Compro_Proove) VALUES (%s,%s, %s,%s, %s,%s, %s)"
            info =   self.entry_NumeroPresu.get(),self.entry_Cliente.get(),self.entryFecha.get(), self.var1.get(), self.var2.get(), p, b
            cursor.execute(query, info)
            Dialog = simpledialog.Dialog(self.frame, text="Guardado")
            conn.commit()
            conn.close()            
        except (Exception, psycopg2.Error) as error:
             print("Failed to insert record", error)
        self.Limpiar()
    #Funciones Para obtener los OptionMenus
    def getOpcion1(self, getOpcion1):
        getOpcion1 = self.var1.get()
        return getOpcion1
   
        
    def getOpcion2(self, getOpcion2):
        getOpcion2 = self.var2.get()
        return getOpcion2

    #Funcion para Limpiar la informacion de los textos
    def Limpiar(self):
        self.entry_NumeroPresu.delete(0, END)
        self.entry_Cliente.delete(0, END)
        self.entryFecha.delete(0, END)

#funcion para mostrar la ventana
def main():
    windows = Tk()
    application = Ventana(windows)
    windows.mainloop()     
      
#LLamar a la funcion
if __name__ == '__main__':
   main()
   