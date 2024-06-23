class Humans:
    def __init__(self, stages: list) -> None:
        self.stages = stages

    def set_new_stages(self, stages: list) -> None:
        self.stages = stages

    def print_stages(self, is_new: bool) -> None:
        print("Ваш ответ:") if not is_new else print("Правильный ответ:")
        print(*self.stages, sep=" => ", end="\n\n")


def main():
    stg: list = [input(f"Введите {stage} стадию развития человека: ") for stage in range(1, 5)]
    humans: Humans = Humans(stg)

    # Не совсем понятно в задании, что должно выводиться в конце, что человек написал или просто все стадии
    # вывел и то и другое

    humans.print_stages(False)
    new_stg = ["Dryopithecus", "Australopithecus", "Homo erectus", "Homo neanderthalensis", "Homo sapiens"]
    humans.set_new_stages(new_stg)
    humans.print_stages(True)


if __name__ == '__main__':
    main()
