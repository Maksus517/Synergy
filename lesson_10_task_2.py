def main():
    nums = {}

    for i in range(10, -6, -1):
        nums[i] = i ** i

    print(nums)


if __name__ == '__main__':
    main()
