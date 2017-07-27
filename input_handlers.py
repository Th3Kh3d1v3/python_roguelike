# Possible commands in the game
from game_states import GameStates

MoveUp = {'move': (0, -1)}
MoveDown = {'move': (0, 1)}
MoveLeft = {'move': (-1, 0)}
MoveRight = {'move': (1, 0)}
MoveUpLeft = {'move': (-1, -1)}
MoveUpRight = {'move': (1, -1)}
MoveDownLeft = {'move': (-1, 1)}
MoveDownRight = {'move': (1, 1)}
Pickup = {'pickup': True}
ShowInventory = {'show_inventory': True}
DropInventory = {'drop_inventory': True}

# Keybindings tied to commands.  Will eventually be able to be changed by user.
keybindings = {
    'UP': MoveUp,
    'DOWN': MoveDown,
    'LEFT': MoveLeft,
    'RIGHT': MoveRight,
    'h': MoveLeft,
    'j': MoveDown,
    'k': MoveUp,
    'l': MoveRight,
    'y': MoveUpLeft,
    'u': MoveUpRight,
    'b': MoveDownLeft,
    'n': MoveDownRight,
    'g': Pickup,
    'i': ShowInventory,
    'd': DropInventory
}


def handle_keys(user_input, game_state):
    if game_state == GameStates.PLAYERS_TURN:
        return handle_player_turn_keys(user_input)
    elif game_state == GameStates.PLAYER_DEAD:
        return handle_player_dead_keys(user_input)
    elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        return handle_inventory_keys(user_input)

    return {}


def handle_player_turn_keys(user_input):
    key_char = user_input.char

    if user_input.key in keybindings:
        return keybindings[user_input.key]
    elif key_char in keybindings:
        return keybindings[key_char]

    if user_input.key == 'ENTER' and user_input.alt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif user_input.key == 'ESCAPE':
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}


def handle_player_dead_keys(user_input):
    key_char = user_input.char

    if key_char == 'i':
        return ShowInventory

    if user_input.key == 'ENTER' and user_input.alt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif user_input.key == 'ESCAPE':
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}


def handle_inventory_keys(user_input):
    if not user_input.char:
        return {}

    index = ord(user_input.char) - ord('a')

    if index >= 0:
        return {'inventory_index': index}

    if user_input.key == 'ENTER' and user_input.alt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif user_input.key == 'ESCAPE':
        # Exit the game
        return {'exit': True}

    return {}
