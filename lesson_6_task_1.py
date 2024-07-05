def main():
    result: int = 0
    num_range: int = int(input("Введите количество чисел: "))
    for _ in range(num_range):
        if int(input("Введите число: ")) == 0:
            result += 1
    print(result)


if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print("Неверный формат ввода")
