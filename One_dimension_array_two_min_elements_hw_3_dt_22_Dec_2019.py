# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint

length = int(input(f'Enter the length of the array: '))
if length < 2:
    print(f'Invalid Input. Enter at least 2.')
    quit()
x = int(input(f'Enter the MIN element of the array: '))
y = int(input(f'Enter the MAX element of the array: '))
array = []

for i in range(length):
    item = randint(x, y)
    array.append(item)

length = len(array)
min_element_first = min(array)

k = min_element_first
min_element_second = 99999999999999999999
for i in array:
    if min_element_second > i and i > k :
        min_element_second = i

print(f'\nArray: {array}.'
    f'\nFirst MIN element is: {min_element_first}.'
    f'\nSecond MIN element is: {min_element_second}.')
