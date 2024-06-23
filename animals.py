class Animals:
    def __init__(self, pet_type: str, pet_age: int, pet_nickname: str):
        self.pet_type = pet_type
        self.pet_age = pet_age
        self.pet_nickname = pet_nickname

    def print_animal(self) -> None:
        print_age: str = self.__check_print_age(self.pet_age)
        print(f'Это {self.pet_type.lower()} по кличке "{self.pet_nickname}". Возраст: {self.pet_age} {print_age}')

    def __check_print_age(self, age: int) -> str:
        if (2 <= age % 10 <= 4) and not (11 <= self.pet_age % 100 <= 14):
            return "года."
        elif self.pet_age % 10 == 1 and self.pet_age % 100 != 11:
            return "год."
        return "лет."


def main():
    type_pet: str = input("Введите вид питомца: ")
    while True:
        try:
            age_pet: int = int(input("Введите возраст питомца: "))
            break
        except ValueError:
            print("Некорректно введен возраст питомца, попробуйте снова")

    name_pet: str = input("Введите кличку питомца: ")
    animals: Animals = Animals(type_pet, age_pet, name_pet)
    animals.print_animal()


if __name__ == '__main__':
    main()
