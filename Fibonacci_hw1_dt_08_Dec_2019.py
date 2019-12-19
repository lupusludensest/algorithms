# TODO: Домашнее задание: Написать программу для вывода только указаного элемента последовательности

# Recursion function for nth Fibonacci number
# def fib(n):
#     if n <= 0:
#         print("Enter not zero and not negative integer.")
#         quit()
#     # member #0 is 0, member #1 is 1, member #2 is 1
#     elif n in [1, 2]:
#         return 1
#     elif n >= 3:
#         return fib(n-1) + fib(n-2)
#     else:
#         return 0
# n = int(input("Enter the number of the sequence member: "))
# result = fib(n)
# print(f'Member # {n} is : {result} .')

# Fibonacci Sequence Using For Loop
n = int(input('Enter the number of sequence member: '))
def Fibonacci(n):
    a, b = 1, 1
    list = []
    for i in range(n):
        list.append(a) #yield a
        a, b = b, a + b
    if n < 0:
       print('Enter not zero and not negative integer.')
       quit()
    elif n == 0:
        print(f'Sequence member# 0 is: {a}.')
        quit()
    return list
fibs = Fibonacci(n) #fibs = list(Fibonacci(n))
result = fibs[-1]
print(f'Sequence member# {n} is: {result}.')

# Fibonacci Sequence Using Lambda and Reduce
# from functools import reduce
# n = int(input('Enter the Number of terms: '))
# def fib(n):
#     if n < 0:
#         print('Enter not zero and not negative integer.')
#         quit()
#     return reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
# fibs = list(fib(n))
# result = fibs[-1]
# print(f'Sequence member# {n} is: {result}.')

