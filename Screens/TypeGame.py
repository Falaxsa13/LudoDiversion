import readchar
import drawing


def print_typegame(selected_option):

    drawing.clear_console()
    typescreen = drawing.choose_mode

    menu_lines = typescreen.split('\n')
    menu_lines[selected_option + 8] = menu_lines[selected_option + 8][:22] + '-> ' + menu_lines[selected_option + 8][25:]
    print('\n'.join(menu_lines))


def typegame_menu():

    selected_option = 1

    while True:
        print_typegame(selected_option)
        key = readchar.readkey()
        if key == readchar.key.UP:
            selected_option = max(1, selected_option - 6)
        elif key == readchar.key.DOWN:
            selected_option = min(6, selected_option + 6)
        elif key == readchar.key.ENTER:
            if selected_option == 1:
                return 1
            elif selected_option == 6:
                return 2
