# # print out "heart" picture
# for row in range(6):
#   for col in range(7):
#     if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
#       print("*",end="   ")
#     else:
#       print(end="   ")
#   print()

# lst_1 = [-99, -77, 0, 2, 4, 44]

# def lst_evn_nm(lst_1):
#   lst_evn_nm = []
#   for i in lst_1:
#     if i % 2 == 0:
#       lst_evn_nm.append(i)
#   return lst_evn_nm
#
# print(lst_evn_nm(lst_1))

# # lambda usage with even elements in the list given
# def filter_even_numbers(numbers):
#   return list(filter(lambda x: x % 2 == 0, numbers))
#
# # Example usage
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = filter_even_numbers(numbers)
# print("Even numbers:", even_numbers)

# # input: two sorted lists
# # a - sorted list, size n
# # b - sorted list, size m
# # output: intersection of two lists a and b
# # example:
# # a = [1, 3, 4, 5, 7]
# # b = [3, 5, 6]
# # expected_output = [3, 5]
#
# def intsctn_lsts(a, b):
#     res = []
#     for i in a:
#         if i in b:
#             res.append(i)
#     return f'Intersected elements: {res}'
#
# a = [1, 3, 4, 5, 7]
# b = [3, 5, 6]
#
# run = intsctn_lsts(a, b)
# print(run)

# # Code challenge:
# # Extract the longest word from the string
#
# def lnst_wrd_str(str_a):
#     wrd = max(str_a.split(' '), key = len)
#     return wrd
#
# str_a = 'sdfg sdfg sdfg sdfg sdfdfgffgbgfdfgb sdfdfv'
# print(lnst_wrd_str(str_a))

# # swap the list. change first and last elements in the list given
#
# lst_a = list(range(0, 10, 2))
# print(lst_a)
# def swp_lst(lst_a):
#     return lst_a[::-1]
#
# print(swp_lst(lst_a))

# lst_b = list(range(-10, 10, 2))
# print(lst_b)
#
# def swp_lst(lst_b):
#     lst_b[0], lst_b[-1] = lst_b[-1], lst_b[0]
#     return lst_b
#
# print(swp_lst(lst_b))

# count chars in the string and create a new string of shape a2b3c4 if input was aabbbcccc

# str_a = 'aabbbcccc'
#
# def cnt_chrs_str(str_a):
#     res = ''
#     prev = ''
#     cnt = ''
#     for i in str_a:
#         if i != prev:
#             if len(prev) != 0:
#                 res += prev + str(cnt)
#             cnt = 1
#             prev = i
#         else:
#             cnt += 1
#     if len(prev) != 0:
#         res += prev + str(cnt)
#     return res
#
# print(cnt_chrs_str(str_a))
#
#
# def compress(s):
#     r = ""
#     c = 1
#
#     for i in range(len(s)):
#         if i == 0 or s[i] != s[i - 1]:
#             if i > 0:
#                 r += s[i - 1] + str(c)
#             c = 1
#         else:
#             c += 1
#
#     return r + s[-1] + str(c)
#
#
# print(compress('aabbbcccc'))

# # 2 list are given. create list with elements intersected
#
# lst_a = [-99, 44, 55, 6]
# lst_b = [-99, 44, 55, 6, 0, 2, 55, 66, 77, 24, 545, 665, 775]
#
# def lmnts_ntrstd(lst_a, lst_b):
#     res = []
#     for i in lst_a:
#         if i in lst_b:
#             res.append(i)
#     return res
#
# print(lmnts_ntrstd(lst_a, lst_b))

# # string given. find the longest word in string and reverse it
#
# str_a = 'ertyu ertyu sdfgh 34567 dfghgfdfghjhgfghj kjhgfdghjgfdghjgfdghjgfd'
#
# def lngst_wrd(str_a):
#     rvrsd_lngst_wrd =  max(str_a.split(), key=len)
#     return rvrsd_lngst_wrd[::-1]
#
# print(lngst_wrd(str_a))

