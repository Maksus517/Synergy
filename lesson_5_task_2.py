def main():
    letters: dict[str, int] = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    string: str = input("Введите слово: ").lower()
    vowels: int = 0
    consonants: int = 0
    for letter in string:
        if letter in letters.keys():
            letters[letter] += 1
            vowels += 1
        else:
            consonants += 1
    for k, v in letters.items():
        print(f"Буква {k} - {v}") if v else print(False)
    print(f"Гласных - {vowels}")
    print(f"Согласных - {consonants}")


if __name__ == '__main__':
    main()
