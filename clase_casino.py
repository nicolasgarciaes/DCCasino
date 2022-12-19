from archivos import Archivos
from clases_bebestibles import Jugo, Brebaje_magico, Gaseosa
from clases_jugadores import Tacaño, Bebedor, Casual, Ludopata
from clases_juegos import Juego
from parametros import PROBABILIDAD_EVENTO
from random import randint, random
from parametros import VALOR_DEUDA, DINERO_SHOW, ENERGIA_SHOW, FRUSTRACION_SHOW


class Casino:
    def __init__(self) -> None:
        pass

    def evento_especial(jugador):
        bebestible_al_azar = Archivos.abrir_bebestibles()[1][randint(0, 12)]
        if bebestible_al_azar[1] == "Jugo":
            bebestible_escodigo = Jugo(
                bebestible_al_azar[0], bebestible_al_azar[1], int(bebestible_al_azar[2]))
        elif bebestible_al_azar[1] == "Gaseosa":
            bebestible_escodigo = Gaseosa(
                bebestible_al_azar[0], bebestible_al_azar[1], int(bebestible_al_azar[2]))
        elif bebestible_al_azar[1] == "Brebaje mágico":
            bebestible_escodigo = Brebaje_magico(
                bebestible_al_azar[0], bebestible_al_azar[1], int(bebestible_al_azar[2]))
        if PROBABILIDAD_EVENTO > random():
            print("\n¡¡¡ Ocurrio el evento especial !!!")
            print(f"Te ganaste: {bebestible_escodigo.nombre}")
            precio_bebestible = bebestible_escodigo.precio
            jugador.dinero += precio_bebestible
            if jugador.personalidad == "Bebedor":
                jugador.cliente_recurrente(bebestible_escodigo)
            else:
                jugador.comprar_bebestible(bebestible_escodigo)
        else:
            print("\nNo ocurrio el evento especial")

    def jugar(jugador, dinero_apostado, juego):
        if jugador.personalidad == "Ludopata":
            jugador.ludopatia(int(dinero_apostado), juego)
            juego.entregar_resultados(jugador, int(dinero_apostado))
            Casino.evento_especial(jugador)
        elif jugador.personalidad == "Tacano":
            jugador.tacaño_extremo(int(dinero_apostado), juego)
            juego.entregar_resultados(jugador, int(dinero_apostado))
            Casino.evento_especial(jugador)
        elif jugador.personalidad == "Casual":
            jugador.suerte_principiante(juego.nombre)
            jugador.apostar(int(dinero_apostado), juego)
            juego.entregar_resultados(jugador, int(dinero_apostado))
            Casino.evento_especial(jugador)
        else:
            jugador.apostar(int(dinero_apostado), juego)
            juego.entregar_resultados(jugador, int(dinero_apostado))
            Casino.evento_especial(jugador)
        Casino.verificar_deuda(jugador)
        Casino.menu_principal(jugador)

    def verificar_estado_apuestas(jugador):
        if jugador.dinero == 0:
            print("\nYa no posees dinero, perdiste el juego")
            print("No puedes realizar apuestas")
            Casino.menu_principal(jugador)
        elif jugador.energia < round((jugador.ego + jugador.frustracion)*0.15):
            print(
                "\nNo posees suficiente energía, debes comprar un bebestible y ver si puedes seguir jugando")
            Casino.menu_principal(jugador)

    def verificar_estado_bebestible(jugador):
        if jugador.energia < round((jugador.ego + jugador.frustracion)*0.15) and jugador.dinero < 102:
            print(
                "\nNo posees la energía mínima para apostar y no posees el dinero suficiente para comprar el bebestible de menor precio.")
            print("Te recomiendo volver al menú anterior o abandonar el juego.")

    def verificar_deuda(jugador):
        if jugador.dinero >= VALOR_DEUDA:
            print("\n¡¡¡ Lograste pagar tu deuda !!!")
            print("Serás redirigido al menú de inicio")
            Casino.menu_inicio()

    def show(jugador):
        if jugador.dinero >= DINERO_SHOW:
            jugador.energia += ENERGIA_SHOW
            jugador.frustracion -= FRUSTRACION_SHOW
            jugador.dinero -= DINERO_SHOW
            print("\nBienvenido al Show")
            print(f"\nPerdiste {DINERO_SHOW} por entrar al Show")
            print(f"\nGanaste {ENERGIA_SHOW} de energía")
            print(f"Perdiste {FRUSTRACION_SHOW} de frustración")
            Casino.menu_principal(jugador)
        else:
            print("\nNo posees suficiente dinero para ver el Show")
            Casino.menu_principal(jugador)

    def menu_inicio():

        etapa_menu_inicio = True
        while etapa_menu_inicio:
            print("\n----- DCCasino -----\n"
                  "\n** Menú de inicio **\n\nSelecciona una de las siguientes opciones:\n"
                  "\n [1]: Iniciar partida \n [x]: Salir ")
            opcion_elegida = input("\nIndique la opción elegida: ")
            if opcion_elegida == "1":
                Casino.opciones_jugador()
                etapa_menu_inicio = False
            elif opcion_elegida in ["X", "x"]:
                print("\nHasta luego")
                etapa_menu_inicio = False
                return
            else:
                print("\nOpción no valida, reintentalo")
                etapa_menu_inicio = True

    def opciones_jugador():

        etapa_elegir_jugador = True
        while etapa_elegir_jugador:
            indice_volver = len(Archivos.abrir_jugadores()[1])
            print("\n", " "*6, "*** Opciones de Jugador ***")
            print("-"*42)
            print(Archivos.abrir_jugadores()[0])
            print(f"{indice_volver: <10} Volver")
            print("x          Salir")
            lista_jugadores = Archivos.abrir_jugadores()[2]
            opcion_elegida = input(
                "\nSeleccione la opción que desea realizar: ")
            if opcion_elegida in ["X", "x"]:
                print("\nHasta luego")
                etapa_elegir_jugador = False
                return
            elif opcion_elegida == str(indice_volver):
                etapa_elegir_jugador = False
                Casino.menu_inicio()
            elif opcion_elegida.isdigit():
                if int(opcion_elegida) < indice_volver:
                    etapa_elegir_jugador = False
                    jugador_elegido = lista_jugadores[int(opcion_elegida)]
                    if jugador_elegido[1] == "Bebedor":
                        jugador = Bebedor(jugador_elegido[0], jugador_elegido[1], jugador_elegido[2], jugador_elegido[3], jugador_elegido[4],
                                          jugador_elegido[5], jugador_elegido[6], jugador_elegido[7], jugador_elegido[8], jugador_elegido[9])
                        Casino.menu_principal(jugador)
                        etapa_elegir_jugador = False
                    elif jugador_elegido[1] == "Tacano":
                        jugador = Tacaño(jugador_elegido[0], jugador_elegido[1], jugador_elegido[2], jugador_elegido[3], jugador_elegido[4],
                                         jugador_elegido[5], jugador_elegido[6], jugador_elegido[7], jugador_elegido[8], jugador_elegido[9])
                        Casino.menu_principal(jugador)
                        etapa_elegir_jugador = False
                    elif jugador_elegido[1] == "Casual":
                        jugador = Casual(jugador_elegido[0], jugador_elegido[1], jugador_elegido[2], jugador_elegido[3], jugador_elegido[4],
                                         jugador_elegido[5], jugador_elegido[6], jugador_elegido[7], jugador_elegido[8], jugador_elegido[9])
                        Casino.menu_principal(jugador)
                        etapa_elegir_jugador = False
                    elif jugador_elegido[1] == "Ludopata":
                        jugador = Ludopata(jugador_elegido[0], jugador_elegido[1], jugador_elegido[2], jugador_elegido[3], jugador_elegido[4],
                                           jugador_elegido[5], jugador_elegido[6], jugador_elegido[7], jugador_elegido[8], jugador_elegido[9])
                        Casino.menu_principal(jugador)
                        etapa_elegir_jugador = False
                else:
                    print("\nOpción no valida, reintentalo nuevamente")
                    etapa_elegir_jugador = True
            else:
                print("\nOpción no valida, reintentalo nuevamente")
                etapa_elegir_jugador = True

    def menu_principal(jugador):
        etapa_menu_principal = True
        while etapa_menu_principal:
            print("\n   ***  Menú Principal ***")
            print("-"*29)
            print("\n [1]: Opciones de juegos \n [2]: Comprar bebestible "
                  "\n [3]: Habilidades jugador \n [4]: Ver Show"
                  "\n [0]: Volver \n [x]: Salir")
            opcion_elegida = input(
                "\nSeleccione la opción que desea realizar: ")
            if opcion_elegida == "1":
                etapa_1 = True
                while etapa_1:
                    juegos = Archivos.abrir_juegos()[0]
                    juegos_totales = Archivos.abrir_juegos()[1]
                    indice_volver = len(Archivos.abrir_juegos()[1])
                    print("\n   *** Opciones de Juegos ***")
                    print("-"*32)
                    print(Archivos.abrir_juegos()[0])
                    print(f" {indice_volver}        Volver"
                          "\n X        Salir")
                    opcion_elegida = input(
                        "\nSeleccione la opción que desea realizar: ")
                    juegos_totales = Archivos.abrir_juegos()[2]
                    Casino.verificar_estado_apuestas(jugador)
                    if opcion_elegida in ["0", "1", "2", "3", "4"]:
                        dinero_jugador = jugador.dinero
                        juego_elegido = juegos_totales[int(opcion_elegida)]
                        juego = Juego(
                            juego_elegido[0], juego_elegido[1], juego_elegido[2], juego_elegido[3])
                        print(
                            f"\nDebido al juego que escogiste, el dinero apostado debe ser entre {juego.apuesta_minima} y {juego.apuesta_maxima}")
                        print(
                            f"\nPosees {jugador.dinero}$ y te faltan {VALOR_DEUDA - jugador.dinero}$ para pagar tu dueda")
                        dinero_apostado = input(
                            "\nCuanto dinero desea apostar: ")
                        if dinero_apostado.isdigit():
                            if int(dinero_apostado) > dinero_jugador:
                                print("No posees tanto dinero")
                                etapa_1 = True
                            elif int(dinero_apostado) <= dinero_jugador and int(dinero_apostado) > 0:
                                if int(dinero_apostado) >= juego.apuesta_minima and int(dinero_apostado) <= juego.apuesta_maxima:
                                    print(
                                        "\nCumples los requisitos de apuesta del juego")
                                    jugador.juegos_jugados.append(juego.nombre)
                                    Casino.jugar(
                                        jugador, dinero_apostado, juego)
                                else:
                                    print(
                                        "El dinero apostado no pertenece a los rango de apuestas del juego")
                                    etapa_1 = True
                            elif int(dinero_apostado) <= 0:
                                print("Opción invalida")
                                Casino.menu_principal(jugador)
                        else:
                            print("Opción invalida")
                            Casino.menu_principal(jugador)
                    elif opcion_elegida in ["x", "X"]:
                        etapa_1 = False
                        return
                    elif opcion_elegida == str(indice_volver):
                        etapa_1 = False
                        Casino.menu_principal(jugador)
                    else:
                        print("Opción invalida, reintentalo")
                        etapa_1 = True
            elif opcion_elegida == "2":
                etapa_2 = True
                while etapa_2:
                    print("\n")
                    print("*** Bebestibles ***".center(45, " "))
                    print("-"*46)
                    print(Archivos.abrir_bebestibles()[0])
                    indice_volver = len(Archivos.abrir_bebestibles()[1])
                    jugos_totales = Archivos.abrir_bebestibles()[1]
                    print(f"{indice_volver}       Volver"
                          "\n X       Salir")
                    Casino.verificar_estado_bebestible(jugador)
                    opcion_elegida = input(
                        "\nSeleccione la opción que desea realizar: ")
                    if opcion_elegida.isdigit():
                        if int(opcion_elegida) < indice_volver:
                            jugo = jugos_totales[int(opcion_elegida)]
                            if jugo[1] == "Jugo":
                                jugo_actual = Jugo(
                                    jugo[0], jugo[1], int(jugo[2]))
                                if jugador.personalidad == "Bebedor":

                                    if jugador.cliente_recurrente(jugo_actual) == False:
                                        print("No posees suficiente dinero")
                                        etapa_2 = True
                                    else:
                                        Casino.menu_principal(jugador)
                                else:

                                    if jugador.comprar_bebestible(jugo_actual) == False:
                                        print("No posees suficiente dinero")
                                        etapa_2 = True
                                    else:
                                        Casino.menu_principal(jugador)
                            elif jugo[1] == "Gaseosa":
                                jugo_actual = Gaseosa(
                                    jugo[0], jugo[1], int(jugo[2]))
                                if jugador.personalidad == "Bebedor":

                                    if jugador.cliente_recurrente(jugo_actual) == False:
                                        print("No posees suficiente dinero")
                                        etapa_2 = True
                                    else:
                                        Casino.menu_principal(jugador)
                                else:

                                    if jugador.comprar_bebestible(jugo_actual) == False:
                                        print("No posees suficiente dinero")
                                        etapa_2 = True
                                    else:
                                        Casino.menu_principal(jugador)
                            elif jugo[1] == "Brebaje mágico":
                                jugo_actual = Brebaje_magico(
                                    jugo[0], jugo[1], int(jugo[2]))
                                if jugador.personalidad == "Bebedor":
                                    if jugador.cliente_recurrente(jugo_actual) == False:
                                        print("No posees suficiente dinero")
                                        etapa_2 = True
                                    else:
                                        Casino.menu_principal(jugador)
                                else:
                                    if jugador.comprar_bebestible(jugo_actual) == False:
                                        print("No posees suficiente dinero")
                                        etapa_2 = True
                                    else:
                                        Casino.menu_principal(jugador)
                        elif int(opcion_elegida) == indice_volver:
                            Casino.menu_principal(jugador)
                        else:
                            print("Opción no valida")
                            Casino.menu_principal(jugador)
                    elif opcion_elegida in ["x", "X"]:
                        etapa_2 = False
                        return
                    else:
                        print("Opción invalida, reintentalo")
                        etapa_2 = True
            elif opcion_elegida == "3":

                etapa_3 = True
                while etapa_3:
                    print("*** Ver estado del Jugador***".center(45, " "))
                    print("-"*45)
                    print(f"Nombre: {jugador.nombre}")
                    print(f"Personalidad: {jugador.personalidad}")
                    print(f"Energía: {jugador.energia}")
                    print(f"Suerte: {jugador.suerte}")
                    print(f"Dinero: {jugador.dinero}")
                    print(f"Frustración: {jugador.frustracion}")
                    print(f"Ego: {jugador.ego}")
                    print(f"Carisma: {jugador.carisma}")
                    print(f"Confianza: {jugador.confianza}")
                    print(f"Juego favorito: {jugador.juegos_favorito}")
                    print(f"Dinero falta: ${VALOR_DEUDA-jugador.dinero}")
                    print("[0] Volver")
                    print("[X] Salir")
                    opcion_elegida = input(
                        "\nSeleccione la opción que desea realizar: ")
                    if opcion_elegida == "0":
                        etapa_3 = False
                        Casino.menu_principal(jugador)
                    elif opcion_elegida in ["x", "X"]:
                        return
                    else:
                        print("Opción no valida, reintentalo")
                        etapa_3 = True
            elif opcion_elegida == "4":
                Casino.show(jugador)
            elif opcion_elegida == "0":
                Casino.menu_inicio()
            elif opcion_elegida in ["x", "X"]:
                print("\nHasta luego")
                etapa_menu_principal = False
                return

            else:
                print("\nOpción no valida, reintentalo nuevamente")
                etapa_menu_principal = True