# # find if a word is a palindrome
#
# str_a = str(input('Enter the word: '))
#
# def f_plndrm(str_a):
#     rvrsd_str_a = str_a[::-1]
#     if rvrsd_str_a == str_a:
#         return f'Palindrome'
#     return f'Not palindrome'
#
# print(f_plndrm(str_a))

# # tuple can not be changed but mutable element in the tuple can be
#
# tuple_a = (1, 'str', [1, 2, 3], (1, 2, 3))
#
# tuple_a[3].append('next')
#
# # print(tuple_a)


# # python deep and shallow copy
# import copy
# a = [1, 2, 3]
# b = copy.copy(a)
#
# b.append('ásdfghj')
#
# c = a == b
# print(c)
#
# d = a is b
# print(d)
#
# print(a)
# print(b)

# preparation for code challenge with dt 13 nov 2023, mon. From memory.
# check if a decimal integer is a palindrome
#
# int_a = int(input('Enter the decimal integer: '))
#
# def dcml_ntgr_plndrm(int_a):
#     if type(int_a) == int:
#         if ((str(int_a))[::-1] == str(int_a)) == True:
#             return f'Palindrome'
#         else:
#             return f'Not a palindrome'
#     elif type(int_a) != int:
#         return f'Enter int'
#
#
# print(dcml_ntgr_plndrm(int_a))

# import os
#
# if not os.path.isfile('text.txt'):
#
#     data = []
#
#     topic = input('Enter Topic: ')
#     series = input('Enter Series: ')
#
#     data.append(topic)
#     data.append(series)
#
#     with open('text.txt', 'w') as file:
#         file.write(topic + '\n')
#         file.write(series + '\n')
#
# else:
#     with open('text.txt', 'r') as file:
#         data = file.readlines()
#
#     topic = data[0].strip()
#     series = data[1].strip()
#
#     print(f'\nWelcome back to: {topic} {series}')

# import pickle, os
# if not os.path.isfile('pickle.dat'):
#
#     data = [0, 1]
#
#     data[0] = input('Enter Topic: ')
#     data[1] = input('Enter Series: ')
#
#     file = open('pickle.dat', 'wb')
#
#     pickle.dump(data, file)
#
#     file.close()
#
#     file = open('pickle.dat', 'rb')
#
#     data = pickle.load(file)
#     file.close()
#
#     print('\nWelcome back to: ', data[0], data[1])
#
#
# import random
# import string
#
# def generate_login():
#   password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
#   username = ''.join(random.choices(string.ascii_letters, k=8))
#   email = username + "@gmail.com"
#
#   print(f"Your login credentials are: \nEmail: {email}\nPassword: {password}")
#
# generate_login()

# 24 nov 2023, fri, practice

# # fib linear
#
# n = int(input('Enter FB SEQ number: '))
#
# def fb_ln(n):
#     if n < 0:
#         raise ValueError('n cannot be negative')
#     if 0 <= n <= 1:
#         return n
#     else:
#         a, b = 0, 1
#         for i in range(2, n + 1):
#             a, b = b, b + a
#         return b
#
# print(fb_ln(n)) # 0 1 1 2 3 5 8 13 21 34 55


# # fib lrec
#
# n = int(input('Enter FB SEQ number: '))
#
# def fb_rc(n):
#     if n < 0:
#         raise ValueError('n cannot be negative')
#     if 0 <= n <= 1:
#         return n
#     else:
#         return ((fb_rc(n - 2)) + (fb_rc(n - 1)))
#
# print(fb_rc(n)) # 0 1 1 2 3 5 8 13 21 34 55

# 27 nov 2023, mon,

# test 1

# addOrConcat(arg0, arg1):

# If Int + Int, thus Addition # 2, 3 # 5

# test 2

# addOrConcat(arg0, arg1):

# If Int + Str, thus Concat # 2 + ' Str' # "2 Str"

# test 3

# addOrConcat(arg0, arg1):

# If Str + Int, thus Concat # 'Str ' + 2 # "Str 2"


