from abc import ABC, abstractmethod
from parametros import MULTIPLICADOR_BONIFICACION_BEBEDOR
from random import randint


class Bebestible(ABC):
    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = int(precio)

    @abstractmethod
    def consumir(self, jugador):
        pass


class Jugo(Bebestible):
    def __init__(self, nombre, tipo, precio):
        super().__init__(nombre, tipo, precio)

    def consumir(self, jugador):
        if jugador.personalidad == "Bebedor":
            ponderador = MULTIPLICADOR_BONIFICACION_BEBEDOR
        else:
            ponderador = 1
        energia_recupera = randint(20, 50)
        jugador.dinero -= self.precio
        if len(self.nombre) <= 4:
            jugador.ego += round(4 * ponderador)
            aumento = round(4 * ponderador)
            jugador.energia += round(energia_recupera * ponderador)
            aumento_energia = round(energia_recupera * ponderador)
            print(f"Su ego ha aumentado en {aumento}")
            print(f"Su energía ha aumentado en {aumento_energia}")
        elif len(self.nombre) >= 5 and len(self.nombre) <= 7:
            jugador.suerte += round(7 * ponderador)
            aumento = round(7 * ponderador)
            jugador.energia += round(energia_recupera * ponderador)
            aumento_energia = round(energia_recupera * ponderador)
            print(f"Su energía ha aumentado en {aumento_energia}")
            print(f"Su suerte ha aumentado en {aumento}")
        elif len(self.nombre) >= 8:
            jugador.frustracion -= round(10 * ponderador)
            jugador.ego += round(11 * ponderador)
            aumento_1 = round(10 * ponderador)
            aumento_2 = round(11 * ponderador)
            jugador.energia += round(energia_recupera * ponderador)
            aumento_energia = round(energia_recupera * ponderador)
            print(f"Su energía ha aumentado en {aumento_energia}")
            print(
                f"Su ego ha aumentado en {aumento_2}, pero tu frustración bajo en {aumento_1}")


class Gaseosa(Bebestible):
    def __init__(self, nombre, tipo, precio):
        super().__init__(nombre, tipo, precio)

    def consumir(self, jugador):
        if jugador.personalidad == "Bebedor":
            ponderador = MULTIPLICADOR_BONIFICACION_BEBEDOR
        else:
            ponderador = 1
        energia_recupera = randint(20, 50)
        jugador.dinero -= self.precio
        if jugador.personalidad in ["Tacaño", "Ludopata"]:
            jugador.frustracion -= round(5 * ponderador)
            jugador.ego += round(6 * ponderador)
            aumento_1 = round(5 * ponderador)
            aumento_2 = round(6 * ponderador)
            jugador.energia += round(energia_recupera * ponderador)
            aumento_energia = round(energia_recupera * ponderador)
            print(f"Su energía ha aumentado en {aumento_energia}")
            print(f"Su frustración ha disminuido en {aumento_1}")
            print(f"Su ego ha aumentado en {aumento_2}")
        elif jugador.personalidad in ["Bebedor", "Casual"]:
            jugador.frustracion += round(5 * ponderador)
            jugador.ego += round(6 * ponderador)
            aumento_1 = round(5 * ponderador)
            aumento_2 = round(6 * ponderador)
            jugador.energia += round(energia_recupera * ponderador)
            aumento_energia = round(energia_recupera * ponderador)
            print(f"Su energía ha aumentado en {aumento_energia}")
            print(f"Su frustracion ha aumentado en {aumento_1}")
            print(f"Su ego ha aumentado en {aumento_2}")


class Brebaje_magico(Bebestible):
    def __init__(self, nombre, tipo, precio):
        super().__init__(nombre, tipo, precio)

    def consumir(self, jugador):
        if jugador.personalidad == "Bebedor":
            ponderador = MULTIPLICADOR_BONIFICACION_BEBEDOR
        else:
            ponderador = 1
        jugador.dinero -= self.precio
        energia_recupera = randint(20, 50)
        if len(self.nombre) <= 4:
            jugador.ego += round(4 * ponderador)
            aumento = round(4 * ponderador)
            print(f"Su ego ha aumentado en {aumento}")
        elif len(self.nombre) >= 5 and len(self.nombre) <= 7:
            jugador.suerte += round(7 * ponderador)
            aumento = round(7 * ponderador)
            print(f"Su suerte ha aumentado en {aumento}")
        elif len(self.nombre) >= 8:
            jugador.frustracion -= round(10 * ponderador)
            jugador.ego += round(11 * ponderador)
            aumento_1 = round(10 * ponderador)
            aumento_2 = round(11 * ponderador)
            print(
                f"Su ego ha aumentado en {aumento_2}, pero tu frustración bajo en {aumento_1}")
        if jugador.personalidad in ["Tacaño", "Ludopata"]:
            jugador.frustracion -= round(5 * ponderador)
            jugador.ego += round(6 * ponderador)
            aumento_1 = round(5 * ponderador)
            aumento_2 = round(6 * ponderador)
            print(f"Su frustración ha disminuido en {aumento_1}")
            print(f"Su ego ha aumentado en {aumento_2}")
        elif jugador.personalidad in ["Bebedor", "Casual"]:
            jugador.frustracion += round(5 * ponderador)
            jugador.ego += round(6 * ponderador)
            aumento_1 = round(5 * ponderador)
            aumento_2 = round(6 * ponderador)
            print(f"Su frustracion ha aumentado en {aumento_1}")
            print(f"Su ego ha aumentado en {aumento_2}")
        jugador.carisma += round(5 * ponderador)
        aumento = round(5 * ponderador)
        jugador.energia += round(energia_recupera * ponderador)
        aumento_energia = round(energia_recupera * ponderador)
        print(f"Su energía ha aumentado en {aumento_energia}")
        print(f"Su carisma ha aumentado en {aumento}")
