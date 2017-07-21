# Possible commands in the game
MoveUp = {'move': (0, -1)}
MoveDown = {'move': (0, 1)}
MoveLeft = {'move': (-1, 0)}
MoveRight = {'move': (1, 0)}
MoveUpLeft = {'move': (-1, -1)}
MoveUpRight = {'move': (1, -1)}
MoveDownLeft = {'move': (-1, 1)}
MoveDownRight = {'move': (1, 1)}

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
    'n': MoveDownRight
}


def handle_keys(user_input):
    """
    Checks if user input is in keybindings dictionary and returns bound command
    If not, checks if user input corresponds with commands below:

    Alt-Enter toggles full screen
    Escape exits the game
    """

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
