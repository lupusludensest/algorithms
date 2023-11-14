# code that defines the effectiveness of code bugs based on execution time
from fibonaccy_straight_dt_02_nov_2023 import *
from fibonaccy_recursion_dt_02_nov_2023 import *
import time

# 1 call func from fibonaccy_straight_dt_02_nov_2023.py
fb_str()

# 2 call func from fibonaccy_recursion_dt_02_nov_2023.py
fb_rc()

# count and comparing the execution times of both functions
start = time.time()
fb_str()
end = time.time()
time1 = end - start

start = time.time()
fb_rc()
end = time.time()
time2 = end - start

# n = 16, 17, 18 and is a treshold when fb_str 1 is more effective
if time1 < time2:
    print(f"fb_str 1 is more effective\nfb_str time: {time1}\nfb_rc: {time2}")
elif time2 < time1:
    print(f"fb_rc 2 is more effective\nfb_str time: {time1}\nfb_rc: {time2}")
else:
    print(f"Both variants are equally effective\nfb_str time: {time1}\nfb_rc: {time2}")