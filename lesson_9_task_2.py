def main():
    row1: set = set(filter(None, input("Введите первую строку чисел: ").split()))
    row2: set = set(filter(None, input("Введите вторую строку чисел: ").split()))
    print(len(row1 & row2))


if __name__ == '__main__':
    main()
