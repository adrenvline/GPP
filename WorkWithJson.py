import json
from Main import *

with open('Data.json', 'r') as f:
    data = json.load(f)

def output_list():
    for index in data:
        id = index['id']
        service = index['service']
        login = index['login']
        print(str(id)+'. '+service + ' | ' + login)

def generate_password_with_json(index, length_input, input_iterations):
    selection = data[index]
    service = selection['service']
    # print(service+'\n')
    login = selection['login']
    # print(login+'\n')
    salt = input('Введите пароль\n')
    result = generate_password(salt, service, login, length_input, input_iterations)
    return result, service

