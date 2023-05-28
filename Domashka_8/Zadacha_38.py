path = 'phonebook.txt'

def open_main_menu():
    print('\nПриветствую! Вы открыли телефонный справочник Александра.')
    print('\nВыберите пункт меню, нажав соответствующую цифру.')
    print('1. Добавить новую запись.')
    print('2. Закрыть программу.\n')

def create_file():
    data = open(path, 'a', encoding='UTF-8')
    data.close()

def add_into_file():
    data = open(path, 'w', encoding='UTF-8')
    firstname = input("Имя: ").capitalize()
    fathername = input("Отчество: ").capitalize()
    surname = input("Фамилия: ").capitalize()
    mobile_phone_number = input("Мобильный телефон: ")
    data.write(f"{surname} - {firstname} - {fathername} - {mobile_phone_number}")
    print('Спасибо, что воспользовались этим справочником!')
    data.close()

open_main_menu()
create_file()
n = int(input('Выберите пункт меню: '))
if n == 1:
    add_into_file()
elif n==2:
    print('До свидания!!! Спасибо, что воспользовались этим справочником!')
else:
    print('\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')
