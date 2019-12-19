# Найти максимальное число из трех. Вводятся три целых числа. Определить какое из них наибольшее.
# 1-й вариант:
a = int(input(f'Enter the first integer : '))
b = int(input(f'Enter the second integer : '))
c = int(input(f'Enter the third integer : '))

max = a
if max < b:
    max = b
if max < c:
    max = c

print(f'Max integer from {a}, {b}, and {c} is: {max}.')

# 2-й вариант:
# a = int(input(f'Enter the first integer : '))
# b = int(input(f'Enter the second integer : '))
# c = int(input(f'Enter the third integer : '))
# if a > b and a > c:
#   print(f'Max integer from {a}, {b}, and {c} is: {a}.')
# elif b > c and b > a:
#   print(f'Max integer from {a}, {b}, and {c} is: {b}.')
# else:
#   print(f'Max integer from {a}, {b}, and {c} is: {c}.')