from parametros import BONIFICACION_SUERTE_CASUAL, BONIFICACION_TACANO, \
    PORCENTAJE_APUESTA_TACANO, ENERGIA_MAX, ENERGIA_MIN, SUERTE_MAX, SUERTE_MIN, \
    FRUSTRACION_MAX, FRUSTRACION_MIN, EGO_MAX, EGO_MIN, CARISMA_MAX, CARISMA_MIN, CONFIANZA_MAX, CONFIANZA_MIN
from random import random


class Jugador:
    def __init__(self, nombre, personalidad, energia, suerte, dinero, frustracion, ego, carisma, confianza, juego_favorito):
        self.nombre = nombre
        self.personalidad = personalidad
        self.__energia = int(energia)
        self.__suerte = int(suerte)
        self.__dinero = int(dinero)
        self.__frustracion = int(frustracion)
        self.__ego = int(ego)
        self.__carisma = int(carisma)
        self.__confianza = int(confianza)
        self.juegos_favorito = juego_favorito
        self.juegos_jugados = []

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, valor):
        if valor in range(0, 101):
            self.__energia = int(valor)
        elif valor > ENERGIA_MAX:
            self.__energia = ENERGIA_MAX
        elif valor < ENERGIA_MIN:
            self.__energia = ENERGIA_MIN

    @property
    def dinero(self):
        return self.__dinero

    @dinero.setter
    def dinero(self, valor):
        if valor >= 0:
            self.__dinero = int(valor)
        elif valor < 0:
            self.__dinero = 0

    @property
    def suerte(self):
        return self.__suerte

    @suerte.setter
    def suerte(self, valor):
        if valor in range(0, 51):
            self.__suerte = int(valor)
        elif valor > SUERTE_MAX:
            self.__suerte = SUERTE_MAX
        elif valor < SUERTE_MIN:
            self.__suerte = SUERTE_MIN

    @property
    def frustracion(self):
        return self.__frustracion

    @frustracion.setter
    def frustracion(self, valor):
        if valor in range(0, 101):
            self.__frustracion = int(valor)
        elif valor > FRUSTRACION_MAX:
            self.__frustracion = FRUSTRACION_MAX
        elif valor < FRUSTRACION_MIN:
            self.__frustracion = FRUSTRACION_MIN

    @property
    def ego(self):
        return self.__ego

    @ego.setter
    def ego(self, valor):
        if valor in range(0, 16):
            self.__ego = int(valor)
        elif valor > EGO_MAX:
            self.__ego = EGO_MAX
        elif valor < EGO_MIN:
            self.__ego = EGO_MIN

    @property
    def carisma(self):
        return self.__carisma

    @carisma.setter
    def carisma(self, valor):
        if valor in range(0, 51):
            self.__carisma = int(valor)
        elif valor > CARISMA_MAX:
            self.__carisma = CARISMA_MAX
        elif valor < CARISMA_MIN:
            self.__carisma = CARISMA_MIN

    @property
    def confianza(self):
        return self.__confianza

    @confianza.setter
    def confianza(self, valor):
        if valor in range(0, 31):
            self.__confianza = int(valor)
        elif valor > CONFIANZA_MAX:
            self.__confianza = CONFIANZA_MAX
        elif valor < CONFIANZA_MIN:
            self.__confianza = CONFIANZA_MIN

    def apostar(self, dinero_apostado, juego):
        self.energia -= round((self.ego + self.frustracion)*0.15)
        if self.personalidad == "Casual":
            if self.suerte_principiante(juego.nombre) == "primera vez":
                self.suerte += BONIFICACION_SUERTE_CASUAL
                print(f"Recibiste la bonificación de suerte de jugador casual")
        if juego.probabilidad_de_ganar(juego.esperanza, dinero_apostado, self) > random():
            self.resultado = True
            
        else:
            self.resultado = False

    def comprar_bebestible(self, bebestible):
        if self.dinero >= bebestible.precio:
            bebestible.consumir(self)
        else:
            return False

    def probabilidad_ganar_jugador(self, dinero_apostado, juego):
        if juego.nombre == self.juegos_favorito:
            favorito = 1
        else:
            favorito = 0
        probabilidad_ganar_jugador = min(1, max(
            0, ((self.suerte * 15 - dinero_apostado * 0.4 + self.confianza * 3 * favorito + self.carisma * 2)/1000)))
        return probabilidad_ganar_jugador

    def contador_juegos_repetidos(self, nombre_juego):
        repeteciones = {}
        for juego in self.juegos_jugados:
            if juego in repeteciones:
                repeteciones[juego] += 1
            else:
                repeteciones[juego] = 0
        return repeteciones


class Ludopata(Jugador):
    def __init__(self, nombre, personalidad, energia, suerte, dinero, frustracion, ego, carisma, confianza, juego_favorito):
        super().__init__(nombre, personalidad, energia, suerte, dinero,
                         frustracion, ego, carisma, confianza, juego_favorito)

    def ludopatia(self, dinero_apostado, juego):
        super().apostar(dinero_apostado, juego)
        self.ego += 2
        self.suerte += 3
        if self.resultado == False:
            self.frustracion += 5


class Tacaño(Jugador):
    def __init__(self, nombre, personalidad, energia, suerte, dinero, frustracion, ego, carisma, confianza, juego_favorito):
        super().__init__(nombre, personalidad, energia, suerte, dinero,
                         frustracion, ego, carisma, confianza, juego_favorito)

    def tacaño_extremo(self, dinero_apostado, juego):
        super().apostar(dinero_apostado, juego)
        if self.dinero * PORCENTAJE_APUESTA_TACANO > dinero_apostado:
            if self.resultado:
                self.dinero += BONIFICACION_TACANO


class Bebedor(Jugador):
    def __init__(self, nombre, personalidad, energia, suerte, dinero, frustracion, ego, carisma, confianza, juego_favorito):
        super().__init__(nombre, personalidad, energia, suerte, dinero,
                         frustracion, ego, carisma, confianza, juego_favorito)

    def cliente_recurrente(self, bebestible):
        super().comprar_bebestible(bebestible)


class Casual(Jugador):
    def __init__(self, nombre, personalidad, energia, suerte, dinero, frustracion, ego, carisma, confianza, juego_favorito):
        super().__init__(nombre, personalidad, energia, suerte, dinero,
                         frustracion, ego, carisma, confianza, juego_favorito)
        self.suerte_casual = 0

    def suerte_principiante(self, nombre_juego):
        super().contador_juegos_repetidos(nombre_juego)
        reps = self.contador_juegos_repetidos(nombre_juego)
        if reps[nombre_juego] == 0:
            return "primera vez"
        else:
            return "segunda vez o más"
