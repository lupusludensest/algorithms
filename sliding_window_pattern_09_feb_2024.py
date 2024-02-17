# The sliding window pattern in programming is like having a small, movable "window" on an array or a string.
# Imagine you're looking through a tiny window that only shows a few elements of a long list at a time.
# You slide this window along the list to examine different parts.
# This technique is handy when you need to keep track of a subset of elements,
# like finding the maximum sum of any continuous subarray of a certain size. The "window" of a
# fixed size moves from the start of the array to the end, updating the required information as it goes,
# making the process efficient and fast.)
# https://yuliahar.notion.site/Whiteboard-Coding-Marathon-2-0-3030f7bbd2904b3193f675e094f3842a#64dc8bb7ba474449b5fccc397ff2ebc1

nums = [1, 12, -5, -6, 50, 3]
k = 4

nums_1 = [1, -6, -5, 12, 50, 3]
k_1 = 4

from typing import List
def mx_vrg_sblst(nums: List[int], k: int) -> int:
    sum_max = curr_sum = sum(nums[0:k])
    for i in range(1, (len(nums) - k) + 1): # 1 - index of 12, (len(nums) - k) + 1 = 6 - 4 + 1 = 3
        curr_sum = curr_sum - nums[i - 1] + nums[i + k - 1] # 2 - 1 + 50 = 51 # 2 - 1 + 50 = 51 # 51 - (-6) + 3 = 60
        # 60 - (-5) + None = 65 or Fail
        if curr_sum > sum_max: # 51 > 2; 51 / 4 = 12.75
            sum_max = curr_sum
    return sum_max / k

print(mx_vrg_sblst(nums, k))
print(mx_vrg_sblst(nums_1, k_1))