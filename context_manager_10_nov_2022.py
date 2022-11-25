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
    yield
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
    fw.write('Hello, World!')