# If Str + Str, thus Concat # 'Str ' + 'Str' # "Str Str"

# Negative

# If Bool + Str, thus Concat # True + 'Str' # raise ValueError"Bool First"

# If Str + Bool, thus Concat # 'Str' + False # raise ValueError"Bool second"


# If List + Int, thus Concat # List + Int # raise ValueError"List first"

# If Set/Dict + Int, thus Concat # Set/Dict + Int # raise ValueError"Set/Dict  first"

# If RegEx + Int/Str, thus Concat # RegExt + Int/Str # raise ValueError"RegExt   first"


#
# can be           open | opening | closing | closed
#
# moving up                                     *
#
# moving down                                   *
#
# stationary        *       *          *        *
#
# button UP                                     *
#
# button down                                   *


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

# to define if an integer is a prime
# the prime number is not negative and can be divided by 1 and itself only and can not be < 2
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
# n = int(input('Enter the prime to evaluate: '))
#
# def is_prm(n):
#     if n < 2:
#         raise ValueError('The prime can not be less than 2')
#     for i in range(2, n):
#         if n % i == 0:
#             return f"Not a prime"
#     else:
#         return f"The prime"
#
#
# print(is_prm(n))

# python data types
# primitive & complex
# primitive: integers, floats, strings, booleans, complex
# complex: list, dictionares, sets, tuples, frozenset
# mutable & unmutable
# mutable: list, dictionary, set,
# unmutable: integers, floats, bbolean, strings, unicode, tuple

# Is Python a Case-Sensitive Language?
# YES, Python is a case-sensitive programming language.

# How Python interpreted?
# 1 Source code
# 2 Intermediate language
# 3 Native
# 4 Executive

# Is list an ordered in Python?
# Dictionary is an unordered collection of data values that stores data values like a map.

# What are unordered datatypes in Python?
# A set is an unordered collection of items. Every set element is exclusive
# (no duplicates) and must be immutable (cannot be changed).

# As the set is an unordered collection, indexing will be meaningless.
#  Dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# Lists are ordered, which means they retain the order in which you insert the elements
# into the list.

# What is a list comprehension?
# The ability of creation of list in one line of the code.

# What kid of operators fo you know in Python?
# /; *; **, =; ==; //; %

# What are the operators and operands in Python?
# 2 + 2 => 2 - operands; + - operator

# What is the difference between shallow nd deep copy in Python?
# Shallow copy is being made if changed-changes the original too.
# Deep copy is independed from the original and is being made if changed-does not change
# the original.


# given a list of the integers every is less 10. return the whole integer with the last digit with added 1.
# and if the last digit is 9 it has to be 0. I.e. list1 = [1, 2, 3] => 124, list2 = [1, 2, 4] => 125,
# list3 = [1, 2, 9, 9, 9, 9] => 129990

# list1 = [1, 2, 3]
# list2 = [1, 2, 4]
# list3 = [1, 2, 9, 9, 9, 9]
# def mass_plus(a):
#     if a[-1] != 9:
#         a[-1] += 1
#         s = []
#         for i in range(len(a)):
#             s.append(str(a[i]))
#             res = int("".join(s))
#         return res
#     else:
#         a[-1] = 0
#         s = []
#         for i in range(len(a)):
#             s.append(str(a[i]))
#             res = int("".join(s))
#         return res
#
#         return res
#
# a = list1
# print(mass_plus(a))
#
# a = list2
# print(mass_plus(a))
#
# a = list3
# print(mass_plus(a))

# 04 dec 2023, practice

# # Function. We have a string 'I'm a Ptthon specialist'. Write a function that will reverse the string given.
#
# a = "I'm a Python specialist"
# #  "I'm a Python specialist"
# #   0123456789 10
#
# def rev_st(a):
#     return a[::-1] # slicing start/stop/step
#
# print(rev_st(a), type(a[::-1]))

