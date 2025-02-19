import re

def input_free_seats(count_rows, count_seats):
    pattern = fr"((0|1)\s*,?\s*){{{count_seats}}}$"
    list_free_seats = []
    i = 1
    while True:
        user_input = input(f"Введите информацию о {count_seats} местах в ряду {i} (0 или 1, разделенных запятыми) (q - для выхода):")
        if user_input == "q":
            return None
        elif re.match(pattern, user_input):
            free_seats_in_row = [x.strip() for x in user_input.split(',')]
            list_free_seats.append(free_seats_in_row)
            i += 1
            if i > count_rows: break
        else:
            print("Не корректный ввод. ", end="")
    return list_free_seats

def function5():
    result = dict()
    pattern = r"[А-Яа-яЁё]+\s[А-Яа-яЁё]+\s\d"
    while True:
        user_input = input("Введите строку формата 'Предмет' 'Фамилия' оценка (q - для выхода, пустая строка для окончания ввода): ")
        if user_input == 'q':
            return None
        elif not user_input:
            return result
        elif re.match(pattern, user_input):
            data_input = user_input.split(' ')
            if data_input[0] in result.keys():
                if isinstance(result[data_input[0]], dict) and data_input[1] in result[data_input[0]].keys():
                    result[data_input[0]][data_input[1]].append(data_input[2])
                else:
                    result[data_input[0]][data_input[1]] = [data_input[2]]    
            else:
                result[data_input[0]] = {data_input[1] : [data_input[2]]}
        else:
            print("Не корректный ввод. ", end="")
    return result

def function1(digital_string):

    while len(digital_string) > 1:
        digital_string_result = 0
        for i in digital_string:
            digital_string_result += int(i)
        digital_string = str(digital_string_result)
    
    return digital_string

def function2(list_cinema_place: list, count_seats: int):
    result = False
    for row_index, row in enumerate(list_cinema_place):
        count_nearby_seats = 0
        for seats in row:
            if seats == '0':
                count_nearby_seats += 1
                if count_nearby_seats >= count_seats:
                    result = row_index
                    break
            else:
                count_nearby_seats = 0
      
    return result

def function3(string_to_RLE: str):
    count_char = 0
    prev_char = ""
    result = ""
    for char in string_to_RLE.strip():
        if not prev_char:
            prev_char = char
            count_char += 1
            continue    
        elif char == prev_char:
            count_char += 1
        else:
            result = result + str(count_char) + prev_char
            count_char = 1
        prev_char = char
    result = result + str(count_char) + prev_char

    return result

def function4(string_to_crypt: str, keycode: int):
    result = ""
    for char in string_to_crypt:
        shift = 65 if char.isupper() else 97
        crypt_char = chr((ord(char) - shift + keycode) % 26 + shift)
        result += crypt_char
    return result


if __name__ == "__main__":
    prompt = '''Выберите программу для тестирования:
          1. Пользователь вводит целое число, программа складывает все цифры числа,
          с полученным числом — то же самое, и так до тех пор, пока не получится однозначное число.

          2. Кинотеатр. Дан список списков, каждый вложенный список состоит из 1 и 0,
          количество вложенных списков — количество рядов. Пользователь вводит, сколько билетов ему требуется.
          Программа должна найти ряд, где можно приобрести нужное количество билетов (места должны быть рядом).
          Если таких рядов несколько, то ближайший к экрану (ближайшим считается нулевой ряд).
          Если таких мест нет, то вывести False.

          3. Написать упрощенную версию алгоритма RLE. Алгоритм RLE объединяет подряд идущие символы в коэффициент и символ.
          
          4. Шифр Цезаря. Пользователь вводит строку и ключ шифра, программа должна вывести зашифрованную строку (со сдвигом по ключу). 
          Сдвиг циклический. Используем только латинский алфавит, пробелы не шифруются.
          
          5. Табель успеваемости. Пользователь в бесконечном цикле (пока не будет введена пустая строка) вводит строки вида: 
          'название предмета' 'фамилия ученика' 'оценка'. После окончания ввода программа выводит в консоль название предмета, 
          далее список учеников и все их оценки в виде таблицы.
          
          q - для выхода
          '''

    user_input = input(prompt)
    while True:
        match user_input:
            case "1":
                input_digit = input("Введите целое число (q - для выхода): ")
                pattern = r"\d+"
                while True:
                    if input_digit == "q":
                        print("Выход из программы!")
                        break
                    elif re.match(pattern, input_digit):
                        result = function1(input_digit)
                        print(f"Результат: {result}") 
                        input_digit = input("Введите целое число(q - для выхода): ")
                    else:
                        input_digit = input("Не корректный ввод. Введите целое число (q - для выхода): ")                         
            case "2":
                while True:
                    pattern = r"\d+\s*,\s*\d+"
                    user_input = input("Введите число рядов и число кресел в ряду через запятую, например 7,4 (q - для выхода): ")
                    if user_input == "q":
                        print("Выход из программы!")
                        break
                    elif re.match(pattern, user_input):
                        numbers = [x.strip() for x in user_input.split(',')]
                        count_rows = int(numbers[0])
                        count_seats = int(numbers[1])
                        list_free_seats = input_free_seats(count_rows, count_seats)
                        if list_free_seats is None:
                            continue
                        while True:
                            pattern = r"\d+"
                            user_input = input("Введите число билетов (q - для выхода): ")
                            if user_input == "q":
                                break
                            elif re.match(pattern, user_input):
                                result = function2(list_free_seats, int(user_input))
                                print(f"{list_free_seats} Результат: {result}") 
                            else:
                                print("Не корректный ввод. ", end="")
                    else:
                        print("Не корректный ввод. ", end="")     
            case "3":
                while True:
                    user_input = input("Введите строку для RLE (q - для выхода): ")
                    if user_input == "q":
                        print("Выход из программы!") 
                        break
                    else:
                        result = function3(user_input)
                        print(f"Результат: {result}")
            case "4":
                while True:
                    user_input = input("Введите строку для шифрования (только латинские буквы) (q - для выхода)")
                    if user_input == "q":
                        print("Выход из программы!") 
                        break
                    keycode = input("Введите ключ шифрования (q - для выхода): ")
                    if keycode == "q":
                        print("Выход из программы!")
                        break
                    result = function4(user_input, int(keycode))
                    print(f"Результат: {result}")

            case "5":
                result = function5()
                if result is None:
                    continue

                for subject, students in result.items():
                    print(subject)
                    for student, marks in students.items():
                        print(student, end=" ")
                        for mark in marks:
                            print(mark, end=" ")
                        print()
                    print()
                input("Для продолжения нажмите Enter.")
            case "q":
                break
            case _:
                user_input = input("Выбрано неверное значение")
        user_input = input(prompt)