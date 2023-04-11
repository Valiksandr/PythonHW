dlina = int(input("Длина шоколадки в кусочках: "))
shirina = int(input("Ширина шоколадки в кусочках: "))
kusok = int(input("Желаемый кусок за раз: "))
if kusok < dlina * shirina and ((kusok % dlina == 0) or (kusok % shirina == 0)):
    print('Можно! Ломай ее полностью!')
else:
    print('Голову себе поломай!')