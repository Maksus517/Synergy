import collections


def create(pets: dict):
    last: int = collections.deque(pets, maxlen=1)[0] + 1 if pets else 1
    pet_data: dict[str, str | int] = {}
    pet_name: str = input("Введите кличку: ")
    pet_data.setdefault("Вид питомца", input("Введите вид питомца: "))
    while True:
        try:
            pet_data.setdefault("Возраст питомца", int(input("Введите возраст питомца: ")))
            break
        except ValueError:
            choice = input("Не правильно введен возраст, повторить еще раз? (y/n)")
            if choice.lower() == "n":
                return
    pet_data.setdefault("Имя владельца", input("Введите имя владельца: "))
    pets.setdefault(last, {}).setdefault(pet_name, pet_data)


def get_id(pets) -> int | None:
    for k, v in pets.items():
        print(k, *v.keys())
    while True:
        try:
            return int(input("Введите номер питомца: "))
        except ValueError:
            choice = input("Не правильно введен возраст, повторить еще раз? (y/n)")
            if choice.lower() == "n":
                return


def read(pets):
    pet: dict = get_pet(pets, get_id(pets))
    if not pet:
        print("Нет такого питомца")
        return
    for key, value in pet.items():
        print(f'Это {value.get("Вид питомца")} по кличке "{key}", '
              f'возраст питомца: {get_suffix(value.get("Возраст питомца"))}, '
              f'имя владельца: {value.get("Имя владельца")}.')


def get_pet(pets: dict[int, dict[str, dict]], ID):
    return pets.get(ID)


def get_suffix(pet_age) -> str:
    if (2 <= pet_age % 10 <= 4) and not (11 <= pet_age % 100 <= 14):
        return f"{pet_age} года"
    elif pet_age % 10 == 1 and pet_age % 100 != 11:
        return f"{pet_age} год"
    return f"{pet_age} лет"


def update(pets):
    ID: int = get_id(pets)
    pet: dict = get_pet(pets, ID)
    if not pet:
        print("Нет такого питомца")
        return
    delete(pets, ID)
    pet_data: dict[str, str | int] = {}
    pet_name: str = input("Введите кличку: ")
    pet_data.setdefault("Вид питомца", input("Введите вид питомца: "))
    while True:
        try:
            pet_data.setdefault("Возраст питомца", int(input("Введите возраст питомца: ")))
            break
        except ValueError:
            choice = input("Не правильно введен возраст, повторить еще раз? (y/n)")
            if choice.lower() == "n":
                return
    pet_data.setdefault("Имя владельца", input("Введите имя владельца: "))
    pets.setdefault(ID, {}).setdefault(pet_name, pet_data)


def delete(pets):
    ID: int = get_id(pets)
    pets.pop(ID)


def main():
    pets: dict[int, dict[str, dict[str, str | int]]] = {}
    while True:
        print("1 - Создать")
        print("2 - Вывести на экран")
        print("3 - Изменить данные")
        print("4 - Удалить")
        print("stop - выход из программы")
        command = str(input())
        if command == "1":
            create(pets)
        elif command == "2":
            read(pets)
        elif command == "3":
            update(pets)
        elif command == "4":
            delete(pets)
        elif command.lower() == "stop":
            break


if __name__ == '__main__':
    main()
