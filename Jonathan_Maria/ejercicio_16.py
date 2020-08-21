from archivo import Archivo
import re
ar = Archivo("Datos.txt")
listado = list()

def buscar_articulo(nombre):
    lista = ar.re()
    listado = re.split(' |\n|\t', lista)
    for p in range(0,len(listado)):
        if(listado[p] == nombre):
            articulo = {'nombre': listado[p], 'cantidad': listado[p+1], 'precio':listado[p+2], 'monto_a_pagar': listado[p+3]}
            print(articulo)

buscar_articulo("lo")