class Wallet:
    total = 0

    def top_up(self, add):
        self.total += add

    def count_1000(self):
        print(f'{self.total // 1000}т.р')

    def take_away(self, x):
        if x <= self.total:
            self.total -= x
        else:
            print(f'Недостаточно средств')


def main():
    pass


if __name__ == '__main__':
    main()
