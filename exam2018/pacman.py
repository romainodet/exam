###
### Author : Antoine Scherrer <antoine.scherrer@lecole-ldlc.com>
### License : GPL
###
import random, time
# The game map, as a large string
# Be careful not to include useless spaces on the right when you modify the map !


game_map = """
##########
.C ..o. .#
#.## #. .#
#.##.#.  #
#.B. .X .#
# . .  . #
##########
"""

# Definition of each component of the map
PACMAN = 'C'
ENNEMY = 'X'
WALL = '#'
SUPERGUM = 'o'
GUM = '.'
EMPTY = ' '
EAT_WALL = 'B'

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
    global height, width
    if position[1] > height or position[0] > width or position[0] < 0 or position[1] < 0:
        return None
    else:
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

    # convert the map into a list (so that we can change a character !)
    game_map_list = list(game_map)
    # remove the gum (put the empty char at the position of the gum)
    game_map_list[get_map_index(current_position)] = EMPTY
    # convert the list back to a string, that will be the updated game map
    game_map_list[get_map_index(next_position)] = PACMAN
    game_map = "".join(game_map_list)

    # print(debug_text('we are now moving PACMAN'))

# move pacman at new position in the map
def move_monster(current_position, next_position):
    # use this line to modify the game_map global variable in the function
    global game_map

    # convert the map into a list (so that we can change a character !)
    game_map_list = list(game_map)
    # remove the gum (put the empty char at the position of the gum)
    game_map_list[get_map_index(current_position)] = EMPTY
    # convert the list back to a string, that will be the updated game map
    game_map_list[get_map_index(next_position)] = ENNEMY
    game_map = "".join(game_map_list)

    #print(debug_text('we are now moving ENNEMY'))

# display the map, with fancy colors !
def show_map(map):
    # for each char of the map
    global invincible
    for char in map:
        if char == WALL:
            print(char, end='')
        elif char == ENNEMY:
            if invincible == 1:
                print(pink_text(char), end='')
            else:
                print(red_text(char), end='')
        elif char == PACMAN:
            if invincible == 1:
                print(blue_text(char), end='')
            else:
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


def end_of_the_program():
    global count_gum, enemy_counter, start
    end = time.time()
    print(green_text("Bravo!"), "vous avez gagné!")
    if count_gum <= 1:
        print("Vous avez attrapé", count_gum, "gomme")
    else:
        print("Vous avez attrapé", count_gum, "gommes")
    if enemy_counter > 0:
        if enemy_counter == 1:
            print("Vous avez mangé", enemy_counter, "ennemi")
        else:
            print("Vous avez mangé", enemy_counter, "ennemis")
    print("Le temps passé à manger des gums est de", red_text(str(round(end - start))), "secondes")

def count_number_of_gum():
    global game_map

    game_map_list = list(game_map)
    total = game_map_list.count('.')
    return total

