from random import randint
from Screens import PlayerVSAi as PvA, ChooseName, ChooseName as Cn, MainMenu as Mn, PlayerVSPlayer as Pvp, \
    TypeGame as Tg, InfoJugadores as Ij
import csv
import drawing
import os
import readchar
import time


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def record():
    clear_console()
    print("Jugadores que han sido victorosos enfrentando al CPU: ")
    with open("Jugadores Victoriosos.csv", 'r') as archivo:
        reader = csv.reader(archivo)
        for row in reader:
            for palabra in row:
                print(palabra)
    print("Presiona enter para salir al menu principal ")
    while True:
        key = readchar.readkey()
        if key == readchar.key.ENTER:
            main()


def save_victory(name):

    with open("Jugadores Victoriosos.csv", 'a', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([name])


def dice(pos1, pos2, option, p1Turn, player1, player2, move):
    key = ""
    Pvp.print_PlayerVSPlayer(pos1, pos2, option, p1Turn, player1, player2, 0)
    while key != readchar.key.ENTER:

        key = readchar.readkey()
        if key == readchar.key.RIGHT:
            if option == 7:
                option = 36

            elif option == 36:
                option = 64
            else:
                option = 64
        elif key == readchar.key.LEFT:
            if option == 64:
                option = 36

            elif option == 36:
                option = 7

            else:
                option = 7

        Pvp.print_PlayerVSPlayer(pos1, pos2, option, p1Turn, player1, player2, move)

    if option == 7:
        move = randint(1, 6)
    elif option == 36:
        move = randint(1, 3)
    else:
        move = randint(4, 6)

    Pvp.print_PlayerVSPlayer(pos1, pos2, option, p1Turn, player1, player2, move)
    time.sleep(1)

    return move


def instrucciones():
    clear_console()
    menu = drawing.instrucciones
    print(menu)
    key = readchar.readkey()
    if key == readchar.key.ENTER:
        main()


def main():

    try:
        with open("Jugadores Victoriosos.csv", 'r'):
            pass
    except FileNotFoundError:
        with open("Jugadores Victoriosos.csv", 'w', newline=''):
            pass

    option = Mn.main_menu()  # Guardar el valor de la opcion que seleccionaste en el menu principal
    if option == 1:  # Se selecciono "Empezar Juego"

        nombre = ChooseName.chooseNameAI()  # Se consigue el nombre del jugador
        jugador_ganador, pasos = PvA.gameAI(nombre, 'AI')
        print(f"JUGADOR GANADOR: {jugador_ganador}")   # Se printea el nombre del jugador ganador
        if jugador_ganador == nombre:
            save_victory(nombre)
        print("\n\nPresiona enter para salir al menu principal ")
        while True:
            key = readchar.readkey()
            if key == readchar.key.ENTER:
                main()

    elif option == 2:  # Se selecciono "Instrucciones"
        instrucciones()

    elif option == 3:  # Se selecciono "Record"
        record()

    elif option == 4:
        Ij.infoJugadores()

    else:  # Se selecciono "Salir"
        clear_console()
        return -1


if __name__ == '__main__':
    main()


#El proyecto 2, consiste en realizar las siguientes modificaciones al juego Ludo diversion:
#• El programa solo tendra un tipo de juego, el cual es Jugador 1 vs. CPU.                   - [X]
#• El programa debe solicitar al jugador la siguiente informacion: ´                         - [ ]
#– El nombre del jugador
#– El correo electronico ´
#– La fecha en formato mm-yyyy
#los cuales deben ser validados por el programa. ´                                           - [ ]
#• El correo electronico es el identificador de los jugadores. ´
#• Durante el juego, los usuarios deben tener la opcion de empezar de nuevo o rendirse. ´
#• En la opcion´ Record: Se debe presentar dos opciones:
#– La opcion Lista de ganadores: donde se presenta a todos los usuarios ordenados, ´
#segun la cantidad de movimientos, en forma decreciente. ´
#– La opcion Ganadores del mes: donde se presenta por meses a los usuarios que ´
#ganaron el juego.
#• Se debe aumentar la opcion´ Info de Jugadores al menu principal, la cual nos solicita el
#correo electronico y proporciona: ´
#– La datos del jugador
#– Las veces que ha ganado
#– Los movimientos de su ultimo intento ´
#Ademas, se debe presentar una opci ´ on para descargar esta informaci ´ on en PDF. ´
#• El programa debe tener una base de datos de los jugadores. En cada ejecucion del ´
#codigo se debe cargar la base de de datos y actualizarla de ser el caso.

