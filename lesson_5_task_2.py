letters: list = ['a', 'e', 'i', 'o', 'u']
string: str = input("Введите строку")
result: int = 0
for letter in string:
    if letter in letters:
        result += 1

print(result) if result else print(False)
