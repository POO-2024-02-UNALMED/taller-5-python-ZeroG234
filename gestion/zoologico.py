class Zoologico:
    def __init__(self, nombre: str, ubicacion: str, zona = []):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zona = zona

    def agregarZonas(self, nuevaZona):
        self._zona.append(nuevaZona)

    def cantidadTotalAnimales(self):
        totalAnimales = 0
        for zona in self._zona:
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

    def getZona(self):
        return self._zona
    
    def setZona(self, nuevaZona):
        self._zona = nuevaZona