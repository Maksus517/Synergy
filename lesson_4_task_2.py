from dataclasses import dataclass


@dataclass
class Nums:
    num: int

    def get_result(self) -> float | str:
        str_num: str = str(self.num)
        return (int(str_num[-2]) ** int(str_num[-1])) * int(str_num[-3]) / (int(str_num[0]) - int(str_num[1])) \
            if len(str_num) == 5 else "Введено не пятизначное число"


def main():
    try:
        nums: Nums = Nums(int(input("Введите пятизначное число: ")))
    except ValueError:
        print("Ошибка ввода, попробуйте еще раз")
        return
    print(nums.get_result())


if __name__ == '__main__':
    main()
