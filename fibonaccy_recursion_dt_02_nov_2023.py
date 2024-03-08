# fibonaccy recursion
# 0 1 2 3 4 5 6  7  8  9  10
# 0 1 1 2 3 5 8 13 21 34  55

def fb_rc(n = int(input('Enter the n for fibonaccy recursion: '))):
    if n < 0:
        return f'Error'
    elif 0 <= n <= 1:
        return n
    else:
        return (fb_rc(n - 2) + fb_rc(n - 1))

print(fb_rc())
