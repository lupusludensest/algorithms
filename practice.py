# # print out "heart" picture
# for row in range(6):
#   for col in range(7):
#     if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
#       print("*",end="   ")
#     else:
#       print(end="   ")
#   print()
import heapq


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

# # linear fib
#
# n = int(input('Enter the Fib seq number: '))
#
# def fb_ln(n):
#     if n < 0:
#         raise ValueError('Err')
#     elif 0 <= n < 2:
#         return n
#     a, b = 0, 1
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     return b
#
# print(fb_ln(n))

# fib recursion

# n = int(input('Enter the Fib seq number: '))
# def fb_rc(n):
#     if n < 0:
#         raise ValueError('Err')
#     elif 0 <= n < 2:
#         return n
#     return ((fb_rc(n - 2)) + (fb_rc(n - 1)))
#
# print(fb_rc(n))

# tesla interview code challenge
# rearrange string. given a string s. rearrange the characters of s so that any two adjacent characters are not the same.
# or return "" if not possible. example 1 input: s = "aab", output = "aba". example 2 input: s = "aaab", output = "".

# from collections import Counter
#
# def rearrange_string(s: str) -> str:
#   """
#   Rearranges the characters in a string so that no two adjacent characters are the same.
#
#   Args:
#     s: The string to rearrange.
#
#   Returns:
#     The rearranged string, or an empty string if it is not possible.
#   """
#   count = Counter(s)
#   max_heap = [(-cnt, char) for char, cnt in count.items()]
#   heapq.heapify(max_heap)
#
#   prev, res = None, ""
#   while max_heap:
#     cnt, char = heapq.heappop(max_heap)
#     res += char
#
#     if prev and prev[1] != char and count[prev[1]] > 0:
#       heapq.heappush(max_heap, prev)
#
#     if cnt < -1:
#       prev = (cnt + 1, char)
#     else:
#       prev = None
#
#   return res if len(res) == len(s) else ""
#
# # Example usage
# s = "aabdd"
# print(rearrange_string(s)) # Output: aba

# convert string to number

# n = str(input('Enter the float: '))
#
# def cnv_t_num(n):
#     try:
#         float(n)
#     except ValueError:
#         return f'Wrong input'
#
#     return round(float(n), 2), type(n)
#
# print(cnv_t_num(n))

# list given. return True if duplicates, return False if not

# l = [-9, 4, -5, 0, 44, 44]
#
# def dplcts(l):
#     if len(l) == len(set(l)):
#         return False
#     return True
#
#
# print(dplcts(l))

# given list and a target with the sum of some two elements of the list. find indexes of those
# elements which give a sum in target

# s = [4, 3, 5, 1, 8, 7]
# t = 10
# def sumt(s, t):
#     d_i_c = {} # dict is pair of keys & values
#     for i in range(len(s)): # start stop step
#         r = t - s[i]
#         if s[i] in d_i_c:
#             return d_i_c[s[i]], i
#         else:
#             d_i_c[r] = i
#     return None, None
#
# print(sumt(s,t)) # time complexity O(n) because only one for loop # space complexity O(n)
# # because only one for loop

# binary search. list sorted given. given target number. find the index of target in the list. if not
# found return -1

# l = [-9, 4, -6, 0, 5, 4, 2, 8]
# t = 5
#
# def fnd_ndx_trg(l, t):
#     s_l = sorted(l)
#     print(s_l)
#     for i in range(len(l)):
#         mdl_el =
#         if l[i] == t:
#             return i
#     return "-1"
#
# print(fnd_ndx_trg(l, t))

# def binary_search(nums, target):
#     """
#     This function finds the index of a target in a sorted list using binary search.
#
#     Args:
#       nums: A list of sorted integers.
#       target: The target integer to search for.
#
#     Returns:
#       The index of the target if it is found, otherwise -1.
#     """
#     left = 0 # pointer not counter
#     right = len(nums) - 1
#
#     while left <= right:
#         middle = (left + right) // 2 # floor division
#
#         if nums[middle] == target: # this is only working part of the code
#             return middle
#
#         if nums[middle] > target:
#             right = middle - 1 # right variable moves to left on one step from the middle
#
#         else:
#             left = middle + 1 # left variable moves to right on one step to the middle
#
#     return -1
#
# # Example usage
# nums = [1, 3, 7, 8, 9, 10, 18]
# target = 7
# print(binary_search(nums, target))

# given list and a target with the sum of some two elements of the list. find indexes of those
# elements which give a sum in target
# via dict

