# EJEMPLO DE IMPLEMENTACION DE COLA DE PRIORIDAD CON MONTICULOS
# ---------------------------------------------------------------
# Descripcion del problema:
# Una determinada impresora procesa, tras un determinado tiempo,
# archivos que diferentes usuarios le envían de acuerdo a un orden
# establecido por la universidad en la que se encuentra.
#
# Para este ejemplo, este es dicho orden, en el que el de menor
# número se procesa primero:
#
# 1. Rectorado y documentos oficiales
# 2. Facultades y Unidades académicas
# 3. Otros departamentos y organismos internos
# 4. Docentes
# 5. Alumnos
#
# El presente ejemplo busca brindar el orden de impresión de un
# bloque
# ----------------------------------------------------------------
#
# Grupo 0
#
# TENORIO QUIROZ Bruno Gustavo     20145679
# ROJAS MAYHUA   Rubí Estefanía    20161215
# SOSA PEZO      Carlos Alberto    20161310

#-----------------------------------------------------------------




# Este paquete permite conectar la implementacion en Prolog con la interfaz en Python
from pyswip import Prolog
prolog = Prolog()
prolog.consult("p_queue.pl")

# Tkinter es un paquete para interfaz grafica en Python
from tkinter import *
from tkinter import ttk, Tk, BOTH
from tkinter.ttk import Frame, Button, Style

# Transforma el archivo de texto en una lista
#def leer_datos(ordenes_de_impresion, ubicacion):

def leer_datos(ordenes_de_impresion):

    # Abrimos el archivo para leer su contenido
    Hf = open ('orden_impresion.txt','r')
    ordenes = Hf.read() #almacena una cadena de caracteres
    Hf.close()

    # separa la prioridad y la ruta de cada archivo y los guarda en una lista
    ordenes_de_impresion = ordenes.split()

def consultar(ordenes_de_impresion,orden_final):


    if ordenes_de_impresion != []:

        for ini in prolog.query("monticulo_vacio(H)"):
            H = ini["H"]

        cont = len(ordenes_de_impresion) // 2

        for i in range(cont):
            consulta = "anadir_elemento(" + H + "," + ordenes_de_impresion[2*i] + "," + ordenes_de_impresion[2*i + 1] + ",H)"
            for resultado in prolog.query(consulta):
                H = resultado["H"]
                H = H.replace("Functor(8253837,3,","t(")

        for i in range(cont):
            consulta = "obtener_primero(" + H + ", P,E,H)"
            for resultado in prolog.query(consulta):
                orden_final.append(resultado["E"])
                H = resultado["H"]
                H = H.replace("Functor(8253837,3,","t(")

        orden_final.reverse()

class Ventana(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.style = Style()
        self.style.theme_use("default")

        self.master.title("Ordenes de impresión")
        self.pack(fill=BOTH, expand=1)

        label1 = Label(self, text="Ingresa la ubicación del archivo de órdenes de impresión").place(x=10, y=10)
        #caja1=Entry(self, textvariable=ubicacion).place(x=30, y=80)
        caja1=Entry(self).place(x=30, y=80)

        processButton = Button(self, text="Hallar orden",
            command = consultar(ordenes_de_impresion, orden_final))
        processButton.place(x = 0, y = 250)

        label2 = Label(self, text= orden_final).place(x=10, y=10)

        inputButton = Button(self, text="Cargar archivo",
            command = leer_datos(ordenes_de_impresion))
        inputButton.place(x = 125, y = 250)

        quitButton = Button(self, text="Salir",
            command=self.quit)
        quitButton.place(x=250, y=250)



# Para definir la ventana principal
raiz = Tk()
orden_final = ''

# Inicializamos las variables
ordenes_de_impresion = []


# Definimos las dimensiones de la pantalla
raiz.geometry("400x300+300+300")

# Llamamos al contenido de la ventana
app = Ventana()

#Dejamos la ventana activa
raiz.mainloop()
