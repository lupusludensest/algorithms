# Python code challenge. Find indexes of elements giving target sum.

lst_1 = [2, 7, 11, 15]  # 0, 1
target_1 = 9
lst_2 = [3, 2, 4]  # # 1, 2
target_2 = 6
lst_3 = [3, 3]  # 0, 1
target_3 = 6


# brute force
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            # compare values from both loops and their indexes are not the same
            if nums[i] + nums[j] == target and i != j:
                return f'{i},{j}'


print(two_sum(lst_1, target_1))
print(two_sum(lst_2, target_2))
print(two_sum(lst_3, target_3))


# faster way aka efficient way
def two_sum(nums, target):
    hash = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash:
            return [hash[diff], i]
        else:
            hash[num] = i


print(two_sum(lst_1, target_1))
print(two_sum(lst_2, target_2))
print(two_sum(lst_3, target_3))