def print_list(x):
    print(x[0])
    x.pop(0)
    if len(x) != 0:
        print_list(x)
    else:
        print("Конец списка")


if __name__ == '__main__':
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    print_list(x)
