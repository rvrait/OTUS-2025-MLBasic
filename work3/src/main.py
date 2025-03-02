import re

def switch_case(string_to_switch: str, case_method: bool):
    result_string = ''
    if case_method:
        need_upper = False
        for char in string_to_switch:
            if char == '_':
                need_upper = True
                continue
            result_string += char.upper() if need_upper else char
            if need_upper: need_upper = False
    else:
        for index, char in enumerate(string_to_switch):
            if char.isupper() and index > 0:
                result_string = result_string + '_' + char.lower()
            else:
                result_string += char.lower() if char.isupper else char
    return result_string

def get_id_user(string_id: str):
    string_len = len(string_id)
    while len(string_id) < 8:
        string_id = '0' + string_id
    return string_id

def output_table(data_table: dict):
    headers = ['ID', 'Фамилия', 'Имя', 'Возраст']
    col_width = 10  # Ширина каждого столбца
    headers = ["ID", "Фамилия", "Имя", "Возраст"]
    print("|".join(header.ljust(col_width) for header in headers))
    print("-" * (col_width * len(headers) + len(headers) - 1))
    for id_, (last_name, first_name, age) in data_table.items():
        row = [str(id_), last_name, first_name, str(age)]
        print("|".join(item.ljust(col_width) for item in row))

def function1(string_to_switch: str):
    if string_to_switch.find('_') > 0:
        result = switch_case(string_to_switch, 1)
    else:
        result = switch_case(string_to_switch, 0)
    return result

def function2(data_string: str):
    data_pattern = r"(0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.]\d\d\d\d"
    if not re.match(data_pattern, data_string): return False
    month_count_day = [31,28,31,30,31,30,31,31,30,31,30,31]
    data_part = data_string.split('.')
    if int(data_part[0]) > month_count_day[int(data_part[1]) - 1]: return False
    
    return True

def function3(number: int):
    for i in range(2,10):
        if number % i == 0 and number != i:
            return False
    return True

if __name__ == "__main__":
    prompt = '''Выберите программу для тестирования:
          1. Написать функцию, которая будет перводить снейк_кейс в КэмелКейс и наоборот.
          Функция сама определяет - какой формат ей передали. Можно добавить ключевой аргумент, 
          который будет принудительно возвращать один из форматов.

          2. Написать функцию проверяющую валидность введенной даты.

          3. Функция проверки на простое число. Простые числа – это такие числа, которые делятся на себя и на единицу.
          
          4. Пользователь в бесконечном цикле вводит данные пользователей: имя, затем фамилию, возраст и ID. 
          Ввод продолжается до тех пор, пока не будет введено пустое поле. Пользователи заносятся в словарь, 
          где ключ это ID пользователя, а остальные данные записываются в виде кортежа. Также программа должна проверять, 
          что имя и фамилия состоят только из символов и начинаются с большой буквы, если не с большой, 
          то заменяет на большую, возраст должен быть числом от 18 до 60, ID - целое число, дополненное до 8 знаков незначащими нулями, 
          ID должен быть уникальным.
          Дополнительно написать функцию, которая будет выводить полученный словарь в виде таблицы.
          
          q - для выхода
          '''

    
    while True:
        user_input = input(prompt)
        match user_input:
            case "1":
                while True:
                    user_input = input("Введите строку для преобразования (q - для выхода): ")
                    if user_input == "q":
                        print("Выход из программы!")
                        break
                    else: 
                        result = function1(user_input)
                        print(f"Результат: {result}") 
            case "2":
                while True:
                    user_input = input("Введите дату в формате дд.мм.гггг (q - для выхода): ")
                    if user_input == "q":
                        print("Выход из программы!")
                        break
                    else: 
                        result = function2(user_input)
                        print(f"Результат: {result}") 
            case "3":
                pattern = r"\d+"
                while True:
                    user_input = input("Введите число на проверку простого числа (q - для выхода): ")
                    if user_input == "q":
                        print("Выход из программы!")
                        break
                    elif re.match(pattern, user_input):
                        result = function3(int(user_input))
                        print(f"Результат: {result}") 
                    else: 
                        print("Не корректный ввод!", end=" ")
            case "4":
                pattern = r"[а-яА-ЯёЁ]+\s+[а-яА-ЯёЁ]+\s+\d+\s+\d+"
                age_pattern = r"(1[89]|[2-5][0-9]|60)"
                user_table = {}
                while True:
                    user_input = input("Введите данные в формате Фамилия Имя Возвраст (от 18 до 60 лет) ID (не более чем 8 цифр) (q - для выхода):")
                    if user_input == "q":
                        print("Выход из программы!")
                        break
                    elif re.match(pattern, user_input):
                        user_input = re.sub(r'\s+', ' ', user_input)
                        input_parts = user_input.split(' ')
                        if len(input_parts[3]) > 8:
                            print("ID должен быть длиной до 8 цифр!")
                            continue
                        id_user = get_id_user(input_parts[3])
                        if id_user in user_table.keys():
                            print(f"ID {id_user} уже добавлен для другого пользователя")
                            continue
                        if not re.match(age_pattern, input_parts[2]):
                            print("Возвраст должен быть от 18 до 60 лет включительно")
                            continue
                        user_table[id_user] = (input_parts[0].capitalize(), input_parts[1].capitalize(), input_parts[2])
                    elif not user_input:
                        output_table(user_table)
                    else:
                        print("Не корректный ввод!")
            case "q":
                break
            case _:
                print("Выбрано неверное значение!")
