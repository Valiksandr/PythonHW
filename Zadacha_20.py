import random
size = int(input("Введите колличество значений: "))
max = int(input("Введите максимальное значение: "))
min = int(input("Введите минимальное значение: "))
num = int(input("Че ищем, босс: "))


my_list = [random.randint(min, max) for _ in range(size)]
count = 0
blizkoe = my_list[0]
print(my_list)
for i in my_list:
    if i == num:
        count = count + 1
print(f"Ваше число встретилось", count, "раз/а")
if count == 0:
    for i in my_list:
        if abs(i - num) < abs(blizkoe - num):
             blizkoe = i
print(f"Наиболее близкое число:", blizkoe,)
