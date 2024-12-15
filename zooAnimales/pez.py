from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones, bacalaos = 0, 0

    def __init__(self, nombre: str, edad: int, habitat: str, genero: str, colorEscamas: str, cantidadAletas: int):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)

    def movimiento(self):
        return 'nadar'

    @classmethod
    def crearSalmon(cls, nombre: str, edad: int, genero: str):
        cls.salmones += 1
        return cls(nombre, edad, 'oceano', genero, 'rojo', 6)

    @classmethod
    def crearBacalao(cls, nombre: str, edad: int, genero: str):
        cls.bacalaos += 1
        return cls(nombre, edad, 'oceano', genero, 'gris', 6)

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, nuevoColorEscamas: str):
        self._colorEscamas = nuevoColorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, nuevaCantidadAletas):
        self._cantidadAletas = nuevaCantidadAletas

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, nuevoListado):
        cls._listado = nuevoListado