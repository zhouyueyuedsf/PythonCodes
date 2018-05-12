# VERSION 1.0.0

import json
import urllib.request

# Some useful constants
NORTH = 'n'
SOUTH = 's'
EAST = 'e'
WEST = 'w'

DIRECTIONS = [NORTH, SOUTH, EAST, WEST]

DEFAULT_PLAYER_NAME = "Ash"

DIRECTION_DELTAS = {
    NORTH: (-1, 0),
    EAST: (0, 1),
    SOUTH: (1, 0),
    WEST: (0, -1)
}

DIRECTION_WALL_DELTAS = {
    NORTH: (-0.5, 0),
    EAST: (0, 0.5),
    SOUTH: (0.5, 0),
    WEST: (0, -0.5)
}

GAME_OBJECT_FORMAT = "{} @ {}"
DEX_FORMAT = "{} Registered: {}\n{} Unregistered: {}"

# Errors
class DirectionError(Exception):
    pass

class DexError(Exception):
    pass

class UnexpectedPokemonError(DexError):
    pass

class InvalidPositionError(Exception):
    pass

class InvalidGameFile(Exception):
    pass

class InvalidGameData(Exception):
    pass

def is_position_valid(position, grid_size):
    """
    Returns True iff position is a valid position for a grid of grid_size.

    is_position_valid((num, num), (int, int)) -> bool
    """
    row, column = position
    rows, columns = grid_size

    return (0 <= row < rows and 0 <= column < columns)


def is_wall_position_valid(position, grid_size):
    """
    Returns True iff position is a valid wall position for a grid of grid_size.

    is_wall_position_valid((num, num), (int, int)) -> bool
    """
    row, column = position

    if not is_position_valid(position, grid_size):
        return False

    is_horizontal_wall = round(row % 1 - 0.5) == 0 and column % 1 == 0
    is_vertical_wall = round(column % 1 - 0.5) == 0 and row % 1 == 0

    # ^ is exclusive or, i.e. either a or b, but not both
    return is_horizontal_wall ^ is_vertical_wall

def is_cell_position_valid(position, grid_size):
    """
    Returns True iff position is a valid cell position for a grid of grid_size.

    is_cell_position_valid((num, num), (int, int)) -> bool
    """
    row, column = position

    if not is_position_valid(position, grid_size):
        return False

    return row % 1 == 0 and column % 1 == 0


def euclidean_distance(a, b):
    """
    Returns the Euclidean distance between two two-dimensional points.

    euclidean_distance((num, num), (num, num)) -> float
    """

    ax, ay = a
    bx, by = b

    return ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5


def parse_game_text(text):
    """
    Parses raw json string for game data into Python dictionary

    Raises:
        InvalidGameData: If game data is invalid.

    parse_game_text(str) -> dict{str: *}
    """
    try:
        data = json.loads(text)
    except json.decoder.JSONDecodeError as e:
        raise InvalidGameData(str(e))

    try:
        # transform relevant lists to tuples
        # not overly necessary, but more meaningful
        for level in data['levels']:
            for pokemon in level['pokemons']:
                pokemon['position'] = tuple(pokemon['position'])

            level['walls'] = [tuple(wall) for wall in level['walls']]

            level['player'] = tuple(level['player'])

        return data
    except Exception as e:
        raise InvalidGameData(str(e))

def load_game_file(game_file):
    """
    Loads game data from local file.

    Raises:
        InvalidGameFile: If filepath is invalid.
        InvalidGameData: If file does not have valid game data.

    load_game_file(str) -> dict
    """

    try:
        with open(game_file, 'r') as f:
            return parse_game_text(f.read())
    except FileNotFoundError as e:
        raise InvalidGameFile(str(e))



def load_game_url(game_url):
    """
    Loads game data from file via remote url.

    Raises:
        InvalidGameFile: If url is invalid.
        InvalidGameData: If file does not have valid game data.

    load_game_url(str) -> dict
    """

    try:
        with urllib.request.urlopen(game_url, 'r') as f:
            return parse_game_text(f.read())
    except FileNotFoundError as e:
        raise InvalidGameFile(str(e))
