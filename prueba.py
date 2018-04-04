from pyswip import Prolog
prolog = Prolog()

def consultar(ordenes_de_impresion):
    if ordenes_de_impresion != []:
        #prolog.query("[p_queue]")

        H = "monticulo(nil,0)"
        for i in range(len(ordenes_de_impresion)//2):
                consulta = "anadir_elemento(" + H + "," + ordenes_de_impresion[2*i] + "," + ordenes_de_impresion[2*i + 1] + ",H)"
                for resultado_parcial in prolog.query(consulta):
                    H = resultado_parcial["H"]
        consulta = "monticulo_a_lista(" + H + ", L)"
        #for resultado in prolog.query(consulta):
            #orden_final = resultado["L"]

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
