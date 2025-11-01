# Этот модуль замещает оконный менеджер, работая в консоли
from Main import generate_password, outputData, DEFAULT_ITERATIONS, DEFAULT_PASSWORD_LENGTH
from WorkWithJson import generate_password_with_json, output_list
from InputHandlers import *

commands = '1. Ввести данные вручную | 2. Импортировать данные из файла'
print(commands)
print('___'*30+'\n')
choice = int(input())

# Работа без файлов
def workWithoutJson():
    # Ввод данных 
    print("Введите данные\n")

    length_input = input_int(f'Введите длину пароля [По умолчанию: {DEFAULT_PASSWORD_LENGTH}]: ', min_value=8, max_value=64, default=DEFAULT_PASSWORD_LENGTH)
    input_iterations = input_int(f'Введите количество повторений\n', min_value=1, max_value=10000000, default=DEFAULT_ITERATIONS)
        
    master_password = input_string('Введите пароль\n')
    service = input_string('Введите сервис\n')
    login = input_string('Введите логин\n')


    # Ввод данных
    password = generate_password(master_password, service, login, length_input, input_iterations)
    print(outputData(password, service))

# Работа с файлами
def workWithJson():
    ## Ввод данных
    print('___'*30)
    output_list()

    choiceData = input_choice(('___'*30+'\nВыберите строку с данными\n'), max_choices=2) - 1
    length_input = input_int(f'Введите длину пароля [По умолчанию: {DEFAULT_PASSWORD_LENGTH}]: ', min_value=8, max_value=64, default=DEFAULT_PASSWORD_LENGTH)
    input_iterations = input_int(f'Введите количество повторений\n', min_value=1, max_value=10000000, default=DEFAULT_ITERATIONS)
    
    # Ввод данных
    password, service = generate_password_with_json(choiceData, length_input, input_iterations)
    print(outputData(password, service))

# Выбор режима работы
if choice == 1:
    workWithoutJson()

elif choice == 2:
    workWithJson()

else:
    print("Выбор не был сделан или был сделан не корректно")