# l = [1, 3, 7, 8, 9, 10, 18]
# t = 10
#
# def fnd_tw_indxs(l, t):
#     res = {}
#     for i, num in enumerate(l):
#         dif = t - num
#         if dif in res:
#             return res[dif], i
#         else:
#             res[num] = i
#     return None, None
#
# print(fnd_tw_indxs(l, t))

# given a list and a target which is a sum of two elements of tge list. find tge indexes of those elements.
# if not return None, None


# l = [1, 3, 7, 8, 9, 10, 18]
# t = 28
#
# def fnd_tw_indxs(l, t):
#     l.sort()
#     left = 0
#     right = len(l) - 1
#     while left < right:
#         sm = l[left] + l[right]
#         if sm == t:
#             return left, right
#         elif sm < t:
#             left += 1
#         elif sm > t:
#             right -= 1
#     return None, None
#
# print(fnd_tw_indxs(l, t))
# print(sorted(l))

# find indexes of two list elements which to be added are equal to some target
# l = [9, 2, 3, 5, 7], t = 7
# via dictionary

# l = [9, 2, 3, 5, 7]
# t = 5

# def fn_indxs_tr(l, t):
#     res = {}
#     for i, num in enumerate(l):
#         df = t - num
#         if df in res:
#             return res[df], i
#         else:
#             res[num] = i
#     return None, None
# print(fn_indxs_tr(l, t))

# via sort and two pointers
# def fnd_indxs_tr(l, t):
#     l.sort()
#     lf = 0
#     rg = len(l) - 1
#     while lf < rg:
#         sm = l[lf] + l[rg]
#         if sm == t:
#             return lf, rg
#         elif sm < t:
#             lf += 1
#         elif sm > t:
#             rg -= 1
#     return None, None
#
# print(fnd_indxs_tr(l, t))
# print(sorted(l))

# if the phrase is a palyndrome return True. if not return False

# phrs = 'A man, a plan, a canal: Panama'

# def if_phr_pal(phrs):
#     res = ""
#     for i in phrs.lower():
#         if i.isalnum():
#             res+=i
#     if res == res[::-1]:
#         return f'Pal'
#     else:
#         return f'Not pal'
#
# print(if_phr_pal(phrs))

# find indexes of two list elements which to be added are equal to some target
# l = [9, 2, 3, 5, 7], t = 7
# via dictionary

# l = [9, 2, 3, 5, 7]
# t = 16
#
# # t_list = []
# for i in l:
#     i_index = l.index(i)
#     # print(f'{i} + #print(i) + {i_index} + #i_index')
#     '''
#     Логика:
#     ok 1. Выявить индекс каждого числа из листа
#     ok 2. Взять число (i) с индексом 0 второй раз пробежаться по массиву (j)
#     ok 2.1. Выявить индексы (j)
#     ok 3. Сравнить индекс (i.index) != (j.index) => sum
#     4. Если sum = "t" => print(t)
#     '''
#
#     for j in l:
#         j_index = l.index(j)
#         # print(f'{j} + #print(j) + {j_index} + #j_index')
#         if i_index != j_index:
#             sum = i + j
#             # print(f'{sum} + #print(sum)')
#             if sum == t:
#                 # print(f'{sum} + #то что мы искали = сумма чисел = цели')
#                 # print(f'{i} + {j} = {sum}')
#                 # print(f'Индекс числа {i} = {i_index} + индекс числа {j} = {j_index} = цели {sum}')
#                 print(f'{i_index} + {j_index} = цели {sum}')
#             #     print(f'{i_index} {j_index}')

# find indexes of two list elements which to be added are equal to some target
# l = [9, 2, 3, 5, 7], t = 5
# via dictionary

# l = [9, 2, 3, 5, 7]
# t = 8
#
# def fnd_indxs_tw_el(l, t):
#     res = {}
#     for i, j in enumerate(l):
#         df = t - j
#         if df in res:
#             return res[df], i
#         else:
#             res[j] = i
#     return f'None'
#
# print(fnd_indxs_tw_el(l, t))

# via sort & two pointers

# l = [9, 2, 3, 5, 7]
# t = 7
#
# def fnd_tw_indxs(l, t):
#     lf = 0
#     rg = len(l) - 1
#     l.sort()
#     while lf < rg:
#         sm = l[lf] + l[rg]
#         if sm == t:
#             return lf, rg
#         elif sm < t:
#             lf += 1
#         elif sm > t:
#             rg -= 1
#     return None, None
#
# print(fnd_tw_indxs(l, t))
# print(sorted(l))

# Array reverse. Write a method that will take an array as an argument and reverse it.
# - Reversing an array involves rearranging its elements so
# that the first element becomes the last and the last becomes the first.
# - This task is a fundamental operation in array manipulation and tests the
# understanding of array data structures.

