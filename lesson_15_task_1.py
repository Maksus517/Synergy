class Transport:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage


class Autobus(Transport):

    def print_ts(self):
        print(f'Название автомобиля: {self.name}, Скорость: '
              f'{self.max_speed} Пробег: {self.mileage}')


def main():
    name = input('Введите имя автобуса: ')
    max_speed = int(input('Введите скорость: '))
    mileage = int(input('Введите пробег: '))
    autobus = Autobus(name, max_speed, mileage)
    autobus.print_ts()


if __name__ == '__main__':
    main()
