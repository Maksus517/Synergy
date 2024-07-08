def main():
    res = []
    for _ in range(int(input())):
        res.append(int(input()))
    res.reverse()
    print(*res)


if __name__ == '__main__':
    main()
