from criptos import MONEDAS

class CriptoValorView:
    def __init__(self):
        self.origen = ""
        self.destino = ""

    def pedir(self):
        origen = input("Moneda origen: ")
        while origen not in MONEDAS:
            print("La moneda debe ser una de las siguientes:")
            print(",".join(MONEDAS))
            origen = input("Moneda origen: ")

        self.origen = origen

        destino = input("Moneda a convertir: ")
        while destino not in MONEDAS:
            print("La moneda debe ser una de las siguientes:")
            print(",".join(MONEDAS))
            destino = input("Moneda a convertir: ")

        self.destino = destino

    def mostrar(self, tasa):
        print("1 {} son {:.2f} {}".format(self.origen, tasa, self.destino))