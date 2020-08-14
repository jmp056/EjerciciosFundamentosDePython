listado = list()
unicos = 0

while True:
    nombre = input()
    if(nombre == 'parar'):
        break
    else:
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

for art in listado:
    apariciones = 0
    for a in listado:
        if(art['nombre'] == a['nombre']):
            apariciones += 1
    if(apariciones == 1):
        unicos += 1

print("La lista contiene un total de", len(listado), "articulos")
print("La lista contiene un total de", unicos, "articulos unicos")