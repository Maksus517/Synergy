def factorial(num: int) -> int:
    return 1 if num == 1 else num * factorial(num - 1)


def main():
    num: int = int(input('Введите число: '))
    new_num = factorial(num)
    res: list = [factorial(new_num - i) for i in range(new_num)]
    print(res)


if __name__ == '__main__':
    main()
