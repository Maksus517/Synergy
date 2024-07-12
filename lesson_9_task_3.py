def main():
    numbers = [s for s in input("Введите последовательность чисел: ").split()]
    warehouse = set()
    for num in numbers:
        print('YES') if num in warehouse else print('NO'), warehouse.add(num)


if __name__ == '__main__':
    main()
    