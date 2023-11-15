# fibonaccy recursion
def fb_rc(n = int(input('Enter the n for fibonaccy recursion: '))):
    if n < 0:
        return f'Error'
    elif 0 <= n <= 1:
        return n
    else:
        return (fb_rc(n - 2) + fb_rc(n - 1))

print(fb_rc())