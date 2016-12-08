# choose random start points for
#    player
#    exit

import random


def draw_maze(rooms):
    print('_____________________')
    for room in rooms:
        if room[1] == 0:
            print('|___|', end='')
        elif room[1] == 4:
            print('___|')
        else:
            print('___|', end='')


def get_location(rooms):
    return random.choice(rooms)


def move_player(rooms, player):
    move = input('"L" to move left, "R" to move right, "U" to move up, "D" to move down')
    if move.lower() in 'lrud':
        if move.lower() == 'l':  # MOVE LEFT
            if (player[1]-1) < 0:
                print("There is just a solid wall there. Try a different direction.")
                move_player(rooms, player)
            else:
                player = (player[0], player[1]-1)
                print('player = ' + str(player))

        elif move.lower() == 'r':  # MOVE RIGHT
            if (player[1]+1) > 4:
                print("There is just a solid wall there. Try a different direction.")
                move_player(rooms, player)
            else:
                player = (player[0], player[1]+1)
                print('player = ' + str(player))

        elif move.lower() == 'u':  # MOVE UP
            if (player[0]-1) < 0:
                print("There is just a solid wall there. Try a different direction.")
                move_player(rooms, player)
            else:
                player = (player[0]-1, player[1])
                print('player = ' + str(player))

        elif move.lower() == 'd':  # MOVE DOWN
            if (player[0]+1) > 4:
                print("There is just a solid wall there. Try a different direction.")
                move_player(rooms, player)
            else:
                player = (player[0]+1, player[1])
                print('player = ' + str(player))

        else:
            print('Didnt move. player = ' + str(player))
    else:
        print("That's not a direction. The nightmares are affecting you, eh?")
        move_player(rooms, player)

    return player




def run_maze():
    ROOMS = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
             (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
             (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
             (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
             (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

    draw_maze(ROOMS)
    exit = get_location(ROOMS)
    player = get_location(ROOMS)
    print('exit = ' + str(exit))
    print('player = ' + str(player))
    player = move_player(ROOMS, player)

    while player != exit:
        player = move_player(ROOMS, player)
        print(player)

    print('\n')
    print("You found the exit!!!")





run_maze()