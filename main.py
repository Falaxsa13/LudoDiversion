import readchar

import player_data
from Screens import PlayerVSAi as PvA, MainMenu as Mn, register_login as rl, info_player as ip
from Screens import record
from drawing import clear_console
import drawing


# Funcion para regresar al menu principal
def regresar_menu():
    print("\nPresiona enter para salir al menu principal ")
    while True:
        key = readchar.readkey()
        if key == readchar.key.ENTER:
            main()


def instrucciones():

    clear_console()
    print(drawing.instrucciones)
    key = readchar.readkey()
    if key == readchar.key.ENTER:
        main()


def main():

    again = True
    option = Mn.main_menu()  # Guardar el valor de la opcion que seleccionaste en el menu principal
    match option:

        case 1:  # Se selecciono "Empezar Juego"

            name, email, date, ans = rl.player_datamenu(drawing.verify)  # Se verifica la cuenta del usuario

            if ans:  # Modo pendejo para saber si la validacion fue correcta

                while again:

                    jugador_ganador, movements, last_movements = PvA.game_ai(name, 'AI')

                    print(f"JUGADOR GANADOR: {jugador_ganador}")  # Se printea el nombre del jugador ganador

                    if jugador_ganador == name:
                        player_data.update_stats(name, movements, date, last_movements)

                    print(f"Presiona ESPACIO para una revancha o ENTER para volver al menu principal")

                    while True:
                        key = readchar.readkey()
                        if key == readchar.key.ENTER:
                            again = False
                            main()
                            break
                        elif key == readchar.key.SPACE:
                            break

            else:
                print("Nombre o Correo incorrectos\nVolviendo al menu principal...")
                regresar_menu()

        case 2: rl.player_datamenu(drawing.register)  # Registrar nuevo jugador

        case 3:
            ip.player_datamenu(drawing.infoplayer)  # Info de Jugadores
            regresar_menu()

        case 4: record.menu()  # Record de jugadores

        case 5: instrucciones()  # Instrucciones

        case 6: return -1  # Salir


if __name__ == '__main__':
    main()
