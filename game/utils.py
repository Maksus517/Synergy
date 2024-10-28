from random import randint as rand


def check_bounds(coordinate_x, coordinate_y, width, height):
    if coordinate_x < 0 or coordinate_y < 0 or coordinate_x >= width or coordinate_y >= height:
        return False
    return True


def rand_bool(cutoff, max_random_range):
    num = rand(0, max_random_range)
    return num <= cutoff


def rand_cell(width, height):
    coordinate_x = rand(0, width - 1)
    coordinate_y = rand(0, height - 1)
    return coordinate_x, coordinate_y


def next_rand_cell(coordinate_x, coordinate_y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_move = rand(0, 3)
    move_coordinate_x, move_coordinate_y = moves[direction_move][0], moves[direction_move][1]
    return coordinate_x + move_coordinate_x, coordinate_y + move_coordinate_y
