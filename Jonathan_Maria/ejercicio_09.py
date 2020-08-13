listado = list()
unicos = 0

while True:
    art = input()
    if(art == 'parar'):
        break
    else:
        articulo = {
            'nombre': art,
            'cantidad': input(),
            'precio': input(),
        }
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