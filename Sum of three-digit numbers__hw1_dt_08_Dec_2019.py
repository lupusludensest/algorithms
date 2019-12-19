# Сложность O(1)
# TODO: Домашнее задание: Написать программу для числа из любого количества цифр.
#  Вместо числа из 3 цифр, нужно считать сумму числа из n цифр.
#  Где  n вводит пользователь с клавиатуры. Только положительные.

# n = int(input(f'Enter the integer : '))
# if n <= 0:
#     print(f'Enter not negative integer and not zero.')
#
# one = (n % 10)
# ten = (n // 10 % 10)
# hundred = (n // 10**2 % 10)
# thousand = (n // 10**3 % 10)
# ten_thousand = (n // 10**4 % 10)
# hundred_thousand = (n // 10**5 % 10)
# million = (n // 10**6 % 10)
# ten_million = (n // 10**7 % 10)
# hundred_million = (n // 10**8 % 10)
# billion = (n // 10**9 % 10)
# ten_billion = (n // 10**10 % 10)
# hundred_billion = (n // 10**11 % 10)
# trillion = (n // 10**12 % 10)
#
# result = trillion + hundred_billion + ten_billion + billion + hundred_million + ten_million + million + one + ten + hundred + thousand + ten_thousand + hundred_thousand
# print(f'Integer you entered is: {n}.')
# print(f'Sum of integer digits is: {result}.')
# print(f'{trillion}: {hundred_billion}: {ten_billion}: {billion}: {hundred_million}: {ten_million}: {million}: {hundred_thousand}: {ten_thousand}: {thousand}: {hundred}: {ten}: {one}')


#
# Given even number. Find sum of its digits.
# If returned not number, return 'Are the nerdy geek?'


# If some_digit == 23
#     return 5
#
# If some_digit == 42
#     return 6
#
# If some_digit == 1321564497
#     return 42
#
# If some_digit == {'key': 'value'}
#     return "Are you the nerdy geek?"

some_digit = input("Enter the number: ")

def sum_of_digits(some_number):
    try:
        number_of_digits = len(str(some_number))
        result = 0
        for digit in range(number_of_digits):
            result += int(str(some_digit)[digit])
        return result
    except ValueError:
        return 'Are you the nerdy geek?'

print('Sum of digits: ', sum_of_digits(some_digit))
print('Quantity of symbols: ', len(str(some_digit)))

"""
Given integer some_digit. Return MAX number containing
exactly some_digit digits"""

# If some_digit == 4
#     return 9999
#
# If some_digit == 7
#     return 9999999
#
# If some_digit == 1
#     return 9

# def largest_number(some_digit):
#     return 10 ** some_digit - 1
#
# some_digit = int(input("Enter the number: "))
#
# print('Largest number is: ', largest_number(some_digit), '.')
# print('Lenght of the number is: ', len(str(10 ** some_digit - 1)), '.')



