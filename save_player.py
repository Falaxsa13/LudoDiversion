import json


def save_player(name, email, date):
    """
    :param name: Nombre del jugador
    :param email: Correo del jugador
    :param date: Fecha de creacion de usuario
    :return string: mensaje con el estado del registro dependiendo de los datos de entrada
    """

    # Cargar datos existentes desde el archivo JSON
    with open('players.json', 'r') as file:
        data = json.load(file)

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
        "date": date,
        "wins": 0,
        "num_movements": 0,
        "last_num_movements": 0
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
    with open('players.json', 'r') as file:
        data = json.load(file)

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
    with open('players.json', 'r') as file:
        data = json.load(file)

    # Buscar jugador por correo electrónico
    for player in data:
        if player['email'] == email:
            return player

    return "Jugador no encontrado"

    # Ejemplo de uso
