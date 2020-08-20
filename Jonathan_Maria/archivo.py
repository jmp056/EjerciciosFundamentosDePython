import os

class Archivo():
    Ruta = ""

    def __init__(self, ruta):
        self.Ruta = ruta
        arch = open(self.Ruta, "a+")
        arch.close()

    def es(self, texto):
        arch = open(self.Ruta, "a")
        #line, escribir = "", True
        arch.write(texto)
        arch.close()
        #while escribir:
        #    self.menu()
        #    line = input("Escriba algo en el archivo: ")
        #    line += "\n"
        #    arch.write(line)
        #    resp = input("\n¿Seguir escribiendo? Introduzca \"n\" pasa salir. ")
        #    if resp.lower() == "n":
        #        escribir = False
        #    else:
        #        os.system("cls")
        

    def le(self):
        arch = open(self.Ruta, "r")
        #print("\nContenido del archivo : \n")
        print(arch.read())
        arch.close()

    def menu(self):
        os.system("title = ArchiPy - By TurKux")
        os.system("cls")
        print("\n")
        print("manejar archivos de texto".upper().center(50, "-"))
        print("\n")
