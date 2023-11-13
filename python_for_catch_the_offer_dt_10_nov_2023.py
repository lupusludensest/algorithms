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

moscow = []
not_moscow = []

for i in dct_a.values():
  if i['address'] == 'Moscow':
    moscow.append(i)
  else:
    not_moscow.append(i)

print(f"Moscow: {moscow};\nNot Moscow: {not_moscow};")