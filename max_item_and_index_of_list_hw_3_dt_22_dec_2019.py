# Заполнить одномерный массив случайными числами.
# Найти и вывести на экран наибольший его элемент и порядковый номер этого элемента.

from random import randint

length = int(input(f'Enter the length of the array: '))
x = int(input(f'Enter the MIN element of the array: '))
y = int(input(f'Enter the MAX element of the array: '))
array = []

for i in range(length):
    item = randint(x, y)
    array.append(item)

print(f'Random array is: {array}.')

def find_max_item_and_its_index_in_list(array):
    index = 1
    max_index = 0
    max = array[0]
    while index < len(array):
        if array[index] > max:
            max_index = index
            max = array[index]
        index += 1
    return {
        "Max value": max,
        "Max index": max_index
    }

print(find_max_item_and_its_index_in_list(array))