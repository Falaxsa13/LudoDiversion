import drawing
import readchar


def infoJugadores():

    from main import clear_console

    name = email = date = ""
    i = j = k = 1
    confirm1 = confirm2 = False

    clear_console()
    print(drawing.infoPlayer)

    while True:

        key = readchar.readkey()

        if key == readchar.key.BACKSPACE:

            if not confirm1 and name != "":
                name = name[:-1]
                i -= 1
            elif not confirm2 and email != "":
                email = email[:-1]
                j -= 1
            elif date != "":
                date = date[:-1]
                k -= 1

        elif key != readchar.key.ENTER:

            if not confirm1:
                if len(name) <= 26:
                    name += key
                    i += 1
            elif not confirm2:
                if len(email) <= 35:
                    email += key
                    j += 1
            elif len(date) <= 6:

                date += key
                k += 1

        elif key == readchar.key.ENTER:

            if not confirm1:
                confirm1 = True
            elif not confirm2:
                confirm2 = True
            else:
                break

        print_infoJugadores(name, email, date, i, j, k)


def print_infoJugadores(name, email, date, i, j, k):

    from main import clear_console
    menu = drawing.infoPlayer

    clear_console()

    menu_lines = menu.split('\n')
    menu_lines[9] = menu_lines[9][:30] + " " + name + "  " + menu_lines[9][32 + i:]
    menu_lines[11] = menu_lines[11][:30] + " " + email + "  " + menu_lines[11][32 + j:]
    if date != "":

        if len(date) > 2:
            menu_lines[13] = menu_lines[13][:30] + " " + date[:2] + "/" + date[2:] + menu_lines[13][31 + k:]
        else:
            menu_lines[13] = menu_lines[13][:30] + " " + date + menu_lines[13][30 + k:]

    print('\n'.join(menu_lines))
