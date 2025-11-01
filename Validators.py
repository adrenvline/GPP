# Здесь находится модуль для проверки на правильность заполнения исходных данных
def validate_non_empty(text):

    return text is not None and text.strip() != ""

def validate_int_range(number, min_value, max_value):

    return min_value <= number <= max_value

def validate_choice(choice, max_choices):
    return 1 <= choice  <= max_choices