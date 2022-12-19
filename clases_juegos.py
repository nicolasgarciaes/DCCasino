from archivos import Archivos
from parametros import FRUSTRACION_PERDER, FRUSTRACION_GANAR, CARISMA_GANAR, EGO_GANAR, CONFIANZA_PERDER


class Juego:
    def __init__(self, nombre, esperanza, apuesta_maxima, apuesta_minima):
        self.nombre = nombre
        self.esperanza = int(esperanza)
        self.apuesta_maxima = int(apuesta_maxima)
        self.apuesta_minima = int(apuesta_minima)

    def entregar_resultados(self, jugador, dinero_apostado):
        if jugador.resultado == False:
            print("\nLo siento, perdiste la apuesta")
            jugador.frustracion += FRUSTRACION_PERDER
            jugador.confianza -= CONFIANZA_PERDER
            jugador.dinero -= dinero_apostado
        else:
            print("\n¡ Ganaste la apuesta !")
            print("Duplicaste el dinero apostado")
            jugador.frustracion -= FRUSTRACION_GANAR
            jugador.carisma += CARISMA_GANAR
            jugador.ego += EGO_GANAR
            jugador.dinero += dinero_apostado * 2

    def probabilidad_de_ganar(self, esperanza, apuesta, jugador):
        self.esperanza = esperanza
        self.apuesta = apuesta
        if self.nombre == jugador.juegos_favorito:
            favorito = 1
        else:
            favorito = 0
        probabilidad = min(1, jugador.probabilidad_ganar_jugador(
            apuesta, self) - ((apuesta-(favorito*50-(esperanza*30)))/10000))
        return probabilidad
