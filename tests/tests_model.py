import unittest
from criptos.models import CriptoValorModel, APIError
from criptos.config import API_KEY

class TestModel(unittest.TestCase):
    def test_debes_informar_la_api(self):
        cv = CriptoValorModel("0", "BTC", "lolailos")


        with self.assertRaisesRegex(APIError, "401"):
            cv.obtener_tasa()


    def test_la_moneda_debe_existir(self):
        cv = CriptoValorModel(API_KEY, "BTC", "lolailos")

        with self.assertRaisesRegex(APIError, "550"):
            cv.obtener_tasa()