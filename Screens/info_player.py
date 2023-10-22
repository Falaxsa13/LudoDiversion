from player_data import fetch_playerF
import drawing
import readchar


def player_datamenu(menu: str) -> None:
    """
    Programming logic of the data menu that asks Email
    :param menu: String - Multiline string to print
    """

    # Initial variables
    email = domain = ""

    drawing.clear_console()
    print(menu)

    while True:

        key = readchar.readkey()

        # Backspace case
        if key == readchar.key.BACKSPACE:
            email = email[:-1]

        # Normal Type case
        elif key != readchar.key.ENTER and len(email) <= 20:

            # if "@" autocomplete with email domain
            if key == "@":
                domain = "@utec.edu.pe"
            else:
                email += key

        # Second Enter case ( confirm case )
        elif key == readchar.key.ENTER:

            # Search Player by Email
            player = fetch_player(f"{email}@utec.edu.pe")

            # If player not found
            if player is None:
                print("Jugador no encontrado")

            # Show data
            else:
                print_data(menu, player)
            break

        print_menu(menu, email, domain)


def print_menu(menu: str, email: str, domain: str) -> None:
    """
    Function that prints the current state of the info_player menu
    having arguments passed by the function "player_data_menu()"
    :param menu: Multiline string to print
    :param email: Current state of the email string
    :param domain: Current state of the domain of the email, changes from "" to "@utec.edu.pe" when "@" triggered.
    """

    drawing.clear_console()
    menu_lines = menu.split('\n')

    # Inserting email in screen
    if email != "":
        menu_lines[9] = f"{menu_lines[9][:30]} {email}{domain}{menu_lines[9][31 + len(email) + len(domain):]}"

    print('\n'.join(menu_lines))


def print_data(menu: str, player: dict) -> None:
    """
    :param menu: Multiline string to print
    :param player: Player JSON object extracted from players.json
    """

    drawing.clear_console()
    menu_lines = menu.split('\n')

    # Reading and saving player data
    name = player["username"]
    date = player["creation_date"]
    wins = str(player["wins"])
    num_movements = str(player["num_movements"])
    last_num_movements = str(player["last_num_movements"])

    # Inserting data in screen
    menu_lines[17] = f"{menu_lines[17][:30]} {name}{menu_lines[17][31+len(name):]}"
    menu_lines[18] = f"{menu_lines[18][:33]} {wins}{menu_lines[18][34 + len(wins):]}"
    menu_lines[19] = f"{menu_lines[19][:43]} {num_movements}{menu_lines[19][44 + len(num_movements):]}"
    menu_lines[20] = f"{menu_lines[20][:29]} {date[:2]}/{date[2:]}{menu_lines[20][31 + len(date):]}"
    menu_lines[22] = f"{menu_lines[22][:22]} {last_num_movements}{menu_lines[22][23 + len(last_num_movements):]}"

    # Priting the string menu
    print('\n'.join(menu_lines))
a