# Дан лист. Вернуть лист, состоящий из элементов,
# которые меньше среднего арифметического исходного листа.
# С.а. = сумма элементов разделить на количество.

from random import randint
import numpy as np

length = int(input(f'Enter the length of the list: '))
x = int(input(f'Enter the MIN element of the list: '))
y = int(input(f'Enter the MAX element of the list: '))
array = []

for i in range(length):
    item = randint(x, y)
    array.append(item)

array_sum = np.sum(array)
length = len(array)
array_average = round(float(array_sum/ (length)), 2)
percent = float(round(array_average / array_sum * 100, 2))
array_less_than_average_value_of_primary_list = []
for x in array:
    if x < array_average:
        array_less_than_average_value_of_primary_list.append(x)


print(f'Random primary list is: {array}.'
      f'\nLenght: {length}.'
      f'\nAverage of list members is: {array_average}.'
      f'\nSum of primary list elements: {array_sum}.'
      f'\nPercent- average from sum of primary list: {percent}%.'
      f'\nNew list: {array_less_than_average_value_of_primary_list}.')

