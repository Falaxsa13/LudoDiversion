import readchar
import drawing


def print_ChooseNamePVP(key1, key2, i, j):
    from main import clear_console
    clear_console()

    menu = drawing.names

    menu_lines = menu.split('\n')

    menu_lines[10] = menu_lines[10][:11] + " " + key1 + "  " + menu_lines[10][13 + i:]
    menu_lines[13] = menu_lines[13][:11] + " " + key2 + "  " + menu_lines[13][13 + j:]

    print('\n'.join(menu_lines))


def chooseNamePVP():
    i = 1
    j = 1
    key1 = ""
    key2 = ""
    enter1 = False
    print_ChooseNamePVP(key1, key2, i, j)
    while True:
        key = readchar.readkey()
        if key == readchar.key.UP or key == readchar.key.DOWN or key == readchar.key.RIGHT or \
                key == readchar.key.LEFT or \
                (not enter1 and key1 == "" and key == readchar.key.BACKSPACE) or \
                (enter1 and key2 == "" and key == readchar.key.BACKSPACE):
            continue

        if key == readchar.key.ENTER and enter1:
            return key1, key2
        if key == readchar.key.ENTER:
            enter1 = True
            continue
        if enter1:
            if key == readchar.key.BACKSPACE:  # Tecla de borrar
                j -= 1
                key2 = key2[:-1]
            else:

                if len(key2) == 17:
                    key2 = key2
                else:
                    j += 1
                    key2 += key
        elif not enter1:
            if key == readchar.key.BACKSPACE:  # Tecla de borrar
                i -= 1
                key1 = key1[:-1]
            else:
                if len(key1) == 17:
                    key1 = key1
                else:
                    i += 1
                    key1 += key
        print_ChooseNamePVP(key1, key2, i, j)


def chooseNameAI():
    i = 1
    j = 3
    key1 = ""
    key2 = "IA"
    enter1 = False
    print_ChooseNamePVP(key1, key2, i, j)
    while True:
        key = readchar.readkey()
        if key == readchar.key.UP or key == readchar.key.DOWN or key == readchar.key.RIGHT or \
                key == readchar.key.LEFT or \
                (not enter1 and key1 == "" and key == readchar.key.BACKSPACE) or \
                (enter1 and key2 == "" and key == readchar.key.BACKSPACE):
            continue

        if key == readchar.key.BACKSPACE:  # Tecla de borrar
            i -= 1
            key1 = key1[:-1]
        elif key == readchar.key.ENTER:
            return key1
        else:
            if len(key1) == 17:
                key1 = key1
            else:
                i += 1
                key1 += key

        print_ChooseNamePVP(key1, key2, i, j)
