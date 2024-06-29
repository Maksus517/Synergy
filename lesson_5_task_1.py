from dataclasses import dataclass


@dataclass
class NumsChecker:
    num: float

    def print_result(self) -> None:
        if self.num == 0:
            print("Нулевое число")
        else:
            print(f"{self.__get_positive()} {self.__get_even()}")
            if not self.__check_even():
                print("Число не является четным")

    def __get_even(self) -> str:
        return "четное число" if self.__check_even() else "нечетное число"

    def __get_positive(self) -> str:
        return "Положительное" if self.num == abs(self.num) else "Отрицательное"

    def __check_even(self) -> bool:
        return self.num % 2 == 0


def main() -> None:
    try:
        num: int = int(input("Введите число: "))
    except ValueError:
        print("Неверный формат ввода")
        return

    nums_checker: NumsChecker = NumsChecker(num)
    nums_checker.print_result()


if __name__ == '__main__':
    main()
