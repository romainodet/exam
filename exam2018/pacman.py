###
### Author : Antoine Scherrer <antoine.scherrer@lecole-ldlc.com>
### License : GPL
###

# The game map, as a large string
# Be careful not to include useless spaces on the right when you modify the map !
game_map = """
##########
.C ..oX .#
#.## #. .#
#.##.#.  #
#. . .X .#
# . .  . .
##########
"""

# Definition of each component of the map
PACMAN = 'C'
ENNEMY = 'X'
WALL = '#'
SUPERGUM = 'o'
GUM = '.'
EMPTY = ' '

# Compute width and height of the map
width = len(game_map.split('\n')[1])
# we need to subtract 2 because of the newline at beginning and the newline at the end of the string
height = len(game_map.split('\n')) - 2

# Generate a red colored text
def red_text(txt):
    return '\033[31;1m' + txt + '\033[0m'


# Generate a green colored text
def green_text(txt):
    return '\033[32;1m' + txt + '\033[0m'


# Generate a blue colored text
def blue_text(txt):
    return '\033[34;1m' + txt + '\033[0m'


# Generate a pink colored text
def pink_text(txt):
    return '\033[35;1m' + txt + '\033[0m'


# Generate a debug text. Use this to show debug messages,
# you can consider the player won't see these messages
def debug_text(txt):
    return '\033[37m' + '[DEBUG]' + txt + '\033[0m'


# get the index of a position in the game_map string
def get_map_index(position):
    # We need to compute the index of that char in the string.
    # We need to add 1 to the width because the the "new line" characters
    return 1 + position[0] + (width + 1) * position[1]


# return the character in the game_map at given coordinates
def get_case_content(position):
    # TODO check if position goes outside of the map, return None in that case
    return game_map[get_map_index(position)]


# remove a gum of the map
def remove_gum_from_map(position):
    # use this line to modify the game_map global variable in the function
    global game_map
    # just in case, check that the case at given position contains a gum !
    if get_case_content(position) != GUM:
        print(debug_text('ERROR: trying to remove a non-existing gum'))
        return

    # convert the map into a list (so that we can change a character !)
    game_map_list = list(game_map)
    # remove the gum (put the empty char at the position of the gum)
    game_map_list[get_map_index(position)] = EMPTY
    # convert the list back to a string, that will be the updated game map
    game_map = "".join(game_map_list)


# move pacman at new position in the map
def move_pacman(current_position, next_position):
    # use this line to modify the game_map global variable in the function
    global game_map
    # TODO : complete this function (you can get inspired by remove_gum_from_map)
    # You will need the two parameters of the function
    # current_position is PACMAN's current position in the map
    # next_position is PACMAN's next position (after move)
    print(debug_text('we are now moving PACMAN'))


# display the map, with fancy colors !
def show_map(map):
    # for each char of the map
    for char in map:
        if char == WALL:
            print(char, end='')
        elif char == ENNEMY:
            print(red_text(char), end='')
        elif char == PACMAN:
            print(green_text(char), end='')
        elif char == GUM:
            print(pink_text(char), end='')
        else:
            print(char, end='')


def begin_of_the_program():
    AgeOfThePlayer = 0
    try:

        AgeOfThePlayer = int(input("Quel est ton age ? : "))

    except:
        print(red_text("ERREUR : AGE INCORRECT"))

    if AgeOfThePlayer < 12:
        exit("Vous etes trop jeune.")

# Program starts here !
if __name__ == "__main__":
    begin_of_the_program()
    print(green_text("Bienvenue dans PACMAN édition ligne de commande !"))
    # Inital positions of PACMAN and ennemy
    pacman_position = [1, 1]
    enemy_position = [6, 4]

    while True:
        # Display the game map (this is what "slow refresh game' implies)
        show_map(game_map)

        # Ask the user where he wants to go
        # convert user input to uppercase
        move = input('Votre déplacement ?').upper()

        # We copy pacman_position in next_position
        next_position = list(pacman_position)
        # Update next_position
        if move == 'L':
            next_position[0] -= 1
        elif move == 'R':
            next_position[0] += 1
        elif move == 'U':
            next_position[1] -= 1
        elif move == 'D':
            next_position[1] += 1
        else:
            print('Move not understood, try again.')
            continue

        # Depending of the content of the case, move PACMAN and take required actions
        case = get_case_content(next_position)
        if case == WALL:
            print(red_text('Vous enterred a wall, try again'))
        elif case == ENNEMY:
            print(red_text('ENNEMY THERE => YOU DIE // GAME OVER'))
            break
        elif case == GUM:
            print(green_text('Yummy !'))
            remove_gum_from_map(next_position)
            # update PACMAN position
            move_pacman(pacman_position, next_position)
            pacman_position = list(next_position)
        elif case == SUPERGUM:
            # TODO Deal with SUPERGUM effect
            print(pink_text('You are now invincible'))
            # update PACMAN position
            move_pacman(pacman_position, next_position)
            pacman_position = list(next_position)
        elif case == EMPTY:
            print(pink_text('Nothing here, keep moving'))
            # update PACMAN position
            move_pacman(pacman_position, next_position)
            pacman_position = list(next_position)
        elif case == None:
            print(red_text('You went outside of the map, stupid !'))
        else:
            print(debug_text('Something went wrong !!'))

        # TODO Check is game is finished, in that case display some messages

        # TODO Make the ennemy move
