# fib yield
# 0 1 2 3 4 5 6 7 8 9 10
# 0 1 1 2 3 5 8 13 21 34 55
def next_number():
    a1, a2 = 0, 1
    # while True:
    for i in range(1, n + 1):
        a1, a2 = a2, a1 + a2
        yield a2

f = next_number()
n = int(input('Enter the number of fib member: '))
for _ in range(n):
    print(next(f))