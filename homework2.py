# Task 1
print("Задание 1")
my_list = [15, 0.5, False, -7, True, -6.8, 0]
print(my_list)
def my_type(element):
    for element in range(len(my_list)):
        print(type(my_list[element]))
    return
my_type(my_list)

# Task 2
print("Задание 2")
element_count = int(input("Введите количество элементов списка: "))
my_list = []
i = 0
element = 0
while i < element_count:
    my_list.append(input("Введите значение элемента списка: "))
    i += 1
for elem in range(int(len(my_list)/2)):
        my_list[element], my_list[element + 1] = my_list [element + 1], my_list[element]
        element += 2
print(my_list)

# Task 3
print("Задание 3")
seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
month = int(input("Введите номер месяца: "))
if month ==12 or month == 1 or month == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
        print("Нет такого месяца.")

# Task 4
print("Задание 4")
my_string = input("Введите строку из нескольких слов, разделенных пробелами: ")
my_word = []
number = 1
for element in range(my_string.count(' ') + 1):
    my_word = my_string.split()
    if len(str(my_word)) <= 10:
        print(f" {number} {my_word [element]}")
        number += 1
    else:
        print(f" {number} {my_word [element] [0:10]}")
        number += 1

# Task 5
print("Задание 5")
my_list = [5, 4, 3, 2, 1]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (000 - выход): "))
while digit != 000:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число (000 - выход) "))

# Task 6
print("Задание 6")
products, order = [], 1
title, price, amount = None, None, None
while True:
    if title is None:
        tmp = input('Введите наименование товара: ')
        if not tmp.isalnum():
            print('Наименование товара не может быть пустым. Попробуйте еще раз.')
            continue
        title = tmp
    if price is None:
        tmp = input('Введите стоимость товара: ')
        if not tmp.isdigit():
            print('Цена должна быть целым числом. Попробуйте еще раз.')
            continue
        price = int(tmp)
    if amount is None:
        tmp = input('Введите количество товара: ')
        if not tmp.isdigit():
            print('Количество должно быть целым числом. Попробуйте еще раз.')
            continue
        amount = int(tmp)
    tmp = input('Введите единицы измерения: ')
    if not tmp.isalpha():
        print('Единица изменерения не может быть пустой. Попробуйте еще раз.')
        continue
    unit = tmp
    products.append((
        order,
        {
            'title': title,
            'price': price,
            'amount': amount,
            'unit': unit
        }
    ))
    title, price, amount = None, None, None
    order += 1
    print(products)
    q = input('Формирование списка завершено? (да/нет)) ')
    if q.lower() == 'да':
        break
analitics = {
    'title': [],
    'price': [],
    'amount': [],
    'unit': set()
}
for _, item in products:
    analitics['title'].append(item['title'])
    analitics['price'].append(item['price'])
    analitics['amount'].append(item['amount'])
    analitics['unit'].add(item['unit'])
print(analitics)
