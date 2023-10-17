from persona import Persona
from deportista import Deportista

class Futbolista(Persona,Deportista):
    listaFutbolistas = list()

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        
        Futbolista.listaFutbolistas.append(self)

    @classmethod
    def setListaFutbolista(clc, listaFutbolistas):
        clc.listaFutbolistas = listaFutbolistas