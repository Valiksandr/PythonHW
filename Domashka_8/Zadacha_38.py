#     print('\nПриветствую! Вы открыли телефонный справочник Александра.')
#     print('\nВыберите пункт меню, нажав соответствующую цифру.')
#     print('1. Добавить новую запись.')
#     print('2. Закрыть программу.\n')

   
# def add_into_file():
#     data = open(path, 'a', encoding='UTF-8')
#     firstname = input("Имя: ").capitalize()
#     fathername = input("Отчество: ").capitalize()
#     surname = input("Фамилия: ").capitalize()
#     mobile_phone_number = input("Мобильный телефон: ")
#     data.write(f"{surname} - {firstname} - {fathername} - {mobile_phone_number}")
#     data.close()

# path = 'phonebook.txt'

# main_menu()
n = int(input('Выберите пункт меню: '))
if n == 1:
    add_into_file()
elif n==2:
    print('Спасибо за работу!')
else:
    print('\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')