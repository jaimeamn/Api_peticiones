import requests
from criptos import URL_TASA_ESPECIFICA
from criptos.errors import APIError, CONNECT_ERROR

class CriptoValorModel:
    def __init__(self, apikey, origen = "", destino = ""):
        self.apikey = apikey
        self.origen = origen
        self.destino = destino

        self.tasa = 0.0

    def obtener_tasa(self, time=""):
        try:
            respuesta = requests.get(URL_TASA_ESPECIFICA.format(
                self.origen,
                self.destino,
                self.apikey
            ))
        except:
            raise APIError(CONNECT_ERROR)            

        if respuesta.status_code != 200:
            #raise APIError(respuesta.status_code, respuesta.json()["error"])
            raise APIError(respuesta.status_code)

        self.tasa = round(respuesta.json()["rate"], 2)