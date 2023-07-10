import json


def read_players():

    with open('players.json', 'r') as file:
        return json.load(file)


def save_player(name, email, date):
    """
    :param name: Nombre del jugador
    :param email: Correo del jugador
    :param date: Fecha de creacion de usuario
    :return string: mensaje con el estado del registro dependiendo de los datos de entrada
    """

    # Cargar datos existentes desde el archivo JSON
    data = read_players()

    # Verificar si el nombre de usuario o el correo electrónico ya existen
    for player in data:
        if player["username"] == name:
            # 1 = Nombre de usuario ya existente
            return 1

        if player["email"] == email:
            # 2 = El correo electronico ya ha sido registrado
            return 2

    # Crear un nuevo player JSON con los argumentos proporcionados
    new_player = {
        "username": name,
        "email": email,
        "date": [],  # Lista que contiene fechas unicas de cada victoria (mm/yyyy)
        "wins": 0,
        "num_movements": 0,
        "last_num_movements": "",
        "creation_date": date
    }

    # Agregar el nuevo objeto a la lista de datos
    data.append(new_player)

    # Escribir los datos actualizados en el archivo JSON
    with open('players.json', 'w') as file:
        json.dump(data, file, indent=4)

    # 3 = Jugador registrado satisfactoriamente!
    return 3


def verify_player(name, email):
    """
    :param name: Nombre del jugador
    :param email: Correo del jugador
    :return Bool: True o False depediendo si el jugador fue verificado
    """

    # Cargar datos existentes desde el archivo JSON
    data = read_players()

    # Verificar si el nombre de usuario y correo electrónico existen en la base de datos
    for player in data:
        if player['username'] == name and player["email"] == email:
            return True

    return False


def fetch_player(email):
    """
    :param email: Correo a verificar
    :return Json: datos del jugador
    """

    # Cargar datos existentes desde el archivo JSON
    data = read_players()

    # Buscar jugador por correo electrónico
    for player in data:
        if player['email'] == email:
            return player

    return "Jugador no encontrado"


def movement_sort():

    # Cargar datos existentes desde el archivo JSON
    data = read_players()

    # Ordenar los datos por el número de movimientos en orden decreciente
    sorted_data = sorted(data, key=lambda x: x['num_movements'], reverse=True)

    # Retornar los datos ordenados
    return sorted_data


def winners_by_month():
    """
    :return Dic:
    key -> Meses del año
    Value -> Jugadores victoriosos en cada key ( Mes )
    """

    # Cargar datos existentes desde el archivo JSON
    data = read_players()

    # Inicializar la lista de ganadores por mes
    winners = {}

    # Recorrer los datos y almacenar los ganadores en el mes correspondiente
    for player in data:
        for date in player['date']:

            # Separar el mes de la fecha de la victoria del jugador
            month = date[:2]

            # Inicializar el key, value del diccionario
            if month not in winners:
                winners[month] = []

            # Añadir la fecha de la victoria del jugador al diccionario
            winners[month].append(player['username'])

    return winners


def update_stats(player_name, movements, date, last_movements):
    """
    :param player_name: Nombre del jugador para actualizar
    :param movements:  Movimientos realizados por el jugador durante el juego
    :param date: Fecha de la victoria
    :return:
    """

    # Cargar datos existentes desde el archivo JSON
    data = read_players()
    player_to_update = data[0]

    # Buscar jugador por nombre
    for player in data:
        if player['username'] == player_name:
            player_to_update = player
            break

    # Actualizar las estadisticas del jugador
    player_to_update['wins'] += 1
    player_to_update['num_movements'] += movements
    player_to_update['last_num_movements'] = last_movements

    # Añadir la fecha de victoria si aun no existe en la lista
    if date not in player_to_update['date']:

        player_to_update['date'].append(date)

    # Sobrescribir los datos actualizados en el archivo JSON
    with open('players.json', 'w') as file:
        json.dump(data, file, indent=4)
