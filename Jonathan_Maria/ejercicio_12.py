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
            articulo = {
                'nombre': nombre,
                'cantidad': cantidad,
                'precio': precio,
                'monto_a_pagar': monto_a_pagar
            }
            print(monto_a_pagar)
            listado.append(articulo)

print("Nombre\tCantidad\tPrecio\tMonto a pagar")
for art in listado:
    print(art['nombre'],"\t",art['cantidad'],"\t",art['precio'],"\t",art['monto_a_pagar'],"\n")