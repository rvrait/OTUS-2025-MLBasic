import re

def function1(number):
    number_str = str(number)

 
    first_digit = number_str[0]  
    central_digits = number_str[1:4]  
    last_digit = number_str[4]  

    mirrored_central = central_digits[::-1]
  
    mirrored_number = first_digit + mirrored_central + last_digit

    return mirrored_number

def function2(days_until_vacation):
    
    full_week_count = days_until_vacation // 7
    weekend_count = full_week_count * 2

    other_days = days_until_vacation % 7
    
    if other_days >= 6:
        weekend_count += 1
    if other_days >= 7:
        weekend_count += 1
    return weekend_count

def function3(string_numbers):
    numbers = [int(x.strip()) for x in string_numbers.split(',')]
    if numbers[2] > (numbers[0] * numbers[1]):
        return False
    elif numbers[2] // numbers[0] >= 1 and numbers[2] % numbers[0] == 0:
        return True
    elif numbers[2] // numbers[1] >= 1 and numbers[2] % numbers[1] == 0:
        return True
    else:
        return False
    
def function4(digitals):
  
    val_to_roman = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = ""
    for value, symbol in val_to_roman:
        while digitals >= value:
            result += symbol
            digitals -= value
    return result

def function5(chek_float_string):
    
    if not chek_float_string:
        return False

    dot_count = 0
    for char in chek_float_string:
        if char == '.':
            dot_count += 1
            if dot_count > 1:
                return False
        elif not char.isdigit():
            return False

    if chek_float_string.startswith('.') or chek_float_string.endswith('.'):
        return False

    return True

if __name__ == "__main__":
    prompt = '''Выберите программу для тестирования:
          1. Пользователь вводит пятизначное число. Программа должна зеркально отразить центральные три цифры.
          Первая и последняя остаются на местах.

          2. Отпуск. Пользователь вводит сколько дней осталось до ближайшего отпуска.
          Программа должна вывести количество выходных дней до отпуска, если учесть, 
          что выходные это суббота и воскресенье, сегодня понедельник и праздники мы не учитываем.

          3. Пользователь вводит длину и ширину плитки шоколада, а также размер куска, 
          который хочет отломить, программа должна вычислить - можно ли совершить подобный разлом или нет,
          если учесть, что ломать можно только по прямой.
          
          4. Пользователь вводит целое положительное число, программа должна вернуть строку в виде римского числа.
          
          5. Пользователь вводит данные, проверить - являются ли они положительным вещественным числом. 
          Не использовать встроенные функции для проверки, только методы данных и конструкцию IF. 
          (Дополнительное задание, по желанию - проверка на отрицательные вещественные числа)
          
          q - для выхода
          '''

    user_input = input(prompt)
    while True:
        match user_input:
            case "1":
                input_digit = input("Введите пятизначеное число (q - для выхода): ")
                pattern = r"\d{5}"
                while True:
                    if input_digit == "q":
                        print("Выход из программы!")
                        break
                    elif re.match(pattern, input_digit):
                        result = function1(input_digit)
                        print(f"Результат: {result}") 
                        input_digit = input("Введите пятизначеное число (q - для выхода): ")
                    else:
                        input_digit = input("Введено не пятизначеное число. Введите пятизначеное число (q - для выхода): ")                         
            case "2":
                input_digit = input("Введите число дней до отпуска (q - для выхода): ")
                pattern = r"\d+"
                while True:
                    if input_digit == "q":
                        print("Выход из программы!")
                        break
                    elif re.match(pattern, input_digit):
                        result = function2(int(input_digit))
                        print(f"Результат: {result}") 
                        input_digit = input("Введите число дней до отпуска (q - для выхода): ")
                    else:
                        input_digit = input("Введено не число. Введите число (q - для выхода): ")     
            case "3":
                input_digit = input("Введите три числа через запятую (q - для выхода): ")
                pattern = r"\d+,\d+,\d+"
                while True:
                    if input_digit == "q":
                        print("Выход из программы!") 
                        break
                    elif re.match(pattern, input_digit):
                        result = function3(input_digit)
                        print(f"Результат: {result}")
                        input_digit = input("Введите три числа через запятую (q - для выхода): ")
                    else:
                        input_digit = input("Введено не корректное значение. Введите три числа через запятую (q - для выхода): ")      
            case "4":
                input_digit = input("Введите целое число от 1 до 3999: ")
                pattern = r"([1-3])?\d?\d?\d"
                while True:
                    if input_digit == "q":
                        print("Выход из программы!") 
                        break
                    elif re.match(pattern, input_digit):
                        result = function4(int(input_digit))
                        print(f"Результат: {result}")
                        input_digit = input("Введите целое число от 1 до 3999: ")
                    else:
                        input_digit = input("Введено не корректное значение. Введите целое число от 1 до 3999: (q - для выхода): ")
            case "5":
                input_digit = input("Введите данные для проверки (q - для выхода): ")
                while True:
                    if input_digit == "q":
                        print("Выход из программы!") 
                        break
                    else:
                        result = function5(input_digit)
                        print(f"Результат: {result}") 
                        input_digit = input("Введите данные для проверки (q - для выхода): ")   
            case "q":
                break
            case _:
                user_input = input("Выбрано неверное значение")
        user_input = input(prompt)
  