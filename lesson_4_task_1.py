from dataclasses import dataclass


@dataclass
class Sides:
    side_a: int | float
    side_b: int | float
    side_c: int | float
    side_d: int | float


@dataclass
class Rectangle:
    sides: Sides

    def get_area(self) -> int | float:
        return self.sides.side_a * self.sides.side_b

    def get_perimeter(self) -> int | float:
        return (self.sides.side_a + self.sides.side_b) * 2


def main() -> None:
    while True:
        try:
            a_c = float(input("Введите сторону прямоугольника a/c: "))
            b_d = float(input("Введите сторону прямоугольника b/d: "))
            break
        except ValueError:
            choice = input("Некорректно введены данные, попробовать еще? Y/N: ")
            if choice.lower() != "y":
                print("\nХорошо, можно попробовать позже")
                return

    sides: Sides = Sides(a_c, b_d, a_c, b_d)
    rectangle: Rectangle = Rectangle(sides)
    print(f'\nПлощадь прямоугольника = {rectangle.get_area():g}',
          f'Периметр прямоугольника = {rectangle.get_perimeter():g}', sep="\n")


if __name__ == '__main__':
    main()
