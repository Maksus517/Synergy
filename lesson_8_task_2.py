def main():
    res = []
    for _ in range(get_checked_num(100000)):
        res.append(get_checked_num(10e9))
    res.insert(0, res.pop())
    print(*res)


def get_checked_num(count: int | float) -> int:
    while True:
        try:
            num: int = int(input(f"Введите число от 1 до {int(count)}: "))
            if 1 <= num <= count:
                return num
            print("Попробуйте еще раз")
        except ValueError:
            print("Неверный формат ввода, попробуйте еще раз")
            continue


if __name__ == '__main__':
    main()
