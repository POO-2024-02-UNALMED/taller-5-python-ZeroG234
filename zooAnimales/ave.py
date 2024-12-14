from animal import Animal

class Ave(Animal):
    _listado = []
    halcones, aguilas = 0, 0

    def __init__(self, nombre: str, edad: int, habitat: str, genero: str, colorPlumas: str):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    def movimiento(self):
        return 'volar'

    @classmethod
    def crearHalcon(cls, nombre: str, edad: int, genero: str):
        cls(nombre, edad, 'montañas', genero, 'café y glorioso')
        cls.halcones += 1

    @classmethod
    def crearAguila(cls, nombre: str, edad: int, habitat: str, genero: str, colorPlumas: str):
        cls(nombre, edad, 'montañas', genero, 'blanco y amarillo')
        cls.halcones += 1

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, nuevoColorPlumas):
        self._colorPlumas = nuevoColorPlumas

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, nuevoListado):
        cls._listado = nuevoListado