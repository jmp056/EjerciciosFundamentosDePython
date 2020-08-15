listado = list()
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
print("Nombre\tCantidad\tPrecio\tMonto a pagar")
articulo_mas_costoso = {'nombre': " ", 'monto_a_pagar': 0}
articulo_mas_economico = {'nombre': " ", 'monto_a_pagar': 999999999999}
for art in listado:
    print(art['nombre'],"\t",art['cantidad'],"\t",art['precio'],"\t",art['monto_a_pagar'],"\n")
    if(art['monto_a_pagar'] > articulo_mas_costoso['monto_a_pagar']):
        articulo_mas_costoso['nombre'] = art['nombre']
        articulo_mas_costoso['monto_a_pagar'] = art['monto_a_pagar']
    if(art['monto_a_pagar'] < articulo_mas_economico['monto_a_pagar']):
        articulo_mas_economico['nombre'] = art['nombre']
        articulo_mas_economico['monto_a_pagar'] = art['monto_a_pagar']
print("El producto más costoso es:", articulo_mas_costoso['nombre'])
print("El producto más economico es:", articulo_mas_economico['nombre'])
