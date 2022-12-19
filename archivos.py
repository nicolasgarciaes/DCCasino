from tabulate import tabulate


class Archivos:
    def __init__(self) -> None:
        pass

    def abrir_jugadores():
        with open("jugadores.csv", encoding="utf-8") as lista_jugadores:
            jugadores = []
            jugadores_totales = []
            primera_linea = lista_jugadores.readline()
            primera_linea = primera_linea.strip().split(',')
            for linea in lista_jugadores:
                lista = []
                for i in linea.strip().split(","):
                    lista.append(i)
                indice = 0
                lista.append(linea)
                dict_info_jugador = {}
                for nombre_columna in primera_linea:
                    dict_info_jugador[nombre_columna] = lista[indice]
                    indice += 1
                jugadores.append([dict_info_jugador["nombre"],
                                 dict_info_jugador["personalidad"]])
                jugadores_totales.append([dict_info_jugador["nombre"], dict_info_jugador["personalidad"], dict_info_jugador["energia"], dict_info_jugador["suerte"], dict_info_jugador["dinero"],
                                          dict_info_jugador["frustracion"], dict_info_jugador["ego"], dict_info_jugador["carisma"], dict_info_jugador["confianza"], dict_info_jugador["juego favorito"]])
            tabla = tabulate(jugadores, headers=[
                "Nombre", "Personalidad"], showindex=True, stralign="center")
        # codigo el cual me retorna una lista de listas, con cada usuario ordenado de la manera correcta para el funcionamiento del codigo
        return tabla, jugadores, jugadores_totales

    def abrir_juegos():
        with open("juegos.csv", encoding="utf-8") as lista_juegos:
            juegos = []
            juegos_totales = []
            primera_linea = lista_juegos.readline()
            primera_linea = primera_linea.strip().split(',')
            for linea in lista_juegos:
                lista = []
                for i in linea.strip().split(","):
                    lista.append(i)
                indice = 0
                lista.append(linea)
                dict_info_juego = {}
                for nombre_columna in primera_linea:
                    dict_info_juego[nombre_columna] = lista[indice]
                    indice += 1
                juegos.append([dict_info_juego["nombre"]])
                juegos_totales.append([dict_info_juego["nombre"], dict_info_juego["esperanza"],
                                      dict_info_juego["apuesta maxima"], dict_info_juego["apuesta minima"]])
            tabla = tabulate(juegos, headers=[
                "Nombre"], showindex=True, stralign="center")
        return tabla, juegos, juegos_totales

    def abrir_bebestibles():
        with open("bebestibles.csv", encoding="utf-8") as lista_bebestibles:
            bebestibles = []
            primera_linea = lista_bebestibles.readline()
            primera_linea = primera_linea.strip().split(',')
            for linea in lista_bebestibles:
                lista = []
                for i in linea.strip().split(","):
                    lista.append(i)
                indice = 0
                lista.append(linea)
                dict_info_bebestible = {}
                for nombre_columna in primera_linea:
                    dict_info_bebestible[nombre_columna] = lista[indice]
                    indice += 1
                bebestibles.append(
                    [dict_info_bebestible["nombre"], dict_info_bebestible["tipo"], dict_info_bebestible["precio"]])
            tabla = tabulate(bebestibles, headers=[
                "Nombre", "Tipo", "Precio"], showindex=True, stralign="center")
        return tabla, bebestibles
