import random
size = int(input("Введите колличество значений: "))
max = int(input("Введите максимальное значение: "))
min = int(input("Введите минимальное значение: "))
num = int(input("Че ищем, босс? Только скажи: "))


my_list = [random.randint(min, max) for _ in range(size)]
count = 0
blizkoe = my_list[0]
print(my_list)
for item in my_list:
    if item == num:
        count = count + 1
if count == 0:
    for item in my_list:
        if abs(blizkoe - num) > abs(item - num):
            blizkoe = item
    print(f"Числа", num, "тут нет! Наиболее близкое число к вашему:", blizkoe,)
else:
    print(f"Ваше число встретилось", count, "раз/а")