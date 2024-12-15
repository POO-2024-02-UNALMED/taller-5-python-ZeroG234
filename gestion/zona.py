from gestion.zoologico import Zoologico
#from zooAnimales.animal import Animal

class Zona:
    def __init__(self, nombre: str, zoo: Zoologico = None, animales = []):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = animales
    
    def agregarAnimales(self, nuevoAnimal):
        self._animales.append(nuevoAnimal)

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

    def setAnimales(self, nuevosAnimales):
        self._animales = nuevosAnimales