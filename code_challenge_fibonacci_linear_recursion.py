
# # fib recursion
# n = int(input('Enter the n: '))
# def fb_rc(n):
#     if 0 <= n <= 1:
#         return n
#     elif 0 > n:
#         return 'Error'
#     else:
#         return fb_rc(n - 2) + fb_rc(n - 1)
#
# print(fb_rc(n))

# fib linear
n = int(input('Enter n: '))
def fb_ln(n):
    if 0 <= n <= 1:
        return n
    elif 0 > n:
        return f'Error'
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

print(fb_ln(n))
