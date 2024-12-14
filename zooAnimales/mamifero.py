from animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos, leones = 0, 0

    def __init__(self, nombre: str, edad: int, habitat: str, genero: str, pelaje: bool, patas: int):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)

    @classmethod
    def crearCaballo(cls, nombre: str, edad: int, genero: str):
        cls(nombre, edad, 'pradera', genero, True, 4)
        cls.caballos += 1

    @classmethod
    def crearLeon(cls, nombre: str, edad: int, genero: str):
        cls(nombre, edad, 'selva', genero, True, 4)
        cls.leones += 1

    def getPelaje(self):
        return self._pelaje

    def setPelaje(self, nuevoPelaje: bool):
        self._pelaje = nuevoPelaje

    def getPatas(self):
        return self._patas

    def setPatas(self, nuevasPatas: int):
        self._patas = nuevasPatas

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, nuevoListado):
        cls._listado = nuevoListado