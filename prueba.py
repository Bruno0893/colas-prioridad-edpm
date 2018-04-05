from pyswip import Prolog
prolog = Prolog()
prolog.consult("p_queue.pl")


def consultar(ordenes_de_impresion):

    if ordenes_de_impresion != []:

        for ini in prolog.query("monticulo_vacio(H)"):
            H = ini["H"]
            #print(H)

        cont = len(ordenes_de_impresion) // 2

        for i in range(cont):
            consulta = "anadir_elemento(" + H + "," + ordenes_de_impresion[2*i] + "," + ordenes_de_impresion[2*i + 1] + ",H)"
            for resultado in prolog.query(consulta):
                H = resultado["H"]
                H = H.replace("Functor(8253837,3,","t(")

        for i in range(cont):
            consulta = "obtener_primero(" + H + ", P,E,H)"
            for resultado in prolog.query(consulta):
                print(resultado["E"])
                H = resultado["H"]
                H = H.replace("Functor(8253837,3,","t(")




def main():
    # Abrimos el archivo para leer su contenido
    Hf = open ('orden_impresion.txt','r')
    ordenes = Hf.read() #almacena una cadena de caracteres
    Hf.close()

    # separa la prioridad y la ruta de cada archivo y los guarda en una lista
    ordenes_de_impresion = ordenes.split()
    consultar(ordenes_de_impresion)

if __name__ == '__main__':
    main()
