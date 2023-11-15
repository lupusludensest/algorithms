# code that defines the effectiveness of code bugs based on execution time
from fibonaccy_straight_dt_02_nov_2023 import *
from fibonaccy_recursion_dt_02_nov_2023 import *
import time

# count and comparing the execution times of both functions
start = time.time()
fb_str() # 1 call func from fibonaccy_straight_dt_02_nov_2023.py
end = time.time()
time_fb_str = end - start

start = time.time()
fb_rc() # 2 call func from fibonaccy_recursion_dt_02_nov_2023.py
end = time.time()
time_fb_rc = end - start

# n = 16, 17, 18 and is a treshold when fb_str 1 is more effective
if time_fb_str < time_fb_rc:
    print(f"fb_str is more effective\nfb_str time: {time_fb_str}\nfb_rc: {time_fb_rc}")
elif time_fb_rc < time_fb_str:
    print(f"fb_rc is more effective\nfb_str time: {time_fb_str}\nfb_rc: {time_fb_rc}")
else:
    print(f"Both variants are equally effective\nfb_str time: {time_fb_str}\nfb_rc: {time_fb_rc}")

