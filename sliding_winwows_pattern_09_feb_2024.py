# The sliding window pattern in programming is like having a small, movable "window" on an array or a string.
# Imagine you('re looking through a tiny window that only shows a few elements of a long list at a time.
# You slide this window along the list to examine different parts.
# This technique is handy when you need to keep track of a subset of elements,
# like finding the maximum sum of any continuous subarray of a certain size. The "window" of a
# fixed size moves from the start of the array to the end, updating the required information as it goes,
# making the process efficient and fast.)
# https://yuliahar.notion.site/Whiteboard-Coding-Marathon-2-0-3030f7bbd2904b3193f675e094f3842a#64dc8bb7ba474449b5fccc397ff2ebc1

nums = [1, 12, -5, -6, 50, 3]
k = 4
from typing import List
def mx_vrg_sblst(nums: List[int], k: int) -> int:
    sm_mx = curr_sum = sum(nums[0:k])
    for i in range(1, len(nums) - k + 1):
        curr_sum = curr_sum - nums[i - 1] + nums[i + k - 1]
        if curr_sum > sm_mx:
            sm_mx = curr_sum
    return sm_mx / k

print(mx_vrg_sblst(nums, k))