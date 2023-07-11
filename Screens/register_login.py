import drawing
import readchar
from player_data import save_player, verify_player


def player_datamenu(menu):
    name = email = dateMY = sup = ""
    i = j = k = 1
    confirm1 = confirm2 = False
    drawing.clear_console()
    print(menu)

    while True:

        key = readchar.readkey()

        if key == readchar.key.BACKSPACE:

            if not confirm1 and name != "":
                name = name[:-1]
                i -= 1
            elif not confirm2 and email != "":
                email = email[:-1]
                j -= 1
            elif dateMY != "":
                dateMY = dateMY[:-1]
                k -= 1

        elif key != readchar.key.ENTER:

            if not confirm1:
                if len(name) <= 26:
                    name += key
                    i += 1
            elif not confirm2 and len(email) <= 20:

                if key == "@":
                    sup = "@utec.edu.pe"
                else:
                    email += key
                    j += 1
            elif len(dateMY) <= 5 and key.isdigit():

                dateMY += key
                k += 1

        elif key == readchar.key.ENTER:

            if not confirm1:
                confirm1 = True
            elif not confirm2:
                confirm2 = True
            else:
                if menu == drawing.register:

                    save = save_player(name, f"{email}@utec.edu.pe", dateMY)

                    return save, name, f"{email}@utec.edu.pe", dateMY

                elif menu == drawing.verify:

                    verify = verify_player(name, f"{email}@utec.edu.pe")

                    return verify, name, f"{email}@utec.edu.pe", dateMY

        print_datamenu(menu, name, email, dateMY, i, j, k, sup)


def print_datamenu(menu, name, email, date, i, j, k, sup):
    drawing.clear_console()

    menu_lines = menu.split('\n')
    menu_lines[9] = menu_lines[9][:30] + " " + name + "  " + menu_lines[9][32 + i:]

    if email != "":
        menu_lines[11] = menu_lines[11][:30] + " " + email + sup + menu_lines[11][30 + len(sup) + j:]

    if date != "":

        if len(date) > 2:
            menu_lines[13] = menu_lines[13][:31] + " " + date[:2] + "/" + date[2:] + menu_lines[13][32 + k:]
        else:
            menu_lines[13] = menu_lines[13][:31] + " " + date + menu_lines[13][31 + k:]

    print('\n'.join(menu_lines))
