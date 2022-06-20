# # Disney code interview dt 10 june 2022
# nums = [2,7,11,15]
# def wrkwlst(nums):
#     nlst=[]
#     nnlst=[]
#     for i in range(len(nums)):
#         if (nums[i-1] + nums[i]) == 9:
#             nlst.append(nums[i-1]), nlst.append(nums[i]),nnlst.append(i-1), nnlst.append(i)
#     return nlst, nnlst
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

# Factorial n! of integer
def fctrl(num = int(input('Enter the integer: '))):
    if num == 0:
        return f'Factorial of "{num}" = "1"'
    fctrl = 1
    for e in range(1, num + 1):
        fctrl *= e
    return f'Factorial of "{num}" = "{fctrl}"'
print(fctrl())
