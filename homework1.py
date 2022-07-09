# Task 1
print("Задание 1")
a = "Разбираю урок 1"
b = "это интересно"
c = "весело."
print(f"{a}, {b}, {c}")
day = input("День сейчас будний или выходной?: ")
if day == "будний":
    print("О нет!")
elif day == "выходной":
    print("Ура!")
else:
    print("Пока непонятно? Надо разбираться!")
pets = input("Кто симпатичнее, кошки или собаки?: ")
if pets == "кошки":
    print("Мы с вами совершенно согласны!")
else:
    print("Кошачья мафия осуждает ваш выбор!")
print("Давайте поиграем. Сколько зубов в норме у взрослого кота?")
tooth = int(input("Ваш ответ: "))
if tooth > 30:
    print("Неа. Это же не акула.")
elif tooth < 30:
    print("Нет, это что-то маловато.")
else:
    print("Верно, вы - знатный фелинолог!")

# Task 2
print("Задание 2")
time = int(input("Введите время в секундах, пожалуйста: "))
hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')

# Task 3
print("Задание 3")
n = input("Введите число, пожалуйста: ")
print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")

# Task 4
print("Задание 4")
a = int(input("Введите целое положительное число: "))
minim = 10
while a:
    d = a % 10
    if d < minim:
        minim = d
    a //= 10
print(f"Наименьшая цифра в вашем числе - это {minim}")

# Task 5
print("Задание 5")
revenue = float(input("Введите значение выручки, руб.: "))
costs = float(input("Введите значение издержек, руб.: "))
taxes = float(input("Введите значение налогов, руб.: "))
loans = float(input("Введите значение процентов по кредитам, руб.: "))
deprecation = float(input("Введите значение амортизации, руб.: "))
profit = revenue - costs - taxes - loans - deprecation
profitability = 100 * (profit / revenue)
print(f"Чистая прибыль равна {profit}")
print(f"Рентабельность чистой прибыли равна {profitability :.1f}%")
print("Оптимальное значение рентабельности продаж по чистой прибыли составляет 15-30%.")
if profitability < 15:
    print("Плохо дело, прогорите скоро с такой эффективностью работы.")
elif profitability > 30:
    print("Ничего себе! Вы - эффективные менеджеры!")
else:
    print("Все в норме. Но у вас есть потенциал для развития!")

# Task 6
print("Задание 6")
while True:
    days = 1
    start = float(input("Начальный результат: "))
    fin = float(input("Конечный результат: "))
    if start <= 0 or fin < 0:
        print("Результаты не дожны быть меньше 0. Начальное значение != 0.")
    else:
        while start < fin:
            start += start * 0.5
            days += 1
        print(f"Результат будет достигнут за {days} дней")
        break
