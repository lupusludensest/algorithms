# 1 Отсортировать любым способом следующий список студентов по имени и по возрасту
students =     [
        {
            "age": 28,
            "name": "Sherman"
        },
        {
            "age": 31,
            "name": "Howell"
        },
        {
            "age": 37,
            "name": "Silva"
        },
        {
            "age": 23,
            "name": "Turner"
        },
        {
            "age": 26,
            "name": "Peters"
        },
        {
            "age": 33,
            "name": "Frank"
        },
        {
            "age": 22,
            "name": "Lynn"
        },
        {
            "age": 23,
            "name": "Obrien"
        },
        {
            "age": 21,
            "name": "Armstrong"
        },
        {
            "age": 39,
            "name": "Herman"
        },
        {
            "age": 25,
            "name": "Gates"
        }
    ]


# for i in sorted(students, key=lambda k: k['name']):
#     print(f'By name: {i};')

# for i in sorted(students, key=lambda k: k['age']):
#     print(f'By name: {i};')
#
# 2 Отсортировать список по убыванию любым понравившимся алгоритмом

# def bubble(students):
#     i = len(students) - 1
#     while i > 0:
#         j = len(students) - 1
#         while j > 0:
#             if students[j]['age'] < students[j - 1]['age']:
#                 students[j], students[j - 1] = students[j - 1], students[j]
#             j -= 1
#         i -= 1
#     return students
# for i in bubble(students):
#     print(f'By age: {i};')


def bubble(students):
    i = len(students) - 1
    while i > 0:
        j = len(students) - 1
        while j > 0:
            if students[j]['name'] < students[j - 1]['name']:
                students[j], students[j - 1] = students[j - 1], students[j]
            j -= 1
        i -= 1
    return students
for i in bubble(students):
    print(f'By name: {i};')




