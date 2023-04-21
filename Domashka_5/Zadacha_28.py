def sum(a, b):
    if b != 0:
        return sum(a + 1, b-1)
    else:
        print(a)


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
sum(a, b)
