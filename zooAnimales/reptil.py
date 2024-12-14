from animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas, serpientes = 0, 0

    def __init__(self, nombre: str, edad: int, habitat: str, genero: str, colorEscamas: str, largoCola: int):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    def movimiento(self):
        return 'reptar'

    @classmethod
    def crearIguana(cls, nombre: str, edad: int, genero: str):
        Reptil(nombre, edad, 'humedal', genero, 'verde', 3)
        cls.iguanas += 1

    @classmethod
    def crearSerpiente(cls, nombre: str, edad: int, genero: str):
        Reptil(nombre, edad, 'jungla', genero, 'blanco', 1)
        cls.serpientes += 1

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, nuevoColorEscamas: str):
        self._colorEscamas = nuevoColorEscamas

    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self, nuevoLargoCola: int):
        self._largoCola = nuevoLargoCola

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, nuevoListado):
        cls._listado = nuevoListado