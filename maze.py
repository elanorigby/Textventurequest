import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_locations(rooms):
    return random.sample(rooms, 2)


def draw_maze(rooms, exit, player):
    print('_'*21)
    cell = '|{}'

    for room in rooms:
        x, y = room
        if x < 4:
            line_end = ''
            if room == player == exit:
                output = cell.format('[*]')
            elif room == player:
                output = cell.format('_*_')
            else:
                output = cell.format('___')
        else:
            line_end = "\n"
            if room == player == exit:
                output = cell.format('[*]|')
            elif room == player:
                output = cell.format('_*_|')
            else:
                output = cell.format('___|')
        print(output, end=line_end)


def get_move():
    move = input('"L" to move left, "R" to move right, "U" to move up, "D" to move down\n>').lower()
    return move


def check_move(player):
    """
    Makes sure not they don't teleport through the outer walls.
    :param player:
    :return:
    """

    x, y = player
    legit_moves = ['l', 'r', 'u', 'd']
    if x == 0:
        legit_moves.remove('l')
    if x == 4:
        legit_moves.remove('r')
    if y == 0:
        legit_moves.remove('u')
    if y == 4:
        legit_moves.remove('d')
    return legit_moves


def move_player(rooms, player):
    move = get_move()
    x, y = player

    if move in 'lrud':
        if move in check_move(player):
            if move == 'l':
                x -= 1
            if move == 'r':
                x += 1
            if move == 'u':
                y -= 1
            if move == 'd':
                y += 1
            return x, y
        else:
            print("There is a wall there... Are you feeling ok?")
            move_player(rooms, player)
    else:
        print("That's not a direction. The nightmares are affecting you, eh?")
        move_player(rooms, player)

    return player


def run_maze(debug=True):
    ROOMS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
             (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
             (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
             (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
             (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

    exit, player = get_locations(ROOMS)
    print("~~~ MAZE OF NIGHTMARES ~~~")

    while player != exit:
        clear_screen()
        draw_maze(ROOMS, exit, player)
        if debug:
            print('exit = ' + str(exit))
        player = move_player(ROOMS, player)
    else:
        draw_maze(ROOMS, exit, player)
        print("\nYou throw open the exit door and step gasping into the sunlight.\n")


if __name__ == '__main__':
    run_maze()