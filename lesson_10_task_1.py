def check_print_age(pet_age) -> str:
    if (2 <= pet_age % 10 <= 4) and not (11 <= pet_age % 100 <= 14):
        return f"{pet_age} года."
    elif pet_age % 10 == 1 and pet_age % 100 != 11:
        return f"{pet_age} год."
    return f"{pet_age}pet_age лет."


def main():
    pets = {}
    
    while True:
        print("1 - Ввести данные питомца")
        print("2 - Вывести данные питомца")
        print("0 - Выйти.")
        choice = str(input())
    
        if choice == "1":
            print("Введите кличку:")
            name = input()
            pets[name] = {"Вид питомца": "", "Возраст питомца": 0, "Имя владельца": ""}
    
            print("Введите вид питомца: ")
            pets[name]["Вид питомца"] = input()
    
            print("Введите возраст питомца: ")
            count = 0
            while True:
                try:
                    years = int(input())
                    break
                except ValueError:
                    if count == 5:
                        years = 0
                        break
                    count += 1
                    print("Введите корректный возраст:")
            if years == 0:
                print("Попробуйте позже")
                break
            pets[name]["Возраст питомца"] = years
    
            print("Введите имя владельца: ")
            pets[name]["Имя владельца"] = input()
    
        elif choice == "2":
            print("Какого питомца вы хотите посмотреть?", *pets.keys(), sep="\n")
            name = input()
            if pets.get(name):
                print("Это", pets[name]["Вид питомца"], "по кличке", '"{}".'.format(name), "Возраст питомца:",
                      check_print_age(pets[name]["Возраст питомца"]), "Имя владельца:", pets[name]["Имя владельца"])
            else:
                print("Такого питомца не существует")
        else:
            break


if __name__ == '__main__':
    main()
    