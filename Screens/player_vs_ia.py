from random import randint
import time
import drawing
import readchar


def dice(pos1: int, pos2: int, selected_option: int, p1_turn: bool, player_name: str, move) -> int:
    """
    Dice function: Logic of the dice move while chaning the game menu during the Dice period
    :param pos1: Current Position of player 1 (Necesary for printing menu)
    :param pos2: Current Position of player 2 (Necesary for printing menu)
    :param selected_option: Current selected option for Dice (Weak, Normal Strong)
    :param p1_turn: Boolean that indicates if it's player's turn
    :param player_name: Player Name
    :param move: Current move got by dice Ex: (1-6)
    :return: new move
    """

    # Current pressed key
    key = ""

    print_game_ai(pos1, pos2, selected_option, p1_turn, player_name, 0)

    while key != readchar.key.ENTER:

        key = readchar.readkey()

        # Going right until row 64
        if key == readchar.key.RIGHT:

            match selected_option:
                case 7:
                    selected_option = 36
                case 36:
                    selected_option = 64

        # Going left until row 7
        elif key == readchar.key.LEFT:

            match selected_option:
                case 64:
                    selected_option = 36
                case 36:
                    selected_option = 7

        print_game_ai(pos1, pos2, selected_option, p1_turn, player_name, move)

    if selected_option == 7:  # Normal Dice
        move = randint(1, 6)
    elif selected_option == 36:  # Weak Dice
        move = randint(1, 3)
    else:  # Strong Dice
        move = randint(4, 6)

    print_game_ai(pos1, pos2, selected_option, p1_turn, player_name, move)

    time.sleep(1)

    # Final Dice value
    return move


def print_game_ai(pos1: int, pos2: int, selected_option: int, p1_turn: bool, player_name: str, move: int) -> int:
    """
    Function that prints the current state of the game
    :param pos1: Current Position of player 1 (Necesary for printing menu)
    :param pos2: Current Position of player 2 (Necesary for printing menu)
    :param selected_option: Current selected option for Dice (Weak, Normal Strong)
    :param p1_turn: Boolean that indicates if it's player's turn
    :param player_name: Player Name
    :param move: Current move got by dice Ex: (1-6)
    :return reset: Integer that determines if a position has to be reseted
    """

    drawing.clear_console()

    # reset 0: No reset
    # reset 1: Player 1 position reset
    # reset -1: Player 2 position reset
    reset = 0

    gamescreen = drawing.gamescreen
    menu_lines = gamescreen.split('\n')

    # Choice text
    if selected_option == 7:
        choice = "NORMAL"
    elif selected_option == 36:
        choice = "DEBIL"
    else:
        choice = "FUERTE"

    # In-game information
    # Left screen side
    if p1_turn:

        menu_lines[7] = menu_lines[7][:4] + "TURNO DEL JUGADOR:" + menu_lines[7][22:]
        menu_lines[8] = menu_lines[8][:4] + player_name + menu_lines[8][4 + len(player_name):]

        menu_lines[13] = menu_lines[13][:4] + "DADO ELEGIDO:" + menu_lines[13][17:]
        menu_lines[14] = menu_lines[14][:4] + choice + menu_lines[14][4 + len(choice):]

        menu_lines[19] = menu_lines[19][:4] + "POSICION:" + menu_lines[19][4+len("POSICION:"):]
        menu_lines[20] = menu_lines[20][:4] + f"(+{move})->[{pos1}]" + menu_lines[20][4 + len(f"(+{move})->[{pos1}]"):]

    # Right screen side
    else:

        menu_lines[7] = menu_lines[7][:67] + "TURNO DEL JUGADOR:" + menu_lines[7][68+len("TURNO DEL JUGADOR"):]
        menu_lines[8] = menu_lines[8][:67] + "IA" + menu_lines[8][69:]

        menu_lines[13] = menu_lines[13][:67] + "DADO ELEGIDO:" + menu_lines[13][67+len("DADO ELEGIDO:"):]
        menu_lines[14] = menu_lines[14][:67] + choice + menu_lines[14][67 + len(choice):]

        menu_lines[19] = menu_lines[19][:67] + "POSICION:" + menu_lines[19][67+len("POSICION:"):]
        menu_lines[20] = menu_lines[20][:67] + f"(+{move})->[{pos2}]" + menu_lines[20][67 + len(f"(+{move})->[{pos1}]"):]

    # Dice selection arrow
    menu_lines[26] = menu_lines[26][:selected_option] + '-> ' + menu_lines[26][3 + selected_option:]

    # --- Pieces Movement ---
    # Pieces in the same position
    if pos1 == pos2:
        menu_lines[23 - pos1] = menu_lines[23 - pos1][:33] + "O" + \
                                menu_lines[23 - pos1][34:55] + "X" + menu_lines[23 - pos1][56:]

        # Player 1 kills Player 2
        if not p1_turn and pos2 != 0:

            # Animation of position reset made by loops
            for i in range(pos2, -1, -1):

                if i >= 0:
                    menu_lines[23 - i] = menu_lines[23 - i][:55] + "X" + menu_lines[23 - i][56:]
                    print('\n'.join(menu_lines))
                    time.sleep(0.2)
                    menu_lines[23 - i] = menu_lines[23 - i][:55] + "-" + menu_lines[23 - i][56:]
                    drawing.clear_console()
                else:
                    break
            # Reset of position
            reset = -1

        # Player 2 kills Player 1
        elif p1_turn and pos1 != 0:

            # Animation of position reset made by loops
            for i in range(pos1, -1, -1):

                if i >= 0:
                    menu_lines[23 - i] = menu_lines[23 - i][:33] + "O" + menu_lines[23 - i][34:]
                    print('\n'.join(menu_lines))
                    time.sleep(0.2)
                    menu_lines[23 - i] = menu_lines[23 - i][:33] + "-" + menu_lines[23 - i][34:]
                    drawing.clear_console()
                else:
                    break
            # Reset of position
            reset = 1

    # Different positions
    elif pos1 != pos2:
        menu_lines[23 - pos1] = menu_lines[23 - pos1][:33] + "O" + menu_lines[23 - pos1][34:]
        menu_lines[23 - pos2] = menu_lines[23 - pos2][:55] + "X" + menu_lines[23 - pos2][56:]

    # Animation of player 1 move if exceeds position 20
    if pos1 > 20:
        pos1c = 3
        menu_lines[pos1c] = menu_lines[pos1c][:33] + "O" + menu_lines[pos1c][34:]
        for i in range(pos1c, 4 + (pos1 % 20)):
            menu_lines[i] = menu_lines[i][:33] + "O" + menu_lines[i][34:]
            print('\n'.join(menu_lines))
            time.sleep(0.3)
            menu_lines[i] = menu_lines[i][:33] + "-" + menu_lines[i][34:]
            drawing.clear_console()

    # Animation of player 2 move if exceeds position 20
    elif pos2 > 20:
        pos2c = 3
        menu_lines[pos2c] = menu_lines[pos2c][:55] + "X" + menu_lines[pos2c][56:]
        for i in range(pos2c, 4 + (pos2 % 20)):
            menu_lines[i] = menu_lines[i][:55] + "X" + menu_lines[i][56:]
            print('\n'.join(menu_lines))
            time.sleep(0.3)
            menu_lines[i] = menu_lines[i][:55] + "-" + menu_lines[i][56:]
            drawing.clear_console()

    # Reunify the string
    print('\n'.join(menu_lines))

    # Return the reset status (-1, 0, 1)
    return reset


