class Turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s == 1:
            print('S не может равняться 0')
            return
        self.s -= 1

    def count_moves(self, x2, y2):
        res_x = self.__calc_count(self.x, x2)
        res_y = self.__calc_count(self.y, y2)
        print(res_y + res_x)

    def __calc_count(self, i, j):
        count = 0
        if i > j:
            count = self.__calculate(count, i, j)
        else:
            count = self.__calculate(count, j, i)
        return count

    def __calculate(self, count, i, j):
        while i > j:
            j += self.s
            count += 1
        return count

