DEFAULT_PASSWORD_LENGTH = 32
DEFAULT_ITERATIONS = 10000

import hashlib
from Dictionary import all_chars
from datetime import *


def generate_password(salt, service, login, length_input=32, input_iterations=10000):

    input_data = f"{service}:{login}"
    hash_pass = hashlib.pbkdf2_hmac(
        'sha256',
        input_data.encode('utf-8'),
        salt.encode('utf-8'),
        iterations=input_iterations,
        dklen=length_input
        )

    return bytes_to_password(hash_pass)

def bytes_to_password(bytes_data):
    
# dictionary symbols

    password_chars = []
    for byte_val in bytes_data:
        index = byte_val % len(all_chars)
        password_chars.append(all_chars[index])

    password = ''.join(password_chars)
    return password

def outputData(password, service):
    now = datetime.now()
    now = now.strftime("%d-%m-%Y %H:%M")
    output = "\n[UTC "+ now + "] | Пароль для '"+ service +"' cгенерирован."+"\n"+'___'*30+'\n'+"Ваш пароль: "+ password
    return output


if __name__ == '__main__':
    # Input
    Password = input('Введите пароль\n')
    Service = input('Введите сервис\n')
    Login = input('Введите login\n')
    try:
        Length_input = int(input(f'Введите длину пароля [По умолчанию: {DEFAULT_PASSWORD_LENGTH}]\n'))
    except ValueError:
        Length_input = DEFAULT_PASSWORD_LENGTH
        print(f'Ошибка ввода. Установлена длина по умолчанию.')

    try:    
        Input_iterations = int(input('Введите количество повторений\n'))
    except ValueError:
        Input_iterations = DEFAULT_ITERATIONS
        print('Ошибка ввода. Установлено количество повторений по умолчанию.')
        
    # Output
    password = generate_password(Password, Service, Login, Length_input, Input_iterations)
    print(outputData(password, Service))