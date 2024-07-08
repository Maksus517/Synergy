def main():
    res = []
    for _ in range(get_checked_num()):
        res.append(get_checked_num())
    print(*res[::-1])


def get_checked_num() -> int:
    while True:
        try:
            num: int = int(input("Введите число от 1 до 10000: "))
            if 1 <= num <= 10000:
                return num
            print("Попробуйте еще раз")
        except ValueError:
            print("Неверный формат ввода, попробуйте еще раз")
            continue


if __name__ == '__main__':
    main()