# Program starts here !
if __name__ == "__main__":
    begin_of_the_program()
    print(green_text("Bienvenue dans PACMAN édition ligne de commande !"))
    # Inital positions of PACMAN and ennemy
    pacman_position = [1, 1]
    enemy_position = [6, 4]
    count_gum = 0
    total_gum = count_number_of_gum()
    invincible = 0
    enemy_counter = 0
    B_case = 0
    number_of_wall_eaten = 0

    while True:
        start = time.time()
        # Display the game map (this is what "slow refresh game' implies)
        show_map(game_map)

        # Ask the user where he wants to go
        # convert user input to uppercase
        try:
            move = input('Votre déplacement ?').upper()

        except:
            print("Une erreur c'est malheuresement produite.")

        # We copy pacman_position in next_position
        next_position = list(pacman_position)
        # Update next_position
        if move == 'L' or move == 'G':
            next_position[0] -= 1
        elif move == 'R':
            next_position[0] += 1
        elif move == 'U':
            next_position[1] -= 1
        elif move == 'D':
            next_position[1] += 1
        elif move == 'Q':
            exit("Vous avez demandez à quitter le jeu. Adieu")
        elif move == "?":
            mid = time.time()
            if count_gum <= 1:
                print("Vous avez attrapé", count_gum, "gomme")
            else:
                print("Vous avez attrapé", count_gum, "gommes")
            if enemy_counter > 0:
                if enemy_counter == 1:
                    print("Vous avez mangé", enemy_counter, "ennemi")
                else:
                    print("Vous avez mangé", enemy_counter, "ennemis")
            print("Le temps actuel passé à manger des gums est de", red_text(str(round(mid - start))), "secondes")
            continue
        else:
            print('Move not understood, try again.')
            continue

        if count_gum == total_gum:
            end_of_the_program()
            exit("Fin Du Jeu")

        # monster random direction
        if enemy_counter == 0:
            ok = 0
            while ok != 1:
                next_position_monster = list(enemy_position)
                direction = random.choice("LRDU")

                if direction == 'L' or direction == 'G':
                    next_position_monster[0] -= 1
                elif direction == 'R':
                    next_position_monster[0] += 1
                elif direction == 'U':
                    next_position_monster[1] -= 1
                elif direction == 'D':
                    next_position_monster[1] += 1
                else:
                    print('direction not understood, try again.')
                    continue

                case_monster = get_case_content(next_position_monster)
                if case_monster == WALL:
                    continue
                elif case_monster == ENNEMY:
                    continue
                elif case_monster == GUM:
                    remove_gum_from_map(next_position_monster)
                    # update PACMAN position
                    move_monster(enemy_position, next_position_monster)
                    enemy_position = list(next_position_monster)
                    ok = 1
                elif case_monster == SUPERGUM:
                    move_monster(enemy_position, next_position_monster)
                    enemy_position = list(next_position_monster)
                    ok = 1
                elif case_monster == EMPTY:
                    # update PACMAN position
                    move_monster(enemy_position, next_position_monster)
                    enemy_position = list(next_position_monster)
                    ok = 1
                elif case_monster == EAT_WALL:
                    # update PACMAN position
                    move_monster(enemy_position, next_position_monster)
                    enemy_position = list(next_position_monster)
                    ok = 1
                elif case_monster == PACMAN:
                    print(red_text('ENNEMY EAT YOU ==> GAME OVER'))
                    ok = 1
                    break
                elif case_monster == None:
                    continue
                else:
                    print(debug_text('Something went wrong !!'))

        # Depending of the content of the case, move PACMAN and take required actions
        case = get_case_content(next_position)
        if case == WALL:
            if B_case == 1:
                print(blue_text('Slurp! A wall'))
                # update PACMAN position
                move_pacman(pacman_position, next_position)
                pacman_position = list(next_position)
                number_of_wall_eaten += 1
            else:
                print(red_text('Vous enterred a wall, try again'))
        elif case == ENNEMY:
            if invincible == 1:
                print(pink_text("Slurp! This monster is delicious!"))
                enemy_counter += 1
                # update PACMAN position
                move_pacman(pacman_position, next_position)
                pacman_position = list(next_position)
            else:
                print(red_text('ENNEMY THERE => YOU DIE // GAME OVER'))
                break
        elif case == GUM:
            print(green_text('Yummy !'))
            remove_gum_from_map(next_position)
            # update PACMAN position
            move_pacman(pacman_position, next_position)
            pacman_position = list(next_position)
            count_gum += 1
        elif case == SUPERGUM:
            print(pink_text('You are now invincible'))
            invincible = 1
            # update PACMAN position
            move_pacman(pacman_position, next_position)
            pacman_position = list(next_position)
        elif case == EMPTY:
            print(pink_text('Nothing here, keep moving'))
            # update PACMAN position
            move_pacman(pacman_position, next_position)
            pacman_position = list(next_position)
        elif case == EAT_WALL:
            print(blue_text("YOU CAN EAT THE WALLS!"))
            # update PACMAN position
            move_pacman(pacman_position, next_position)
            pacman_position = list(next_position)
            B_case = 1
        elif case == None:
            print(red_text('You went outside of the map, stupid !'))
        else:
            print(debug_text('Something went wrong !!'))
