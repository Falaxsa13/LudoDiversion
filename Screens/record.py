import readchar
import drawing
from player_data import read_players, movement_sort, winners_by_month
import to_pdf


def menu():
    drawing.clear_console()

    selected_option = 1

    # La confirmacion se inicializa como 0, indicando que aun no imprimamos los datos
    confirmation = 0

    while True:
        print_menu(selected_option, confirmation)
        key = readchar.readkey()

        # Tecla flecha hacia arriba
        if key == readchar.key.UP:
            selected_option = max(1, selected_option - 1)

        # Tecla flecha hacia abajo
        elif key == readchar.key.DOWN:
            selected_option = min(3, selected_option + 1)

        # Tecla enter
        elif key == readchar.key.ENTER:

            # Confirmamos la opcion seleccionada
            confirmation = selected_option

            # Mandamos a imprimir la opcion seleccionada
            print_menu(selected_option, confirmation)


def print_menu(selected_option, confirmation):
    record_menu = drawing.record

    drawing.clear_console()

    menu_lines = record_menu.split('\n')

    menu_lines[selected_option + 7] = menu_lines[selected_option + 7][:35] + 'X' + menu_lines[selected_option + 7][36:]

    row = 1

    if confirmation == 1:

        players_data = movement_sort()

        for player in players_data:

            if row > 12:
                break

            content = f"{row}. {player['username']} - {player['num_movements']} movimientos"
            menu_lines[row + 12] = menu_lines[row + 12][:17] + content + menu_lines[row + 12][17 + len(content):]

            row += 1

    elif confirmation == 2:

        winners_month = winners_by_month()

        months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
                  "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

        for month, winners in winners_month.items():

            winners_string = ""
            for player in winners:
                winners_string += f"{player} - "
            winners_string = winners_string[:-3]

            content = f"En {months[int(month)-1]}: {winners_string}"

            if len(content) > 65:
                menu_lines[row + 12] = menu_lines[row + 12][:17] + content[:65] + "..." + menu_lines[row + 12][17 + len(content[:68]):]
            else:
                menu_lines[row + 12] = menu_lines[row + 12][:17] + content + menu_lines[row + 12][17 + len(content):]

            row += 1

    elif confirmation == 3:
        to_pdf.exportar_a_pdf(read_players(), movement_sort() ,winners_by_month())

    print('\n'.join(menu_lines))
