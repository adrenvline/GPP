# Этот модуль предназначен для вывода ошибки в случае неправильного ввода данных, чтобы повторить попытку
from Validators import *

def input_string(prompt, allow_empty = False):

    while True:
        value = input(prompt).strip()
        if allow_empty or validate_non_empty(value):
            return value
        print("Ошибка: поле не может быть пустым")

def input_int(prompt, min_value, max_value, default = None):

    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input and default is not None:
                return default

            value = int(user_input)
            if validate_int_range (value, min_value, max_value):
                return value
            print(f"Число должно быть от {min_value} до {max_value}")
        except ValueError:
            print("Ошибка: введите целое число")

def input_choice(prompt, max_choices):

    return input_int(prompt, 1, max_choices)