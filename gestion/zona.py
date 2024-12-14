from zoologico import Zoologico
from zooAnimales.animal import Animal

class Zona:
    def __init__(self, nombre: str, zoo: Zoologico, animales = list[Animal]):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = animales
    
    def agregarAnimales(self, nuevosAnimales: list[Animal]):
        self._animales += nuevosAnimales

    def cantidadAnimales(self):
        return len(self._animales)

    def getNombre(self):
        return self._nombre

    def setNombre(self, nuevoNombre: str):
        self._nombre = nuevoNombre

    def getZoo(self):
        return self._zoo

    def setZoo(self, nuevoZoo: Zoologico):
        self._zoo = nuevoZoo

    def getAnimales(self):
        return self._animales

    def setAnimales(self, nuevosAnimales: list[Animal]):
        self._animales = nuevosAnimales