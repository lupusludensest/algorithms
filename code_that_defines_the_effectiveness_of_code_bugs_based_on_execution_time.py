# code that defines the effectiveness of code bugs based on execution time
import time
# 1
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
# 2
def fb_rc(n):
    if 0 <= n <= 1:
        return n
    elif 1 <= n:
        return (fb_rc(n - 2) + fb_rc(n - 1))
    else:
        return f'Error'

# data for input
n = int(input('Enter the n for fibonaccy: '))

start = time.time()
fb_str(n)
end = time.time()
time1 = end - start

start = time.time()
fb_rc(n)
end = time.time()
time2 = end - start

# n = 16, 17, 18 and is a treshold when fb_str 1 is more effective
if time1 < time2:
    print(f"fb_str 1 is more effective\nfb_str time: {time1}\nfb_rc: {time2}")
elif time2 < time1:
    print(f"fb_rc 2 is more effective\nfb_str time: {time1}\nfb_rc: {time2}")
else:
    print(f"Both variants are equally effective\nfb_str time: {time1}\nfb_rc: {time2}")