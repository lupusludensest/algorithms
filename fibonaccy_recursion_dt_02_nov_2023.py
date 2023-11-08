# fibonaccy recursion
def fb_rc(n):
    if 0 <= n <= 1:
        return n
    elif 1 <= n:
        return (fb_rc(n - 2) + fb_rc(n - 1))
    else:
        return f'Error'

print(fb_rc(9))