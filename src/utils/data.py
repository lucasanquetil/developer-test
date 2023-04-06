import os
import sqlite3
import json
from src.model.empire import Empire
from src.model.millennium_falcon import MillenniumFalcon
import sys


def get_routes(filepath: str) -> list:
    """
    Reads an SQLite database containing the number of days required to travel from departure planet to arrival planet.
    :param filepath: Path toward the .db dataset containing a ROUTES table.
    :return route_table: A list of triplets (departure, arrival, days) containing all the possible planet trips possible
            and their time consumption.
    """
    assert isinstance(filepath, str), "data.py: get_routes: filepath should be an string"

    connection = None
    cursor = None
    route_table = None
    try:
        connection = sqlite3.connect(filepath)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ROUTES")
        route_table = cursor.fetchall()
        cursor.close()
        connection.close()
    except Exception as e:
        print(e)
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return route_table


def open_json_file(filepath: str):
    assert isinstance(filepath, str), "data.py: open_json_file: filepath should be an string"
    assert filepath.endswith('.json'), "data.py: open_json_file: filepath should lead to a JSON file"
    assert os.path.isfile(filepath), "data.py: open_json_file: filepath should lead to an existing file"

    file = open(filepath)
    raw_data = json.load(file)
    file.close()
    return raw_data


def build_millenium_falcon(filepath: str) -> MillenniumFalcon:
    """
    Reads a JSON file containing information on the Millennium Falcon.
    :param filepath: Path toward the .json file containing Millennium Falcon's information.
    :return millenium_falcon: A MillenniumFalcon object, see utils.classes for more details.
    """
    assert isinstance(filepath, str), "data.py: build_millenium_falcon: filepath should be an string"

    try:
        file = open(filepath)
        raw_data = json.load(file)
        file.close()
        autonomy = raw_data['autonomy']
        departure = raw_data['departure']
        arrival = raw_data['arrival']
        route_database = raw_data['routes_db']

        if os.path.isfile(os.getcwd() + route_database):
            routes = get_routes(os.getcwd() + route_database)

        elif os.path.isfile(filepath[:-22] + route_database):
            routes = get_routes(filepath[:-22] + route_database)

        else:
            sys.stderr.write('Error data.py: build_millenium_falcon: Impossible to read the database routes\n')
            sys.exit()

        millenium_falcon = MillenniumFalcon(autonomy, departure, arrival, routes)
    except Exception as e:
        print(e)
        sys.stderr.write('Error data.py: build_millenium_falcon: impossible to build Millennium Falcon object\n')
        sys.exit()
    return millenium_falcon


def build_empire(raw_data) -> Empire:
    """
    Reads a JSON file containing information on the Millennium Falcon.
    :param raw_data: JSON file already open containing Millennium Falcon's information.
    :return: empire: an Empire object, see utils.classes for more details.
    """
    try:
        countdown = raw_data['countdown']
        bounty_hunters = raw_data['bounty_hunters']
        empire = Empire(countdown, bounty_hunters)
    except Exception as e:
        print(e)
        sys.stderr.write('Error data.py: build_empire: : Could not build Empire object\n')
        sys.exit()
    return empire
