import readchar

import player_data
from Screens import player_vs_ia
from Screens import main_menu
from Screens import register_login
from Screens import info_player
from Screens import record

from drawing import clear_console, verify, register, infoplayer, instrucciones


def regresar_menu() -> None:
    """
    Returns to main menu
    """
    print("\nPresiona enter para salir al menu principal ")
    while True:
        key = readchar.readkey()
        if key == readchar.key.ENTER:
            main()


def instrucciones_menu() -> None:
    """
    Shows instructions
    """
    clear_console()
    print(instrucciones)


def main():
    """
    Main function that runs the game
    """
    # Saves selected option in main menu
    option = main_menu.main_menu()

    match option:
        case 1:  # "Empezar Juego" was selected
            # Saves Player data in data_menu
            ans, name, email, date = register_login.player_datamenu(verify)

            # Data verification
            if ans:
                while True:
                    # Saves IA game data
                    jugador_ganador, movements, last_movements = player_vs_ia.game_ai(name)

                    print(f"JUGADOR GANADOR: {jugador_ganador}")

                    # Player stats update if wins
                    if jugador_ganador == name:
                        player_data.update_stats(name, movements, date, last_movements)

                    print(f"Presiona ESPACIO para una revancha o ENTER para volver al menu principal")

                    # Waits confirmation for rematch/surrender
                    while True:
                        key = readchar.readkey()
                        if key == readchar.key.ENTER:
                            main()
                        elif key == readchar.key.SPACE:
                            break
            else:
                print("Nombre o Correo incorrectos\nVolviendo al menu principal...")

        case 2:  # "Registrar Jugador"
            save = register_login.player_datamenu(register)

            match save[0]:
                case 1:
                    print("El nombre de usuario ya ha sido registrado.")
                case 2:
                    print("El correo electronico ya ha sido registrado.")
                case 3:
                    print("El usuario ha sido registrado satisfactoriamente!")

        case 3: info_player.player_datamenu(infoplayer)  # "Info de Jugadores"

        case 4: record.record_menu()  # "Record"

        case 5: instrucciones_menu()  # "Instrucciones"

        case 6: return -1  # "Salir"

    regresar_menu()


if __name__ == '__main__':
    main()
