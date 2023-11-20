# 10 ноября 2023 Анонс следующего Питон ивента:
# 1. Научиться запустить файл .py из терминала Пайчарма, UI на "теле" исполняемого файла, UI в правом верхнем углу из drop down menu. Если выдает ошибку о неверном нахождении/не может найти файл-скопипасть этот текст и прогуглить на предмет решения. См. скриншот;
# 2. "Запилить" материалы из w3. Quiz(https://www.w3schools.com/python/python_quiz.asp) и Python Tutorial(https://www.w3schools.com/python/default.asp);
# 3. Начать работать с Introduction to Python в Pycharm. Fail/Learn and Teach/Browse Courses/Marketplace/Introduction to Python;
# 4.
# Create a dictionary 'dct_a' with keys as integers:
# 1, 2, 3, 4

# and values for every key above as a sub-dictionaries
# keys in the sub-dictionaries
# 'id', 'name', 'age', 'address'

# 'id' values in the sub-dictionaries:
# 1,      2,        3,      4

# 'name' values in the sub-dictionaries:
# 'Anna', 'Peter', 'John', 'Pen'

# 'address' values in the sub-dictionaries:
# 'Rome', 'Moscow', 'Tokio', 'Moscow'

# 'age' values in the sub-dictionaries::
# 99,     33,     42,        18

# sort data in dictionary based on addresses into two sub-lists: 'moscow' and 'not_moscow'

# solution – replace * by appropriate char, variable, etc
dct_a = {
    1: {'id':1, 'name':'Anna', 'address':'Rome', 'age':99},
    4: {'id':4, 'name':'Pen', 'address':'Moscow', 'age':18},
    2: {'id':2, 'name':'Peter', 'address':'Moscow', 'age':33},
    3: {'id':3, 'name':'John', 'address':'Tokio', 'age':42}
    }

# print(dct_a)

# ass one more
# dct_a[4] = {'id':5, 'name':'Vincent', 'address':'Milano', 'age':88}

# moscow = []
# not_moscow = []
#
# for i in dct_a.values():
#   if i['address'] == 'Moscow':
#     moscow.append(i)
#   else:
#     not_moscow.append(i)
#
# print(f"Moscow: {moscow}\nTotal: {len(moscow)};\nNot Moscow: {not_moscow}\nTotal: {len(not_moscow)};")

# def high_and_low(numbers):
#     numbers_sorted = [int(x) for x in numbers.split(' ')]
#     numbers_sorted.sort()
#
#     min = numbers_sorted[0]
#     max = numbers_sorted[-1]
#
#     return str(max) + ' ' + str(min)
#
#
# print(high_and_low('8 3 -5 42 -1 0 0 -9 4 7 4 -4'))

# Lucas numbers
def lucasnum(n):
    a, b = 2, 1

    flip = n < 0 and n % 2 != 0

    for i in range(abs(n)):
        a, b = b, a + b

    return -a if flip else a

print(lucasnum(-10))