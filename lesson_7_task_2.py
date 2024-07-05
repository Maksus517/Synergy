def main():
    result: list[str] = []
    for string in str(input("Введите слова: ")).split(" "):
        if string:
            result.append(string)
    print(*result, sep=" ")


if __name__ == '__main__':
    main()
