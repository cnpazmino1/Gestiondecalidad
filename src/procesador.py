import csv
from collections import defaultdict

class Analizador:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.datos = self._cargar_datos()

    def _cargar_datos(self):
        datos = []
        with open(self.archivo_csv, newline='', encoding='latin1') as csvfile:
            lector = csv.DictReader(csvfile, delimiter=';')  # <---- AQUÍ CAMBIADO
            print("Columnas encontradas:", lector.fieldnames)
            for fila in lector:
                datos.append(fila)
        return datos

    def ventas_totales_por_provincia(self):
        resumen = defaultdict(float)
        for fila in self.datos:
            provincia = fila['PROVINCIA']
            ventas = float(fila['TOTAL_VENTAS'].replace(',', '.'))  # corregido el problema de la coma
            resumen[provincia] += ventas
        return resumen

    def ventas_por_provincia(self, nombre):
        resumen = self.ventas_totales_por_provincia()
        return resumen.get(nombre, 0.0)

