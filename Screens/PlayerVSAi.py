from random import randint
import time
import drawing
import readchar


def dice(pos1, pos2, option, p1_turn, player1, player2, move):
    key = ""
    print_player_vs_player(pos1, pos2, option, p1_turn, player1, player2, 0)
    while key != readchar.key.ENTER:

        key = readchar.readkey()

        if key == readchar.key.RIGHT:

            match option:
                case 7:
                    option = 36
                case 36:
                    option = 64

        elif key == readchar.key.LEFT:

            match option:
                case 64:
                    option = 36
                case 36:
                    option = 7

        print_player_vs_player(pos1, pos2, option, p1_turn, player1, player2, move)

    if option == 7:
        move = randint(1, 6)
    elif option == 36:
        move = randint(1, 3)
    else:
        move = randint(4, 6)

    print_player_vs_player(pos1, pos2, option, p1_turn, player1, player2, move)
    time.sleep(1)

    return move


def print_player_vs_player(pos1, pos2, option, p1_turn, name1, name2, move):

    drawing.clear_console()
    reset = 0
    gamescreen = drawing.gamescreen
    menu_lines = gamescreen.split('\n')

    # Escribir el texto de informacion
    if option == 7:
        choice = "NORMAL"
    elif option == 36:
        choice = "DEBIL"
    else:
        choice = "FUERTE"

    # Tabla de informacion de las zonas exteriores
    if p1_turn:

        menu_lines[7] = menu_lines[7][:4] + "TURNO DEL JUGADOR:" + menu_lines[7][22:]
        menu_lines[8] = menu_lines[8][:4] + name1 + menu_lines[8][4 + len(name1):]

        menu_lines[13] = menu_lines[13][:4] + "DADO ELEGIDO:" + menu_lines[13][17:]
        menu_lines[14] = menu_lines[14][:4] + choice + menu_lines[14][4 + len(choice):]

        menu_lines[19] = menu_lines[19][:4] + "POSICION:" + menu_lines[19][4+len("POSICION:"):]
        menu_lines[20] = menu_lines[20][:4] + f"(+{move})->[{pos1}]" + menu_lines[20][4 + len(f"(+{move})->[{pos1}]"):]

    else:

        menu_lines[7] = menu_lines[7][:67] + "TURNO DEL JUGADOR:" + menu_lines[7][68+len("TURNO DEL JUGADOR"):]
        menu_lines[8] = menu_lines[8][:67] + name2 + menu_lines[8][67 + len(name2):]

        menu_lines[13] = menu_lines[13][:67] + "DADO ELEGIDO:" + menu_lines[13][67+len("DADO ELEGIDO:"):]
        menu_lines[14] = menu_lines[14][:67] + choice + menu_lines[14][67 + len(choice):]

        menu_lines[19] = menu_lines[19][:67] + "POSICION:" + menu_lines[19][67+len("POSICION:"):]
        menu_lines[20] = menu_lines[20][:67] + f"(+{move})->[{pos2}]" + menu_lines[20][67 + len(f"(+{move})->[{pos1}]"):]

    # Cursor del dado
    menu_lines[26] = menu_lines[26][:option] + '-> ' + menu_lines[26][3 + option:]

    # Movimiento de las fichas
    if pos1 == pos2:  # Cuando caen en la misma casilla
        menu_lines[23 - pos1] = menu_lines[23 - pos1][:33] + "O" + \
                                menu_lines[23 - pos1][34:55] + "X" + menu_lines[23 - pos1][56:]

        # El Jugador 1 comio al Jugador 2
        if not p1_turn and pos2 != 0:
            for i in range(pos2, -1, -1):
                if i >= 0:
                    menu_lines[23 - i] = menu_lines[23 - i][:55] + "X" + menu_lines[23 - i][56:]
                    print('\n'.join(menu_lines))
                    time.sleep(0.2)
                    menu_lines[23 - i] = menu_lines[23 - i][:55] + "-" + menu_lines[23 - i][56:]
                    drawing.clear_console()
                else:
                    break
            reset = -1

        # El jugador 2 comio al jugador 1
        elif p1_turn and pos1 != 0:
            for i in range(pos1, -1, -1):
                if i >= 0:
                    menu_lines[23 - i] = menu_lines[23 - i][:33] + "O" + menu_lines[23 - i][34:]
                    print('\n'.join(menu_lines))
                    time.sleep(0.2)
                    menu_lines[23 - i] = menu_lines[23 - i][:33] + "-" + menu_lines[23 - i][34:]
                    drawing.clear_console()
                else:
                    break
            reset = 1

    elif pos1 != pos2:  # Cuando estan en distintas casillas
        menu_lines[23 - pos1] = menu_lines[23 - pos1][:33] + "O" + menu_lines[23 - pos1][34:]
        menu_lines[23 - pos2] = menu_lines[23 - pos2][:55] + "X" + menu_lines[23 - pos2][56:]

    # Animacion para casillas mayores a 20
    if pos1 > 20:
        pos1c = 3
        menu_lines[pos1c] = menu_lines[pos1c][:33] + "O" + menu_lines[pos1c][34:]
        for i in range(pos1c, 4 + (pos1 % 20)):
            menu_lines[i] = menu_lines[i][:33] + "O" + menu_lines[i][34:]
            print('\n'.join(menu_lines))
            time.sleep(0.3)
            menu_lines[i] = menu_lines[i][:33] + "-" + menu_lines[i][34:]
            drawing.clear_console()

    elif pos2 > 20:
        pos2c = 3
        menu_lines[pos2c] = menu_lines[pos2c][:55] + "X" + menu_lines[pos2c][56:]
        for i in range(pos2c, 4 + (pos2 % 20)):
            menu_lines[i] = menu_lines[i][:55] + "X" + menu_lines[i][56:]
            print('\n'.join(menu_lines))
            time.sleep(0.3)
            menu_lines[i] = menu_lines[i][:55] + "-" + menu_lines[i][56:]
            drawing.clear_console()

    print('\n'.join(menu_lines))
    return reset


def game_ai(player1, player2):

    current_movements = ""
    pos1 = 0
    pos2 = 0
    p1Turn = True
    print_player_vs_player(pos1, pos2, 7, p1Turn, player1, player2, 0)
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

            current_movements += f"{move}-"
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

        reset = print_player_vs_player(pos1, pos2, 7, p1Turn, player1, player2, move)

        # Posicion mayor a 20
        if pos1 > 20:
            pos1 = 40 - pos1
            reset = print_player_vs_player(pos1, pos2, 7, p1Turn, player1, player2, move)

        # Posicion mayor a 20
        elif pos2 > 20:
            pos2 = 40 - pos2
            reset = print_player_vs_player(pos1, pos2, 7, p1Turn, player1, player2, move)

        # Reseteo cuando el jugador 1 come
        if reset == -1:
            pos2 = 0
            print_player_vs_player(pos1, pos2, 7, p1Turn, player1, player2, move)

        # Reseteo cuando el jugador 2 come
        elif reset == 1:
            pos1 = 0
            print_player_vs_player(pos1, pos2, 7, p1Turn, player1, player2, move)

        # Sistema de victoria
        if pos1 == 20:
            return player1, contador_movimientos, current_movements[:-1]
        elif pos2 == 20:
            return player2, contador_movimientos, current_movements[:-1]
