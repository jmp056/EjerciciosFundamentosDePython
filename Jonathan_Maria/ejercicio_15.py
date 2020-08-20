from archivo import Archivo
listado = list()
ar = Archivo("Datos.txt")
te = ""
while True:
    nombre = input()
    existe = 0
    if(nombre == 'parar'):
        break
    else:
        for art in listado:
            if(art['nombre'] == nombre):
                print("Ya este producto se encuentra en la lista, ingrese otro")
                existe = 1
                break
        if(existe == 0):
            cantidad = int(input())
            precio = int(input())
            monto_a_pagar = cantidad * precio
            articulo = {'nombre': nombre, 'cantidad': cantidad, 'precio': precio, 'monto_a_pagar': monto_a_pagar}
            print(monto_a_pagar)
            listado.append(articulo)           
ar.es("Nombre\tCantidad\tPrecio\tMonto a pagar")
ar.es("\n")
articulo_mas_costoso = {'nombre': " ", 'monto_a_pagar': 0}
articulo_mas_economico = {'nombre': " ", 'monto_a_pagar': 999999999999}
for art in listado:
    ar.es(art['nombre']),ar.es("\t"),ar.es(str(art['cantidad'])),ar.es("\t"),ar.es(str(art['precio'])),ar.es("\t"),ar.es(str(art['monto_a_pagar'])),ar.es("\n")
    if(art['monto_a_pagar'] > articulo_mas_costoso['monto_a_pagar']):
        articulo_mas_costoso['nombre'] = art['nombre']
        articulo_mas_costoso['monto_a_pagar'] = art['monto_a_pagar']
    if(art['monto_a_pagar'] < articulo_mas_economico['monto_a_pagar']):
        articulo_mas_economico['nombre'] = art['nombre']
        articulo_mas_economico['monto_a_pagar'] = art['monto_a_pagar']
ar.es("El producto más costoso es:"), ar.es(articulo_mas_costoso['nombre'])
ar.es("\n")
ar.es("El producto más economico es:"), ar.es(articulo_mas_economico['nombre'])
ar.le()
print("Se ha guardado la lista en el fichero: Datos.txt")




