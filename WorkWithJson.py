# Этот модуль предназначен для обработки json файлов и выборки оттуда данных
import json
from Main import *
from InputHandlers import *

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
    master_password = input_string('Введите пароль\n')
    result = generate_password(master_password, service, login, length_input, input_iterations)
    return result, service

