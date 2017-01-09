import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_maze(rooms, player):
    print('_'*21)
    cell = '|{}'

    for room in rooms:
        x, y = room

        if x < 4:
            line_end = ''
            if room == player:
                output = cell.format('_*_')
            else:
                output = cell.format('___')
        else:
            line_end = "\n"
            if room == player:
                output = cell.format('_*_|')
            else:
                output = cell.format('___|')
        print(output, end=line_end)


def get_locations(rooms):
    return random.sample(rooms, 2)


def get_move(player):
    move = input('"L" to move left, "R" to move right, "U" to move up, "D" to move down\n>').lower()
    x, y = player
    legit_moves = ['l', 'r', 'u', 'd']
    if x == 0:
        moves.remove('l')
    if x == 4:
        moves.remove('r')
    if y == 0:
        moves.remove('u')
    if y == 4:
        moves.remove('d')
    return move

def check_move(move):
    x, y = move
    legit_moves = ['l', 'r', 'u', 'd']
    if x == 0:
        moves.remove('l')
    if x == 4:
        moves.remove('r')
    if y == 0:
        moves.remove('u')
    if y == 4:
        moves.remove('d')
    return legit_moves

def move_player(rooms, player):
    move = get_move()
    x, y = player

    if move in 'lrud':
        if move in check_move(move):
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
            print("\n There is a wall there... Are you feeling ok?")
            move_player(rooms, player)
    else:
        print("\nThat's not a direction. The nightmares are affecting you, eh?")
        move_player(rooms, player)

    return player



def run_maze(debug=True):
    ROOMS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
             (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
             (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
             (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
             (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

    exit, player = get_locations(ROOMS)

    while player != exit:
        clear_screen()
        draw_maze(ROOMS, player)
        if debug:
            print('exit = ' + str(exit))
        player = move_player(ROOMS, player)
    else:
        print("\nYou found the exit!!!\n")



run_maze()