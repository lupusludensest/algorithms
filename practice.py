# # Disney code interview dt 10 june 2022
# nums = [2,7,11,15]
# def wrkwlst(nums):
#     nlst=[]
#     nnlst=[]
#     for i in range(len(nums)):
#         if (nums[i-1] + nums[i]) == 9:
#             nlst.append(nums[i-1]), nlst.append(nums[i]),nnlst.append(i-1), nnlst.append(i)
#     return f'Elements: \t{nlst}\nIndexes: \t{nnlst}'
# print(wrkwlst(nums))

# # Decimal to binary
# dec = int(input('Input decimal: '))
# bnr=''
# while dec > 0:
#     bnr += str(dec % 2)
#     dec = dec // 2
# bnr = bnr[::-1]
# print(bnr)

# # Count even and odd number in the integer
# def cntevod(num = int(input('Énter the integer: '))):
#     print(f'You entered integer: {num}')
#     lsnm = list(map(int, str(num)))
#     print(f'We have a list {lsnm}, {type(lsnm)}')
#     ev = []
#     od = []
#     for e in lsnm:
#         if e % 2 == 0:
#             ev.append(e)
#         else:
#             od.append(e)
#     return f'Ev: {len(ev)} = {ev}\nOd: {len(od)} = {od}'
# print(cntevod())

# # Count char in the string
# st = str(input('Enter the string: '))
# print(f'You entered the string: {st}')
# ch = str(input('Enter the char to count the char in string: '))
# print(f'You have {ch} to count in the string')
# def cntchr(st, ch):
#     cntr = 0
#     for e in st:
#         if e == ch:
#             cntr += 1
#         else:
#             cntr += 0
#     return f'We have "{ch}" repeated "{cntr}" times'
# print(cntchr(st, ch))

# # Factorial n! of integer
# def fctrl(num = int(input('Enter the integer: '))):
#     if num == 0:
#         return f'Factorial of "{num}" = "1"'
#     fctrl = 1
#     for e in range(1, num + 1):
#         fctrl *= e
#     return f'Factorial of "{num}" = "{fctrl}"'
# print(fctrl())

# answers = ['A', 'B', '', 'D']
# for answer in answers:
#     if answer == '':
#         print('Incomlete')
#         break
#     print(answer)
# print('Loop is done')

# list1 = [1, 2, 3, 4, 5]
# def fnd_n_lst(list1):
#     ev = []
#     od = []
#     for i in list1:
#         if i % 2 == 0:
#             ev.append(i)
#         else:
#             od.append(i)
#     return f'Even: {ev}, total: {len(ev)},\nOdd:{od}, total: {len(od)}'
#
# print(fnd_n_lst(list1))


# # Iterate as an elements
# lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# def itrsel():
#     i = []
#     for e in lst1:
#         i.append(e)
#     return i, type(i)
# print(itrsel())

# # Iterate as indexes
# lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# def itrsin():
#     i = []
#     for e in range(0, len(lst2)):
#         i.append(e)
#     return i, type(i)
# print(itrsin())

# print(f'1\n')
#
# chars = "abcdefghijklmnopqrstuvwxyz"
# check_string = "aaaabbbccdddd"
#
# for char in chars:
#     count = check_string.count(char)
#     if count > 0:
#         print(str(count) + char, end='')
#
# print(f'2\n')
#
# from collections import Counter
#
# i = 'aaaabbbccdddd'
# count = Counter(i)
# print(''.join(list(map(lambda b: str(count[b]) + b, count))))
#
# print(f'3\n')
#
# input = 'aaaabbbccdddd'
# def cntchrs(input):
#     a = b = c = d = 0
#     for e in input:
#         if e == 'a':
#             a += 1
#         elif e == 'b':
#             b += 1
#         elif e == 'c':
#             c += 1
#         else:
#             d += 1
#     return f'{a}{e}{b}{e}{c}{e}{d}{e}'
#
# print(cntchrs(input))
#
# print(f'4\n')
#
# i = 'aaaabbbccdddd'
# def cntchrs(input):
#     res = ''
#     for e in i:
#         if i.count(e) > 0:
#             res.join(str(i.count(e)) + e)
#     return res
#
# print(cntchrs(i))

input = 'aaaabbbccdddd'
# expected output is: output = '4a3b2c4b'
def cntltrs(input):
    output = []
    for i in input:
        if input.count(i) != 0:
            output.append(str(input.count(i)) + i)
    return f'{output}'
print(cntltrs(input))