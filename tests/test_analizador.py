import unittest
from src.procesador import Analizador

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("datos/sri_ventas_2024.csv")

    def test_numero_provincias(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertGreaterEqual(len(resumen), 20)

    def test_valores_numericos(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        for total in resumen.values():
            self.assertIsInstance(total, float)
            self.assertGreaterEqual(total, 0)

    def test_retornar_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict)


    def test_provincia_existente(self):
        ventas = self.analizador.ventas_por_provincia("PICHINCHA")
        self.assertIsInstance(ventas, float)

    def test_valores_correctos(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIn("GUAYAS", resumen)
        self.assertIn("PICHINCHA", resumen)
        self.assertIn("MANABÍ", resumen)

if __name__ == '__main__':
    unittest.main()
