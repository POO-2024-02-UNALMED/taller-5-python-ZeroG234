from animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas, salamandras = 0, 0

    def __init__(self, nombre: str, edad: int, habitat: str, genero: str, colorPiel: str, venenoso: bool):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    def movimiento(self):
        return 'saltar'

    @classmethod
    def crearRana(cls, nombre: str, edad: int, genero: str):
        cls(nombre, edad, 'selva', genero, 'rojo', True)
        cls.ranas += 1

    @classmethod
    def crearSalamandra(cls, nombre: str, edad: int, genero: str):
        cls(nombre, edad, 'selva', genero, 'negro y amarillo', False)
        cls.salamandras += 1

    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, nuevoColorPiel: str):
        self._colorPiel = nuevoColorPiel

    def isVenenoso(self):
        return self._venenos

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, nuevoListado):
        cls._listado = nuevoListado