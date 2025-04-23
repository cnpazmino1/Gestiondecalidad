import csv
from collections import defaultdict

class Analizador:
    def __init__(self, archivo_csv):
        self.datos = []
        try:
            try:
                with open(archivo_csv, mode='r', encoding='utf-8') as file:
                    self.datos = self._procesar_csv(file)
            except UnicodeDecodeError:
                with open(archivo_csv, mode='r', encoding='latin-1') as file:
                    self.datos = self._procesar_csv(file)
        except Exception as e:
            raise ValueError(f"Error al leer el archivo CSV: {str(e)}")

    def _procesar_csv(self, file):
        lector = csv.DictReader(file, delimiter='|')
        datos = []
        for fila in lector:
            try:
                valor_ventas = fila["TOTAL_VENTAS"].strip()
                if valor_ventas.upper() == "ND":
                    continue  # Si prefieres, cambia esto por: fila["TOTAL_VENTAS"] = 0.0
                fila["TOTAL_VENTAS"] = float(valor_ventas.replace(',', '.'))
                datos.append(fila)
            except (ValueError, KeyError) as e:
                print(f"Error al procesar fila: {fila} -> {e}")
        return datos

    def ventas_por_provincia(self):
        resultado = defaultdict(float)
        for registro in self.datos:
            resultado[registro['PROVINCIA']] += registro['TOTAL_VENTAS']
        return dict(resultado)

    def ventas_de_provincia(self, nombre_provincia):
        total = 0.0
        for registro in self.datos:
            if registro['PROVINCIA'].lower() == nombre_provincia.lower():
                total += registro['TOTAL_VENTAS']
        return total
