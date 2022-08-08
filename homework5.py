# Task 1
my_f = open('test.txt', 'w', encoding= 'utf-8')
line = input('Ввести текст или пустую строку: \n')
while line:
    my_f.writelines(line)
    line = input('Ввести текст или пустую строку: \n')
    if not line:
        break
my_f.close()
my_f = open('test.txt', 'r', encoding= 'utf-8')
content = my_f.readlines()
print(content)
my_f.close()

# Task 2
# Собрала 10 русских поговорок :)
with open('test-5-2.txt', 'r', encoding= 'utf-8') as f_obj:
    useful = [f'{count}. {line.strip()} - {len(line.split())} слов'
        for count, line in enumerate(f_obj, 1)]
    print(*useful, f"Всего строк: {len(useful)}.", sep="\n")

# Task 3
import sys
MINIMAL_SALARY = 20000
FILENAME = "text_3.txt"
if __name__ == "__main__":
    try:
        with open(FILENAME, encoding='utf-8') as fh:
            employees = fh.readlines()
    except IOError as e:
        print(e)
        sys.exit(1)
    summ_salary = 0
    for employee in employees:
        name, salary = employee.split()
        try:
            salary = float(salary)
        except ValueError:
            continue
        summ_salary += salary
        if salary < MINIMAL_SALARY:
            print(name)
    print('Средняя зарплата: ', round(summ_salary / len(employees), 2))

# Task 4
rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('text_4.txt', 'r', encoding='utf-8') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)
with open('file_4_new.txt', 'w', encoding='utf-8') as file_obj_2:
    file_obj_2.writelines(new_file)

# Task 5
from random import randint
with open ("test-5-5.txt", "w", encoding='utf-8') as my_file:
    my_list = [randint (1, 100) for _ in range(100)]
    my_file.write(" ".join(map(str, my_list)))
print(f"Сумма элементов равна {sum(my_list)}")

# Task 6
my_dict = {}
with open("text_6.txt", encoding='utf-8') as fobj:
    for line in fobj:
        name, stats = line.split(":")
        name_sum = sum(map(int, "".join([i for i in stats if i == " " or "9" >= i >= "0"]).split()))
        my_dict[name] = name_sum
print(f"{my_dict}")

# Task 7
import json
with open ("test-5-7.json", "w", encoding='utf-8') as write_f, open("text_7.txt", encoding='utf-8') as f_obj:
    profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_obj}
    f_up = [i for i in profit.values() if i > 0]
    result = [profit, {"Средняя выручка:": round(sum(f_up) / len(f_up))}]
    json.dump(result, write_f, ensure_ascii=False, indent=4)
