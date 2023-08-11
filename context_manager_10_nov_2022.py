# Контекстный менеджер (context manager) в Python - это удобная конструкция, которая позволяет управлять
# поведением блока кода внутри специального контекста. Он обеспечивает уверенное и элегантное управление
# ресурсами, такими как файлы или соединения с базой данных, чтобы они корректно открывались и закрывались.
#
# Контекстный менеджер можно создать с использованием ключевого слова with. Когда блок кода начинается с
# with, контекстный менеджер автоматически вызывает методы __enter__() и __exit__() объекта, который
# определен внутри него.
#
# Метод __enter__() выполняется в начале блока кода и может быть использован для инициализации ресурсов.
# Например, для открытия файла или установки соединения с базой данных. Результат, возвращаемый
# методом __enter__(), будет доступен в переменной после ключевого слова as.
#
# После выполнения блока кода метод __exit__() вызывается независимо от того, произошло
# исключение или нет. Он закрывает ресурсы и освобождает память, занимаемую ими.
#
# Пример использования контекстного менеджера для работы с файлами выглядит так:
# with open("file.txt", "r") as file:
#     content = file.read()
#     print(content)
#
#
# В этом примере, блок кода, выполняемый внутри with, отвечает за чтение содержимого файла.
# Контекстный менеджер open("file.txt", "r") автоматически открывает файл для чтения в начале
# блока и закрывает его в конце блока. Переменная file содержит доступ к файлу во время
# выполнения блока кода.

# f = open('file.txt', 'w')
# f.write('Hello, World!')
# f.close()

# f = open('file.txt', 'w')
#
# try:
#     f.write('Hello, Globe!')
# except:
#     print('An error occurred')
# finally:
#     f.close()

# with open('file.txt', 'w') as f:
#     f.write('Hello, Earth!')

# with open('file.txt', 'w') as file_data:
#     file_data.write('Hello, Planet!')

# class Resource:
#     def __init__(self, name):
#         print(f'Resource: create {name}')
#         self.name = name
#
#     def get_name(self):
#         return self.__name
#
#     def post_work(self):
#         print(f'Resource: close')
#
#
# class ResourceForWith:
#     def __init__(self, name):
#         self.__resource = Resource(name)
#
#     def __enter__(self):
#         return self.__resource
#
#     def __exit__(self, type, value, traceback):
#         self.__resource.post_work()
#
# with ResourceForWith('Worker') as r:
#     print(r.get_name())


from contextlib import contextmanager

@contextmanager
def processor():
    print('--> start processing')
    yield # makes python function a generator
    print('<-- stop processing')

with processor():
    print('::processing')

from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    yield f
    f.close()

with open_file('file.txt', 'w') as fw:
    fw.write('Hello, World!!!')