articulo = " "
listado = list()

while True:
    articulo = input()
    if(articulo == 'parar'):
        break
    else:
        listado.append(articulo)

print("La lista contiene", len(listado), "articulos")