# lst = [1, 3, 5, 7, 9]
# def lst_rev(lst):
#     return lst[::-1]
#
# print(lst_rev(lst))

# lst = [1, 3, 5, 7, 9]
# def lst_rev_nxt(lst):
#     lst_rev_nxt = []
#     for i in range(len(lst) - 1, -1, -1): # start, stop, step
#         lst_rev_nxt.append(lst[i])
#     return lst_rev_nxt
#
# print(lst_rev_nxt(lst))

# lst = [1, 3, 5, 7, 9]
# def lst_rev_one_more(lst):
#     return list(reversed(lst)), type(reversed(lst)), type(lst)
#
# print(lst_rev_one_more(lst))

# check if an array contains any duplicates.
# Your function should accept an array of integers as input.
# - It should return **`true`** if any value appears at least
# twice in the array, and **`false`** otherwise.

# lst = [1, 3, 5, -1, 9, -5, 55, 7]
# def fnd_dplcts(lst):
#     st_lst = list(set(lst))
#     if sorted(st_lst) == sorted(lst):
#         return False
#     else:
#         return True
#
# print(fnd_dplcts(lst))

# tpl = (1, 2.3, 'rty', False, [1, 2.3, 'fgh'], (1, 2.3, 'rty', False))
# print(tpl, type(tpl))

# dct_1 = {'num':1, 'name':'Petya', 'age': 99}
# print(dct_1, type(dct_1))

# dct_1 = {'num':1, 'name':'Petya', 'age': 99, 'num':1, 'name':'Petya', 'age': 99}
# set_1 = set(dct_1)
# print(set_1, type(set_1))

# lst_1 = {1, 3, 5, -1, 9, -5, 55, 7, 1, 3, 5, -1, 9, -5, 55, 7}
# set_1 = set(lst_1)
# print(lst_1, type(lst_1))

# ternary operator
# x = int(input('Enter the integer: '))
#
# def trn_prt(x):
#     answer = 'pos' if x > 0 else 'neg'
#     return answer
#
# print(trn_prt(x))

# find sum of all positive elements in list
#
# l = [-99, 9, -4, -3, 0, -3, -4, -6, -8, 1]
#
# def sm_lmnts_lst(l):
#     res = []
#     for i in l:
#         if i > 0:
#             res.append(i)
#
#     return sum(res)
#
# print(sm_lmnts_lst(l))

# find indexes of two list elements which to be added are equal to some target
# l = [9, 2, 3, 5, 7], t = 5

# l = [9, 2, 3, 5, 7]
# t = 5
#
# # via sort and two pointers
# def fnd_indxs_tr(l, t):
#     l.sort()
#     lf = 0
#     rg = len(l) - 1
#     while lf < rg:
#         sm = l[lf] + l[rg]
#         if sm == t:
#             return lf, rg
#         elif sm < t:
#             lf += 1
#         elif sm > t:
#             rg -= 1
#     return None, None
#
# print(fnd_indxs_tr(l, t))
# print(sorted(l))

# swap the list of integers by two pointers

# lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
#
# def tw_pntrs(lst):
#   lf_pntr = 0
#   rt_pntr = len(lst) - 1
#
#   while lf_pntr < rt_pntr:
#     lst[lf_pntr], lst[rt_pntr] = lst[rt_pntr], lst[lf_pntr]
#     lf_pntr += 1
#     rt_pntr -= 1
#
#   return lst
#
# print(tw_pntrs(lst))

# # if phrase has all alphabet letters
#
# my_string = "qwertyuioplkjhgfdsazxc" #vbnm"
# def pangram(my_string): # O(n)
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
#     for letter in alphabet:
#         if letter not in my_string:
#             return False
#     return True
#
# print(pangram(my_string))

# # fib recursion
# # 0 1 2 3 4 5 6 7 8 9 10
# # 0 1 1 2 3 5 8 13 21 34 55
#
# n = int(input('Enter the number of fob seq element: '))
# def fb_rec(n):
#     if n < 0:
#         return "Err"
#     elif 0 <= n <= 1:
#         return n
#     return(fb_rec(n - 2) + fb_rec(n - 1))
#
# print(fb_rec(n))

# # fib linear
# # 0 1 2 3 4 5 6 7 8 9 10
# # 0 1 1 2 3 5 8 13 21 34 55
#
# n = int(input('Enter the number of fib member: '))
# def fb_lin(n) -> int:
#     if n < 0:
#         raise ValueError
#     elif 0 < n < 1:
#         return n
#     else:
#         a = 0
#         b = 1
#         for i in range(1, n):
#             a, b = b, a + b
#         return b
#
# print(fb_lin(n))
















