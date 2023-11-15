# fibonaccy straignt

def fb_str(n = int(input('Enter the n for fibonaccy straight: '))):
    if n < 0:
        return f'Error'
    elif 0 <= n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

print(fb_str())