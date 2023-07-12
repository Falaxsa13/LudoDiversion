import readchar
import drawing


def main_menu() -> int:
    """
    Programming logic of the main menu
    """

    drawing.clear_console()
    selected_option = 1

    while True:

        print_menu(selected_option)
        key = readchar.readkey()

        # UP arrow key
        if key == readchar.key.UP:
            selected_option = max(1, selected_option - 1)

        # DOWN arrow key
        elif key == readchar.key.DOWN:
            selected_option = min(6, selected_option + 1)

        # ENTER key
        elif key == readchar.key.ENTER:
            return selected_option


def print_menu(selected_option: int) -> None:
    """
    Function that prints the current state of the main menu
    :param selected_option: Current option chosen by the player
    """

    drawing.clear_console()
    menu = drawing.main_menu

    # Inserting Arrow in screen
    menu_lines = menu.split('\n')
    menu_lines[selected_option + 9] = menu_lines[selected_option + 9][:32] + '-> ' + menu_lines[selected_option + 9][35:]
    print('\n'.join(menu_lines))
