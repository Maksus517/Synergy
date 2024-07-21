def factorial(num: int) -> int:
    return 1 if num == 1 else num * factorial(num - 1)


def main():
    num: int = int(input('Введите число: '))
    res: list = [factorial(num - i) for i in range(num)]
    print(res)


if __name__ == '__main__':
    main()
