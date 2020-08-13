articulo = " "
listado = list()
unicos = 0

while True:
    articulo = input()
    if(articulo == 'parar'):
        break
    else:
        listado.append(articulo)

for art in listado:
    if(listado.count(art) == 1):
        unicos += 1

print("La lista contiene un total de", len(listado), "articulos")
print("La lista contiene un total de", unicos, "articulos unicos")