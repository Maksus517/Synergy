class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"


class Autobus(Transport):
    def __str__(self):
        return f'Название автомобиля: {self.name}, Скорость: {self.max_speed} Пробег: {self.mileage}'

    def seating_capacity(self, c=50):
        return super().seating_capacity(c)


def main():
    auto = Autobus("Renaul Logan", "60", "50000")
    print(auto.seating_capacity())


if __name__ == '__main__':
    main()
