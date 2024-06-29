x, a, b = float(input("введите минимальную сумму: ")), \
    float(input("введите сумму Майкла: ")), float(input("введите сумму Ивана: "))

if a >= x and b >= x:
    print(2)
elif a >= x >= b:
    print("Mike")
elif b >= x >= a:
    print("Ivan")
elif a + b >= x:
    print(1)
else:
    print(0)