# def reverse_string(input_str):
#     reversed_str = "" # empty str is declared
#     index = len(input_str) - 1 # index variable is declared
#     while index >= 0:
#         reversed_str += input_str[index]
#         index -= 1
#     return reversed_str
#
#
# input_str = "I'm a Python specialist"
# print(reverse_string(input_str))

# Define if a string is a palyndrome

# a = str(input('Enter the word: '))

# def if_plndrm(a):
#     if a == (a[::-1]):
#         return True
#     raise ValueError('Err')
#
# print(if_plndrm(a))

# We have a two different string 'Wsdfgh' and 'Kjhgfdsdfg'. Write a function to concatenate the not usin "+".
# Use a ' ' between them.

# a = 'Wsdfgh'
# b = ' Kjhgfdsdfg'
# c = ' '
#
# def nct_strns(a, b, c):
#     return f'{a}{c}{b}'
#
# print(nct_strns(a, b, c))

# a = 'Wsdfgh'
# b = ' Kjhgfdsdfg'
# c = ' '
#
# def nct_strns(a, b, c):
#     return '{}{}{}'.format(a, b, c)
#
# print(nct_strns(a, b, c))

# Given string by user. "()[]{}". If "(]", if "([)]" false.
#
# a = input('Enter the string: ')
# def check_brackets(a):
#     bopen = ['(', '[', '{']
#     bclose = [')', ']', '}']
#     stack = []
#
#     for char in a:
#         if char in bopen:
#             stack.append(char)
#         elif char in bclose:
#             pos = bclose.index(char)
#             if ((len(stack) > 0) and (bopen[pos] == stack[len(stack) - 1])):
#                 stack.pop()
#             else:
#                 return False
#
#     if len(stack) == 0:
#         return True
#     else:
#         return False
#
# print(check_brackets(a))

# s = input("Enter the word: ")
# def isValid(s):
#     stack = []
#     for char in s:
#         if char in ['(', '[', '{']:
#             stack.append(char)
#         elif char == ')':
#             if not stack or stack[-1] != '(':
#                 return False
#             stack.pop()
#         elif char == ']':
#             if not stack or stack[-1] != '[':
#                 return False
#             stack.pop()
#         elif char == '}':
#             if not stack or stack[-1] != '{':
#                 return False
#             stack.pop()
#
#     return not stack
#
# print(isValid(s))

# We have a string give. We need to count each char in the string. And return a string where 'a2b3'.

# a = str(input('Enter the string: ')) # abc
# def count_chars(a):
#     res = ""
#     prev_char = ""
#     char_count = 0
#
#     for char in a:
#         if char != prev_char:
#             if len(prev_char) > 0:
#                 res += prev_char + str(char_count)
#             char_count = 1
#             prev_char = char
#         else:
#             char_count += 1
#
#     res += prev_char + str(char_count)
#     return res
#
# print(count_chars(a))

# # Given integer. Define if it is odd or even and is it negative or positive.
#
# a = int(input('Enter the integer: '))
#
# def if_int_odd_even_pos_neg(a):
#     if a == 0:
#         return f'{a} is just a zero-not even/add and not pos/neg'
#     elif a < 0 and a % 2 == 0:
#         return f'{a} is negative and even' # -2
#     elif a < 0 and a % 2 != 0:
#         return f'{a} is negative and odd' # -3
#     elif a > 0 and a % 2 == 0:
#         return f'{a} is positive and even' # 4
#     elif a > 0 and a % 2 != 0:
#         return f'{a} is positive and odd' # 7
#     else:
#         raise ValueError('Err')
#
# print(if_int_odd_even_pos_neg(a))


import re

str_a = str(input('Enter the word: '))


def f_plndrm(str_a):
    # Remove non-alphanumeric characters
    str_a = re.sub(r'[\W_]+', '', str_a)

    # Decapitalize
    str_a = str_a.lower()

    # Reverse string
    rvrsd_str_a = str_a[::-1]

    if rvrsd_str_a == str_a:
        return f'Palindrome'
    return f'Not palindrome'


print(f_plndrm(str_a))















