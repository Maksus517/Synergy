def main():
    x, a, b = float(input("Введите минимальную сумму: ")), \
        float(input("Введите сумму Майкла: ")), float(input("Введите сумму Ивана: "))

    if a >= x and b >= x:
        print(2)
    elif a >= x >= b:
        print("Mike")
    elif b >= x >= a:
        print("Ivan")
    elif a + b >= x:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print("Неверный формат ввода")
