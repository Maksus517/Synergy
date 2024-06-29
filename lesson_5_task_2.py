def main():
    letters: list = ['a', 'e', 'i', 'o', 'u']
    string: str = input("Введите слово: ").lower()
    result: int = 0
    for letter in letters:
        if letter in string:
            result += 1

    print(result) if result else print(False)


if __name__ == '__main__':
    main()
