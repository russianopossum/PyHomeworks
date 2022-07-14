# Task 1
print("Задание 1")
def calculator(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f'Деление на ноль запрещено.')
print(calculator(int(input('Первое число: ')), int(input('Второе число: '))))

# Task 2
print("Задание 2")
def personal_data(name, lastname, year_of_birth, city, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {year_of_birth} Город проживания: {city} Email: {email} Телефон: {phone}')
personal_data(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    year_of_birth=input('Год рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '),
)

# Task 3
print("Задание 3")
def my_func(arg1, arg2, arg3):
    print(f'Сумма двух наибольших аргументов: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')
my_func(
    int(input('Аргумент 1:')),
    int(input('Аргумент 2:')),
    int(input('Аргумент 3:')),
)

# Task 4
print("Задание 4")
# Ну, если просто, то там скучно, будет с return x ** y
def my_func(x, y):
    if y == 0:
        return 1
    y = abs(y)
    return x * my_func(x, y-1)
while True:
    try:
        x = float(input("Введите действительное положительное число x: "))
        if x < 0:
            raise Exception()
        y = int(input("Введите целое отрицательное число y: "))
        if y > 0:
            raise Exception()
        print(1 / my_func(x, y))
        break
    except Exception as e:
        print('Ошибка в формате ввода данных.')

# Task 5
print("Задание 5")
def calculate_sum(*nums):
    sum = 0
    flag = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            flag = True
    return sum, flag
general_sum = 0
while True:
    numbers_string = input('Введите числа через пробел: ').split(' ')
    sum, stop_flag = calculate_sum(*numbers_string)
    general_sum += sum
    print(f'сумма {general_sum}')
    if stop_flag:
        break

# Task 6, 7
print("Задание 6, 7")
def int_func(text):
    return text.title()
def my_title(text):
    listed_text = list(text)
    listed_text[0] = listed_text[0].upper()
    return ''.join(listed_text)
output_1 = []
output_2 = []
for word in input('Введите строку, слова в которой разделены пробелами: ').split(' '):
    output_1.append(int_func(word))
    output_2.append(my_title(word))
print(f'Вар. 1: {" ".join(output_1)}')
print(f'Вар. 2: {" ".join(output_2)}')
