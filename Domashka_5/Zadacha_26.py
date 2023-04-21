def stepen(a, b):
    if (b == 0):
        return 1
    elif (b == 1):
        return (a)
    elif b > 1:
        return a * stepen(a, b - 1)

a = int(input("Введите число: "))
b = int(input("Введите степень числа, которую хотите посчитать: "))
print("Результат возведения числа",a, "в степень",b, "равен:", stepen(a, b))
