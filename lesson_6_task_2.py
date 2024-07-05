def main():
    q: int = 0
    num: int = int(input("Введите число: "))
    for n in range(1, num + 1):
        if num % n == 0:
            q += 1
    print(f"Количество натуральных делителей {q}")


if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print("Неверный формат ввода")
