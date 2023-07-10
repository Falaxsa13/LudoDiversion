from random import randint
import time
from main import dice


def gameAI(player1, player2):

    from Screens import PlayerVSPlayer as Pvp
    pos1 = 0
    pos2 = 0
    p1Turn = True
    Pvp.print_PlayerVSPlayer(pos1, pos2, 7, p1Turn, player1, player2, 0)
    contador_movimientos = 0

    while True:

        if p1Turn:
            # Valor que tomara el dado
            move = dice(pos1, pos2, 7, p1Turn, player1, player2, 0)
        else:
            time.sleep(1.5)
            # Valor que tomara el dado IA, en este caso numero random del 1 al 6
            move = randint(1, 6)

        # Manejar bonuses y extensiones
        if p1Turn:
            pos1 += move

            contador_movimientos += 1

            if pos1 == 8 or pos1 == 14 or move == 6:
                print("BONUS")
            else:
                p1Turn = False
        else:
            pos2 += move

            if pos2 == 8 or pos2 == 14 or move == 6:
                print("BONUS")
            else:
                p1Turn = True

        reset = Pvp.print_PlayerVSPlayer(pos1, pos2, 7, p1Turn, player1, player2, move)

        # Posicion mayor a 20
        if pos1 > 20:
            pos1 = 40 - pos1
            reset = Pvp.print_PlayerVSPlayer(pos1, pos2, 7, p1Turn, player1, player2, move)

        # Posicion mayor a 20
        elif pos2 > 20:
            pos2 = 40 - pos2
            reset = Pvp.print_PlayerVSPlayer(pos1, pos2, 7, p1Turn, player1, player2, move)

        # Reseteo cuando el jugador 1 come
        if reset == -1:
            pos2 = 0
            Pvp.print_PlayerVSPlayer(pos1, pos2, 7, p1Turn, player1, player2, move)

        # Reseteo cuando el jugador 2 come
        elif reset == 1:
            pos1 = 0
            Pvp.print_PlayerVSPlayer(pos1, pos2, 7, p1Turn, player1, player2, move)

        # Sistema de victoria
        if pos1 == 20:
            return player1, contador_movimientos
        elif pos2 == 20:
            return player2, contador_movimientos