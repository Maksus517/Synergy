def main():
    res: list[int] = []
    for i in range(int(input("Введите число a: ")), int(input("Введите число b: "))):
        if i % 2 == 0:
            res.append(i)
    print(*res, sep=" ")


if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print("Неверный формат ввода")
