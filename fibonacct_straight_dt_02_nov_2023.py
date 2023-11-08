# fibonaccy straignt

def fb_str(n):
    if n < 0:
        return f'Error'
    elif 0 <= n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b

print(fb_str(9))