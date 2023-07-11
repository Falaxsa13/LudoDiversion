import readchar

import player_data
from Screens import PlayerVSAi as PvA, MainMenu as Mn, register_login, info_player as ip
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


# Instrucciones
def instrucciones():
    clear_console()
    print(drawing.instrucciones)


# Funcion principal que maneja el juego
def main():

    again = True

    # Guardar el valor de la opcion que seleccionaste en el menu principal
    option = Mn.main_menu()
    match option:

        case 1:  # Se selecciono "Empezar Juego"

            # Datos del jugador
            ans, name, email, date = register_login.player_datamenu(drawing.verify)

            if ans:  # Validacion de datos

                while again:  # Loop que nos permitira volver a jugar

                    # Juego contra IA, devolviendo datos del juego
                    jugador_ganador, movements, last_movements = PvA.game_ai(name, 'AI')

                    # Se imprime el nombre del jugador ganador
                    print(f"JUGADOR GANADOR: {jugador_ganador}")

                    # Actualizamos las estadisticas si el jugador salio victorioso
                    if jugador_ganador == name:
                        player_data.update_stats(name, movements, date, last_movements)

                    print(f"Presiona ESPACIO para una revancha o ENTER para volver al menu principal")

                    # Esperando confirmacion del input para tomar una accion definida arriba
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

        case 2:
            # Registrar nuevo jugador
            save = register_login.player_datamenu(drawing.register)

            match save[0]:
                case 1:
                    print("El nombre de usuario ya ha sido registrado.")
                case 2:
                    print("El correo electronico ya ha sido registrado.")
                case 3:
                    print("El usuario ha sido registrado satisfactoriamente!")

        case 3: ip.player_datamenu(drawing.infoplayer)  # Info de Jugadores

        case 4: record.menu()  # Record de jugadores

        case 5: instrucciones()  # Instrucciones

        case 6: return -1  # Salir

    regresar_menu()


if __name__ == '__main__':
    main()
