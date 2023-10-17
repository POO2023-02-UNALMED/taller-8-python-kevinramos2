class Deportista:
    def __init__(self,añosPracticando):
        self._deporte="Futbol"
        self._añosPracticando=añosPracticando 

    def getDeporte(self):
        return self._deporte
    def setDeporte(self,nuevo):
        self._deporte=nuevo

    def getAñosPracticando(self):
        return self._añosPracticando
    def setAñosPracticando(self,añosPracticando ):
        self._añosPracticando=añosPracticando 
    