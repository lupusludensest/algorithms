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

