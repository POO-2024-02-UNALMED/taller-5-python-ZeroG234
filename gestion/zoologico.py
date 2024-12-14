from zona import Zona

class Zoologico:
    def __init__(self, nombre: str, ubicacion: str):#, zonas: list[Zona]):
        self._nombre = nombre
        self._ubicacion = ubicacion
        #self._zonas = zonas

    def agregarZonas(self, nuevasZonas: list[Zona]):
        self._zonas += nuevasZonas

    def cantidadTotalAnimales(self):
        totalAnimales = 0
        for zona in self._zonas:
            totalAnimales += zona.cantidadAnimales()

        return totalAnimales

    def getNombre(self):
        return self._nombre

    def setNombre(self, nuevoNombre: str):
        self._nombre = nuevoNombre

    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self, nuevaUbicacion: str):
        self._ubicacion = nuevaUbicacion