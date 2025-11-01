# Здесь находятся глобальные переменные, которые в случае чего используются по умолчанию в некоторых аргументах
DEFAULT_PASSWORD_LENGTH = 32
DEFAULT_ITERATIONS = 10000

import hashlib, getpass # getpass - Ввод данных в консоли без отображения
from Dictionary import all_chars # Библиотека символов
from datetime import *

# Генерация пароля на основе исходных данных - для всех
def generate_password(salt, service, login, length_input=32, input_iterations=10000): 
    service = service.lower()
    login = login.lower()
    input_data = f"{service}:{login}"
    hash_pass = hashlib.pbkdf2_hmac(
        'sha256',
        input_data.encode('utf-8'),
        salt.encode('utf-8'),
        iterations=input_iterations,
        dklen=length_input
        )

    return bytes_to_password(hash_pass)

# Функция перевода хэша в символы
def bytes_to_password(bytes_data):

    password_chars = []
    for byte_val in bytes_data:
        index = byte_val % len(all_chars)
        password_chars.append(all_chars[index])

    password = ''.join(password_chars)
    return password

# Функция для вывода данных в виде лога
def outputData(password, service):
    now = datetime.now()
    now = now.strftime("%d-%m-%Y %H:%M")
    output = "[UTC "+ now + "] | Пароль для '"+ service +"' cгенерирован."+"\n"+'___'*30+'\n'+"Ваш пароль: "+ password
    return output

# Модуль на проверку основного модуля
if __name__ == '__main__':

# Ввод данных
    master_password = getpass.getpass('Введите пароль. Пароль скрыт\n')
    service = input('Введите сервис\n')
    login = input('Введите login\n')
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
        
# Вывод данных
    password = generate_password(master_password, service, login, length_input, input_iterations)
    print(outputData(password, service))