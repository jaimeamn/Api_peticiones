from criptos.models import CriptoValorModel, APIError
from criptos.view import CriptoValorView
from criptos.config import API_KEY

class CriptoValorController:
    def __init__(self):
        self.vista = CriptoValorView()
        self.modelo = CriptoValorModel(API_KEY)

    def ejecutar(self):
        self.vista.pedir()
        self.modelo.origen = self.vista.origen
        self.modelo.destino = self.vista.destino
        try:
            self.modelo.obtener_tasa()
            self.vista.mostrar(self.modelo.tasa)
        except APIError as e:
            self.vista.error(e.args[0])
