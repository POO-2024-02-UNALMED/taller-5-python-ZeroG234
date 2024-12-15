class Animal:
    _totalAnimales = 0

    def __init__(self, nombre: str, edad: int, habitat: str, genero: str, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal._totalAnimales += 1
        self._zona = zona

    def movimiento(self):
        return 'desplazarse'

    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil

        texto =  f'Mamiferos : {Mamifero.cantidadMamiferos()}\n'
        texto += f'Aves : {Ave.cantidadAves()}'
        texto += f'Reptiles : {Reptil.cantidadReptiles()}'
        texto += f'Peces : {Pez.cantidadPeces()}'
        texto += f'Anfibios : {Anfibio.cantidadAnfibios()}'
        return  texto

    def toString(self):
        texto =  f'Mi nombre es {self._nombre}, tengo una edad de {self._edad}, '
        texto += f'habito en {self._habitat} y mi genero es {self._genero}'
        return texto

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