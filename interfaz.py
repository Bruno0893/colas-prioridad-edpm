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

# Inicializamos las variables
ordenes_de_impresion = []
orden_final = []

# Transforma el archivo de texto en una lista
def leer_datos(ordenes_de_impresion, ubicacion,listbox):
#def leer_datos(ordenes_de_impresion):

    # Abrimos el archivo para leer su contenido
    Hf = open (ubicacion,'r')
    ordenes = Hf.read() #almacena una cadena de caracteres
    Hf.close()
    # separa la prioridad y la ruta de cada archivo y los guarda en una lista
    ordenes_de_impresion = ordenes.split()
    consultar(ordenes_de_impresion, orden_final,listbox)

def consultar(ordenes_de_impresion,orden_final,listbox):
    orden_final = []
    if ordenes_de_impresion != []: #No procesa nada si no hay contenido en la orden de impresion

        for ini in prolog.query("monticulo_vacio(H)"): #Se inicializa el montículo
            H = ini["H"]

        cont = len(ordenes_de_impresion) // 2

        for i in range(cont): #Se añade uno a uno los elementos al montículo mediante consultas sucesivas
            consulta = "anadir_elemento(" + H + "," + ordenes_de_impresion[2*i] + "," + ordenes_de_impresion[2*i + 1] + ",H)"
            for resultado in prolog.query(consulta):
                H = resultado["H"]
                H = H.replace("Functor(8253837,3,","t(")

        for i in range(cont): #Se extrae uno a uno los elementos del montículo, se ubica cada uno al final
            consulta = "obtener_primero(" + H + ", P,E,H)"
            for resultado in prolog.query(consulta):
                orden_vigente = str(i+1) + '. ' + resultado["E"]
                orden_final.append(orden_vigente)
                H = resultado["H"]
                H = H.replace("Functor(8253837,3,","t(")

        for i in orden_final:
            listbox.insert(END,i)

def leer_datos_boton():
    ubicacion = entrada.get()
    listbox.delete(0, END)
    leer_datos(ordenes_de_impresion,ubicacion,listbox)

class Ventana(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.style = Style()
        self.style.theme_use("default")

        self.master.title("Órdenes de impresión")
        self.pack(fill=BOTH, expand=1)


        label1 = Label(raiz, text="Ingresa la ubicación del archivo de órdenes de impresión").place(x=10, y=10)
        caja_ingresa_ubicacion=Entry(self, textvariable=entrada).place(x=30, y=80)

        #Boton para procesar la informacion
        processButton = Button(raiz, text="Hallar orden",
            command = leer_datos_boton)
        processButton.place(x = 0, y = 350)

        quitButton = Button(self, text="Salir",
            command=self.quit)
        quitButton.place(x=300, y=350)



# Para definir la ventana principal
raiz = Tk()

# Se crean las variables para leer la ubicacion del archivo
entrada = StringVar()
ubicacion = StringVar()

# Definimos las dimensiones de la pantalla
raiz.geometry("400x400+400+400")

# Llamamos al contenido de la ventana
app = Ventana()
listbox = Listbox(raiz)
listbox.place(x=30, y=150)

#Dejamos la ventana activa
raiz.mainloop()