def game_ai(player_name: str) -> tuple:
    """
    Function that handles the logic of the game
    :param player_name: Player name
    :return: (winner name, number of movements, movements)
    """

    # String for movements Ex: 5-6-2-1-3
    current_movements = ""

    # Position of player 1 and 2
    pos1 = pos2 = 0

    # Player turn
    p1Turn = True

    # Print initial state of game
    print_game_ai(pos1, pos2, 7, p1Turn, player_name, 0)

    movement_counter = 0

    while True:

        # Player turn
        if p1Turn:

            # Player Dice value
            move = dice(pos1, pos2, 7, p1Turn, player_name, 0)

            # Move Update & Log
            pos1 += move
            current_movements += f"{move}-"
            movement_counter += 1

            # Check bonuses ( Doesn't change turn )
            if pos1 == 8 or pos1 == 14 or move == 6:
                print("BONUS")
            else:
                # Change turn
                p1Turn = False

        # AI turn
        else:

            # AI Dice value
            move = randint(1, 6)
            time.sleep(1.5)

            # Update position
            pos2 += move

            # Check bonuses ( Doesn't change turn )
            if pos2 == 8 or pos2 == 14 or move == 6:
                print("BONUS")
            else:
                # Change turn
                p1Turn = True

        # Updates game screen with new arguments and saves reset value
        reset = print_game_ai(pos1, pos2, 7, p1Turn, player_name, move)

        # Position higher than 20 for player 1
        if pos1 > 20:
            # Position reset Ex: 22 -> 18
            pos1 = 40 - pos1
            reset = print_game_ai(pos1, pos2, 7, p1Turn, player_name, move)

        # Position higher than 20 for player 2
        elif pos2 > 20:
            pos2 = 40 - pos2
            reset = print_game_ai(pos1, pos2, 7, p1Turn, player_name, move)

        # Reset if Player 1 kills AI
        if reset == -1:
            pos2 = 0
            print_game_ai(pos1, pos2, 7, p1Turn, player_name, move)

        # Reset if IA kills Player 1
        elif reset == 1:
            pos1 = 0
            print_game_ai(pos1, pos2, 7, p1Turn, player_name, move)

        # Victory
        if pos1 == 20:
            return player_name, movement_counter, current_movements[:-1]

        elif pos2 == 20:
            return "IA", movement_counter, current_movements[:-1]
