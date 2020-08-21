import os

class Archivo():
    Ruta = ""

    def __init__(self, ruta):
        self.Ruta = ruta
        arch = open(self.Ruta, "a+")
        arch.close()

    def es(self, texto):
        arch = open(self.Ruta, "a")
        arch.write(texto)
        arch.close()

    def le(self):
        arch = open(self.Ruta, "r")
        print(arch.read())
        arch.close()

    def re(self):
        arch = open(self.Ruta, "r")
        lista = arch.read()
        arch.close()
        return(lista)

