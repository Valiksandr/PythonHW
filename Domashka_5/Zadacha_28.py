def sum(a, b):
    if b != 0:
        a += 1
        b -= 1
        sum(a, b)
    else:
        print(a)
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
sum(a, b)
