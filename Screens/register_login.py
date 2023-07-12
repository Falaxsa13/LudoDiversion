import drawing
import readchar
from player_data import save_player, verify_player


def player_datamenu(menu: str) -> tuple:
    """
    Programming logic of the register/login menu that asks for name, email, and date
    :param menu: Multiline string menu
    :return tuple: Bool for successful verification, name, email, date (mm/yyyy)
    """

    # Starting variables
    name = email = dateMY = sup = ""
    confirm1 = confirm2 = False

    drawing.clear_console()
    print(menu)

    while True:

        key = readchar.readkey()

        # Backspace case
        if key == readchar.key.BACKSPACE:

            # When confirm1 is false -> Name delete
            if not confirm1 and name != "":
                name = name[:-1]

            # When confirm2 is false -> Email delete
            elif not confirm2 and email != "":
                email = email[:-1]

            # Last Date deleting
            elif dateMY != "":
                dateMY = dateMY[:-1]

        # Letter case
        elif key != readchar.key.ENTER:

            # When confirm1 is false -> Name insert
            if not confirm1 and len(name) <= 26:  # Length limit

                name += key

            # When confirm2 is false -> Email insert
            elif not confirm2 and len(email) <= 20:  # Length limit

                # if "@" autocomplete with email domain
                if key == "@":
                    sup = "@utec.edu.pe"

                else:
                    email += key

            # Last date insert
            elif len(dateMY) <= 5 and key.isdigit():
                dateMY += key

        # ENTER case
        elif key == readchar.key.ENTER:

            # confirm1 update
            if not confirm1:
                confirm1 = True

            # confirm2 update
            elif not confirm2:
                confirm2 = True
            else:

                if menu == drawing.register:

                    # Save 1: Username already exists
                    # Save 2: Email has already been registered
                    save = save_player(name, f"{email}@utec.edu.pe", dateMY)

                    return save, name, f"{email}@utec.edu.pe", dateMY

                elif menu == drawing.verify:

                    # ferify True: Verification succeed
                    # verify False: Verification failed
                    verify = verify_player(name, f"{email}@utec.edu.pe")

                    return verify, name, f"{email}@utec.edu.pe", dateMY

        print_datamenu(menu, name, email, dateMY, sup)


def print_datamenu(menu: str, name: str, email: str, date: str, domain: str) -> None:
    """
    Functions that shows the register/login menu
    :param menu: Multiline string menu
    :param name: Current Name state
    :param email: Current Email state
    :param date: Current date state
    :param domain: Current state of the domain of the email, changes from "" to "@utec.edu.pe" when "@" triggered.
    """

    drawing.clear_console()
    menu_lines = menu.split('\n')

    # Name insert
    menu_lines[9] = menu_lines[9][:30] + " " + name + "  " + menu_lines[9][33 + len(name):]

    # Email insert
    if email != "":
        menu_lines[11] = menu_lines[11][:30] + " " + email + domain + menu_lines[11][31 + len(email) + len(domain):]

    # Date insert
    if date != "":

        # Adding "/" before inserting years
        if len(date) > 2:
            menu_lines[13] = menu_lines[13][:31] + " " + date[:2] + "/" + date[2:] + menu_lines[13][33 + len(date):]
        else:
            menu_lines[13] = menu_lines[13][:31] + " " + date + menu_lines[13][32 + len(date):]

    # Reunify string
    print('\n'.join(menu_lines))
