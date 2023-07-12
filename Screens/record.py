import readchar
import drawing
from player_data import read_players, movement_sort, winners_by_month
import to_pdf


def record_menu() -> None:
    """
    Programming logic of the record menu
    """

    drawing.clear_console()

    # Current option
    selected_option = 1

    # confirmation 0: Doesn't show data
    # confirmation 1: Shows the sort by movement
    # confirmation 2: Shows the winners by month
    # confirmation 3: Export PDF
    confirmation = 0

    while True:

        print_record_menu(selected_option, confirmation)
        key = readchar.readkey()

        # UP arrow key
        if key == readchar.key.UP:
            selected_option = max(1, selected_option - 1)

        # DOWN arrow key
        elif key == readchar.key.DOWN:
            selected_option = min(3, selected_option + 1)

        # ENTER key
        elif key == readchar.key.ENTER:

            # Confirmation of selected option
            confirmation = selected_option

            # Prints selected option
            print_record_menu(selected_option, confirmation)

        # SPACE: return to main menu
        elif key == readchar.key.SPACE:
            return


def print_record_menu(selected_option: int, confirmation: int) -> None:
    """
    Prints the chosen option in the record menu
    :param selected_option: Current selected option before confirmation
    :param confirmation: Current option that is showing in the record menu
    """

    drawing.clear_console()
    menu = drawing.record

    menu_lines = menu.split('\n')
    menu_lines[selected_option + 7] = menu_lines[selected_option + 7][:35] + 'X' + menu_lines[selected_option + 7][36:]

    # row index for line printing
    row = 1

    # Movement sort
    if confirmation == 1:

        # List with player data
        players_data = movement_sort()

        for player in players_data:

            # Limit of player that screen is able to show
            if row > 12:
                break

            # Content of each line
            content = f"{row}. {player['username']} - {player['num_movements']} movimientos"
            menu_lines[row + 12] = menu_lines[row + 12][:17] + content + menu_lines[row + 12][17 + len(content):]

            row += 1

    # Winners by month
    elif confirmation == 2:

        # Dictionary containing montly winners
        winners_month = winners_by_month()

        # Priting in word format
        # Ex: dict = { "01: hans, guillermo } -> { "Enero": hans, guillermo }
        months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
                  "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

        for month, winners in winners_month.items():

            # String that contains the players who won in a month
            winners_string = ""

            # Iterating throught all players
            for player in winners:
                winners_string += f"{player} - "

            # Removing the last " - "
            winners_string = winners_string[:-3]

            # Final content to print
            content = f"En {months[int(month)-1]}: {winners_string}"

            # Length limit of content
            if len(content) > 65:
                # Printing "..." if exceeds limit
                menu_lines[row + 12] = menu_lines[row + 12][:17] + content[:65] + "..." + menu_lines[row + 12][17 + len(content[:68]):]
            else:
                menu_lines[row + 12] = menu_lines[row + 12][:17] + content + menu_lines[row + 12][17 + len(content):]

            row += 1

    # Exports in PDF format
    elif confirmation == 3:
        to_pdf.exportar_a_pdf(read_players(), movement_sort(), winners_by_month())

    print('\n'.join(menu_lines))
