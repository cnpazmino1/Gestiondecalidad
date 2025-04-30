import unittest
from src.procesador import Analizador
import unittest
from src.procesador import Analizador

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("data/sri_ventas_2024.csv")

    def test_ventas_totales_como_diccionario(self):
        resumen = self.analizador.ventas_por_provincia()
        self.assertIsInstance(resumen, dict)

    def test_cantidad_de_provincias(self):
        resumen = self.analizador.ventas_por_provincia()
        total_provincia = len(resumen)
        self.assertEqual(total_provincia, 25)

    def test_valores_de_ventas_mayores_a_cero(self):
        resumen = self.analizador.ventas_por_provincia()
        self.assertTrue(all(float(v) > 0 for v in resumen.values()))

    def test_ventas_por_provincia_inexistente():