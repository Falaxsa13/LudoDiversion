import readchar
from save_player import fetch_player


def player_datamenu(menu):
    from main import clear_console

    email = sup = ""
    i = 1
    clear_console()
    print(menu)

    while True:

        key = readchar.readkey()

        if key == readchar.key.BACKSPACE:

            email = email[:-1]
            i -= 1

        elif key != readchar.key.ENTER and len(email) <= 20:

            if key == "@":
                sup = "@utec.edu.pe"
            else:
                email += key
                i += 1

        elif key == readchar.key.ENTER:

            player = fetch_player(f"{email}@utec.edu.pe")

            if type(player) == str:
                print("Jugador no encontrado")
                break
            else:
                print_data(menu, player)
                email = ""
                return

        print_menu(menu, email, i, sup)


def print_menu(menu, email, i, sup):
    from main import clear_console

    clear_console()

    menu_lines = menu.split('\n')

    if email != "":
        menu_lines[9] = menu_lines[9][:30] + " " + email + sup + menu_lines[9][30 + len(sup) + i:]

    print('\n'.join(menu_lines))


def print_data(menu, player):
    from main import clear_console

    name = player["username"]
    date = player["date"]
    wins = str(player["wins"])
    num_movements = str(player["num_movements"])
    last_num_movements = str(player["last_num_movements"])

    clear_console()

    menu_lines = menu.split('\n')

    menu_lines[17] = menu_lines[17][:30] + " " + name + menu_lines[17][31+len(name):]
    menu_lines[18] = menu_lines[18][:33] + " " + wins + menu_lines[18][34 + len(wins):]
    menu_lines[19] = menu_lines[19][:43] + " " + num_movements + menu_lines[19][44 + len(num_movements):]
    menu_lines[20] = menu_lines[20][:43] + " " + last_num_movements + menu_lines[20][44 + len(last_num_movements):]
    menu_lines[21] = menu_lines[21][:29] + " " + f"{date[:2]}/{date[:2]}" + menu_lines[21][29 + len(date):]

    print('\n'.join(menu_lines))
