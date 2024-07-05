def main():
    string: str = str(input("Введите слово: "))
    print("yes" if string[::-1] == string else "no")


if __name__ == '__main__':
    main()

