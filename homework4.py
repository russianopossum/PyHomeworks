# Task 1
print("Задание 1")
def simple_calc():
    x = float(input('Введите количество отработанных часов : '))
    y = float(input('Введите ставку за 1 час : '))
    c = float(input('Введите размер премии : '))
    pay = x * y
    return pay + c
print(f'Заработная плата составляет: {simple_calc() }')

# Task 2
print("Задание 2")
result_list = []
list = [int(i) for i in input("Введите список чисел через пробел: ").split()]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        (result_list.append(list[i]))
print("Исходный список: ", list)
print("Список, элементы которого больше предыдущего: ", result_list)

# Task 3
print("Задание 3")
list = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
print("Список чисел, кратных 20 или 21, в диапазоне от 20 до 240: ", list)

# Task 4
print("Задание 4")
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print("Исходный список:\n", my_list)
new_list = [i for i in my_list if my_list.count(i) == 1]
print("Элементы списка, не имеющие повторений:\n", new_list)

# Task 5
print("Задание 5")
from functools import reduce
list = [i for i in range(100, 1001, 2)]
print("Список четных чисел от 100 до 1000]:\n", list)
print("Произведение всех элементов списка:\n", reduce(lambda x,y: x*y, list))

# Task 6
print("Задание 6")
from itertools import count, cycle

print("Итератор, генерирующий целые числа, начиная с указанного:")
for item in count(5):
    if item > 10:
        break
    else:
        print(item)

print("Итератор, повторяющий элементы некоторого списка, определенного заранее:")
i = 0
for value in cycle([3, 6, 11, 0, 9]):
    if i > 15:
        break
    print(value)
    i += 1

# Task 7
print("Задание 7")
from math import factorial
def factorial_gen(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)
print("Вычисление факториала")
for el in factorial_gen(8):
    print(el)
