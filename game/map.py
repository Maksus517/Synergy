from utils import rand_bool, rand_cell, next_rand_cell, check_bounds
import os

CELL_TYPES = {
    0: '🟩',
    1: '🌲',
    2: '🌊',
    3: '🏥',
    4: '🏪',
    5: '🔥',
    6: '☁️',
    7: '⚡️',
    8: '🚁',
    9: '💧',
    10: '🏆',
    11: '💙',
    12: '⬛',
}


class Map:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for _ in range(width)] for _ in range(height)]
        self.generate_forest(5, 10)
        self.generate_river(10)
        self.generate_garage()
        self.generate_hospital()

    def print_map(self, helico, clouds):
        print(CELL_TYPES[12] * (self.width + 2))
        for row_index in range(self.height):
            print(CELL_TYPES[12], end='')
            for cell_index in range(self.width):
                cell = self.cells[row_index][cell_index]
                if clouds.cells[row_index][cell_index] == 1:
                    print(CELL_TYPES[6], end='')
                elif clouds.cells[row_index][cell_index] == 2:
                    print(CELL_TYPES[7], end='')
                elif helico.coordinate_x == row_index and helico.coordinate_y == cell_index:
                    print(CELL_TYPES[8], end='')
                elif 0 <= cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end='')
            print(CELL_TYPES[12])
        print(CELL_TYPES[12] * (self.width + 2))

    def generate_river(self, len_river):
        random_cell = rand_cell(self.width, self.height)
        rand_coordinate_x, rand_coordinate_y = random_cell[0], random_cell[1]
        self.cells[rand_coordinate_x][rand_coordinate_y] = 2
        while len_river > 0:
            next_random_cell = next_rand_cell(rand_coordinate_x, rand_coordinate_y)
            next_coordinate_x, next_coordinate_y = next_random_cell[0], next_random_cell[1]
            if check_bounds(next_coordinate_x, next_coordinate_y, self.width, self.height):
                self.cells[next_coordinate_x][next_coordinate_y] = 2
                rand_coordinate_x, rand_coordinate_y = next_coordinate_x, next_coordinate_y
                len_river -= 1

    def generate_forest(self, cutoff, max_random_range):
        for row_index in range(self.height):
            for cell_index in range(self.width):
                if rand_bool(cutoff, max_random_range):
                    self.cells[row_index][cell_index] = 1

    def generate_tree(self):
        random_cell = rand_cell(self.width, self.height)
        rand_coordinate_x, rand_coordinate_y = random_cell[0], random_cell[1]
        if self.cells[rand_coordinate_x][rand_coordinate_y] == 0:
            self.cells[rand_coordinate_x][rand_coordinate_y] = 1

    def add_fire(self):
        random_cell = rand_cell(self.width, self.height)
        rand_coordinate_x, rand_coordinate_y = random_cell[0], random_cell[1]
        if self.cells[rand_coordinate_x][rand_coordinate_y] == 1:
            self.cells[rand_coordinate_x][rand_coordinate_y] = 5

    def update_fires(self):
        for row_index in range(self.height):
            for cell_index in range(self.width):
                cell = self.cells[row_index][cell_index]
                if cell == 5:
                    self.cells[row_index][cell_index] = 0

        for _ in range(10):
            self.add_fire()

    def generate_garage(self):
        random_cell = rand_cell(self.width, self.height)
        rand_coordinate_x, rand_coordinate_y = random_cell[0], random_cell[1]
        if self.cells[rand_coordinate_x][rand_coordinate_y] == 0:
            self.cells[rand_coordinate_x][rand_coordinate_y] = 4
        else:
            self.generate_garage()

    def generate_hospital(self):
        random_cell = rand_cell(self.width, self.height)
        rand_coordinate_x, rand_coordinate_y = random_cell[0], random_cell[1]
        if self.cells[rand_coordinate_x][rand_coordinate_y] == 0:
            self.cells[rand_coordinate_x][rand_coordinate_y] = 3
        else:
            self.generate_hospital()

    @staticmethod
    def print_stat(helico):
        print(CELL_TYPES[9], helico.tank, '/', helico.mxtank, sep='', end=' | ')
        print(CELL_TYPES[11], helico.lives, end=' | ')
        print(CELL_TYPES[10], helico.score)
        if helico.score >= helico.UPGRADE_COST:
            print('Доступна модернизация бака!')
        if helico.score >= helico.LIVE_COST:
            print('Доступна модернизация брони!')

    @staticmethod
    def game_over(score):
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print(f'GAME OVER, YOUR SCORE - {score}')
        print()
        exit(0)

    def export_data(self):
        return {
            'cells': self.cells,
        }

    def import_date(self, data):
        self.cells = data['cells'] or [[0 for _ in range(self.width)] for _ in range(self.height)]
