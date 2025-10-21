from Main import *
from WorkWithJson import *

commands = '1. Ввести данные вручную | 2. Импортировать данные из файла'
print(commands)
print('___'*30+'\n')
choice = int(input())

def workWithoutJson():
    # input
    print("Введите данные\n")

    try:
        length_input = int(input(f'Введите длину пароля [По умолчанию: {DEFAULT_PASSWORD_LENGTH}]\n'))
    except ValueError:
        length_input = DEFAULT_PASSWORD_LENGTH
        print(f'Ошибка ввода. Установлена длина по умолчанию.')

    try:    
        input_iterations = int(input('Введите количество повторений\n'))
    except ValueError:
        input_iterations = DEFAULT_ITERATIONS
        print('Ошибка ввода. Установлено количество повторений по умолчанию.')
        
    salt = input('Введите пароль\n')
    service = input('Введите сервис\n')
    login = input('Введите логин\n')


    # output
    password = generate_password(salt, service, login, length_input, input_iterations)
    print(outputData(password, service))

def workWithJson():
    # input
    print('___'*30)
    output_list()
    choiceData = int((input('___'*30+'\nВыберите строку с данными\n')))-1

    try:
        length_input = int(input(f'Введите длину пароля [По умолчанию: {DEFAULT_PASSWORD_LENGTH}]\n'))
    except ValueError:
        length_input = DEFAULT_PASSWORD_LENGTH
        print(f'Ошибка ввода. Установлена длина по умолчанию')

    try:    
        input_iterations = int(input('Введите количество повторений\n'))
    except ValueError:
        input_iterations = DEFAULT_ITERATIONS
        print('Ошибка ввода. Установлено количество повторений по умолчанию.')

    # output
    password, service = generate_password_with_json(choiceData, length_input, input_iterations)
    print(outputData(password, service))

if choice == 1:
    workWithoutJson()

elif choice == 2:
    workWithJson()

else:
    print("Выбор не был сделан или был сделан не корректно")
