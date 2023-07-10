import readchar
import drawing


def main_menu():

    drawing.clear_console()
    selected_option = 1

    while True:
        print_menu(selected_option)
        key = readchar.readkey()

        # Tecla flecha hacia arriba
        if key == readchar.key.UP:
            selected_option = max(1, selected_option - 1)

        # Tecla flecha hacia abajo
        elif key == readchar.key.DOWN:
            selected_option = min(6, selected_option + 1)

        # Tecla enter
        elif key == readchar.key.ENTER:

            return selected_option


def print_menu(selected_option):

    drawing.clear_console()
    menu = drawing.main_menu  # Pantalla Principal
    menu_lines = menu.split('\n')
    menu_lines[selected_option + 9] = menu_lines[selected_option + 9][:32] + '-> ' + menu_lines[selected_option + 9][35:]
    print('\n'.join(menu_lines))
