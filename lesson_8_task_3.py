def main():
    m: int = get_checked_num(10e6)
    n: int = get_checked_num(100)
    weights: list[int] = sorted([int(input()) for _ in range(n)])
    count = 0
    for _ in range(n):
        if weights:
            weight = weights[0] + weights[-1]
            if weight > m:
                if weights[-1] <= m:
                    count += 1
                weights.pop(-1)
                continue
            weights.pop(-1)
            weights.pop(0)
            count += 1
        else:
            break
    print(f"\nКоличество: {count}")


def get_checked_num(count: int | float) -> int:
    while True:
        try:
            num: int = int(input(f"Введите число от 1 до {int(count)}: "))
            if 1 <= num <= count:
                return num
            print("Попробуйте еще раз")
        except ValueError:
            print("Неверный формат ввода, попробуйте еще раз")
            continue


if __name__ == '__main__':
    main()
