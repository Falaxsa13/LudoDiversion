import json

'''
The JSON file contains a list of player objects, where each player is represented by a dictionary with various fields. 
The fields include:
- "username": Represents the player's username.
- "email": Represents the player's email address.
- "date": Represents a list of unique victory dates in the format "mm/yyyy".
- "wins": Represents the number of wins the player has achieved.
- "num_movements": Represents the total number of movements made by the player.
- "last_num_movements": Represents the number of movements made by the player in the last game.
- "creation_date": Represents the date when the player's account was created.
'''


def read_players() -> list:
    """
    Reads player JSON
    """
    with open('players.json', 'r') as file:
        return json.load(file)


def save_player(name, email, date) -> int:
    """
    Saves a new player into the Json file.

    :param name: Player name
    :param email: Player email
    :param date: Player Creation date
    :return: Integer indicating the function status
            1: Username already exists
            2: Email has already been registered
            3: Successful Player Registration
    """

    # Load existing data from JSON file
    data = read_players()

    # Check if username or email already exist
    for player in data:
        if player["username"] == name:

            return 1  # Username already exists

        if player["email"] == email:

            return 2  # Email has already been registered

    # New Player Object ( Dictionary )
    new_player = {
        "username": name,
        "email": email,
        "date": [],
        "wins": 0,
        "num_movements": 0,
        "last_num_movements": "",
        "creation_date": date
    }

    # Add Object to data list
    data.append(new_player)

    # Write updated data to JSON
    with open('players.json', 'w') as file:
        json.dump(data, file, indent=4)

    # 3 = Successful Player Registration
    return 3


def verify_player(name: str, email: str) -> bool:
    """
    Verify if player exists by  by email and name
    :param name: Player Name
    :param email: Player Email
    :return Bool: Verification status
    """

    # Load existing data from JSON file
    data = read_players()

    # Verify if player exsits in data
    for player in data:
        if player['username'] == name and player["email"] == email:
            return True

    return False


def fetch_player(email: str) -> dict:
    """
    :param email: Email to verify
    :return Json: Player data
    """

    # Load existing data from JSON file
    data = read_players()

    # Search player by email
    for player in data:
        if player['email'] == email:
            return player

    return {}


def movement_sort() -> list:

    # Load existing data from JSON file
    data = read_players()

    # Sort the data by number of movements decreasingly
    sorted_data = sorted(data, key=lambda x: x['num_movements'], reverse=True)

    # Return the sorted data
    return sorted_data


def winners_by_month() -> dict:
    """
    :return Dic:
    key -> Meses del año
    Value -> Jugadores victoriosos en cada key ( Mes )
    """

    # Load existing data from JSON file
    data = read_players()

    # Initialize winners dictionary
    winners = {}

    # Iterate through the data and store the winners in the corresponding month inside the dictionary
    for player in data:
        for date in player['date']:

            # Separate the month of the victory date of player
            month = date[:2]

            # Initialize (key, value) dictionary
            if month not in winners:
                winners[month] = []

            # Add the player to the corresponding month
            winners[month].append(player['username'])

    return winners


def update_stats(player_name: str, movements: int, date: str, last_movements: str) -> None:
    """
    :param player_name: Player name to update
    :param movements: Movements made by the player during the game
    :param date: Victory date
    :param last_movements: String that contains the exact movements made by player in the last game
    :return:
    """

    # Load existing data from JSON file
    data = read_players()
    player_to_update = data[0]

    # Find player by name
    for player in data:
        if player['username'] == player_name:
            player_to_update = player
            break

    # Update player's statistics
    player_to_update['wins'] += 1
    player_to_update['num_movements'] += movements
    player_to_update['last_num_movements'] = last_movements

    # Add victory date if it doesn't already exist in the list
    if date not in player_to_update['date']:
        player_to_update['date'].append(date)

    # Overwrite the updated data to the JSON file
    with open('players.json', 'w') as file:
        json.dump(data, file, indent=4)




