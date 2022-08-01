# recursion
# 1. hello
# 2.hello n times
# 3. sum 0 + 1 + 2 + 3 + 4 + 5 = 15
# 4. factorial 5! = 1 * 2 * 3 * 4 * 5 = 120
# 5. fibonacci 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

def hello(n):
    if n <= 0:
        return
    else:
        print(f'Hello world!')
        hello(n - 1)
hello(1)

def sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum(n - 1) # 5 + 4 + 3 + 2 + 1 = 15
print(sum(5))

def factorial(n):
    if n == 0:
        return 1
    else:
        return  n * factorial(n - 1) # 5*4*3*2*1 = 120
print(factorial(5))

def fib(n):
    if n <= 0: return 0
    elif n == 1: return 1
    else:
        return fib(n - 1) + fib(n - 2) # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
print(fib(10))
