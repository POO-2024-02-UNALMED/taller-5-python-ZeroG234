from gestion.zona import Zona
from mamifero import Mamifero
from ave import Ave
from reptil import Reptil
from pez import Pez
from anfibio import Anfibio

class Animal:
    _totalAnimales = 0

    def __init__(self, nombre: str, edad: int, habitat: str, genero: str):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal._totalAnimales += 1
        #self._zona = zona

    def movimiento(self):
        return 'desplazarse'

    def totalPorTipo(self):
        texto =  f'Mamíferos: {Mamifero.cantidadMamiferos()}\n'
        texto += f'Aves: {Ave.cantidadAves()}'
        texto += f'Reptiles: {Reptil.cantidadReptiles()}'
        texto += f'Peces: {Pez.cantidadPeces()}'
        texto += f'Anfibios: {Anfibio.cantidadAnfibios()}'
        return  texto

    def __str__(self):
        return f'Mi nombre es {self._nombre}, tengo una edad de {self._edad},
          habito en {self._habitat} y mi género es {self._genero},
          la zona en la que me ubico es {self._zona}, en el {self._zoo}'

    def getNombre(self):
        return self._nombre

    def setNombre(self, nuevoNombre: str):
        self._nombre = nuevoNombre

    def getEdad(self):
        return self._edad

    def setEdad(self, nuevaEdad: int):
        self._edad = nuevaEdad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, nuevoHabitat: str):
        self._habitat = nuevoHabitat

    def getGenero(self):
        return self._genero

    def setGenero(self, nuevoGenero: str):
        self._genero = nuevoGenero

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    
    @classmethod
    def setTotalAnimales(cls, nuevoTotalAnimales: int):
        cls._totalAnimales = nuevoTotalAnimales