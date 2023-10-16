# В заданном листе найти непрерывный подлист, сумма элементов в котором максимальна.
# TODO: Вывести саму подсумму largest_sum_continguous_sublist([5, -3, 4, -9, 2, -6])
#  выводит в ответ [5, -3, 4]

def largest_sum_contiguous_sublist(array):
    best_sum = 0
    current_sum = 0
    best_list = []
    current_list = []
    for i in array:
        current_sum += i
        if current_sum < 0:
            current_sum = 0
            current_list = []
        else:
            current_list.append(i)
            if current_sum > best_sum:
                best_sum = current_sum
                best_list = current_list

    return {
        "Best sum": best_sum,
        "Best list": best_list
    }

print(largest_sum_contiguous_sublist([5, -3, 4, -9, 2, -6]))

# def maxSubArray(nums):
#
#     # we are taking two varible total_sum and max_sum
#     # total_sum will take care of sum till every index and max_sum will the max(total_sum, max_sum)
#     total_sum = max_sum = nums[0]
#     # variable = 0
#     # output_list = []
#     # output_list.append(variable)
#     # for i in maxSubArray:
#
#     # in starting we are giving value to both total_sum and max_sum as value at index 0
#     for i in nums[1:]:  # looping the array starting from index 1
#
#         total_sum = max(i, total_sum + i)  # computing total sum
#         max_sum = max(total_sum, max_sum)  # updating max_sum if total_sum is larger than max_sum
#
#     return max_sum
#
# print(maxSubArray([5, -3, 4, -9, 2, -6]))
#
# # print(output_list)

# def largest_sum_contiguous_sublist(array): # declared function
#     best_sum = 0 # declared zero-counter for best_sum
#     current_sum = 0 # declared zero counter for current_sum
#
#     for item in array: # starting from the 0-index add next member to previous
#         current_sum += item
#         if current_sum < 0:
#             current_sum = 0 # if result is negative claim result as zero
#         else:
#             if current_sum > best_sum: # if result is bigger than previous best_sum claim new best_sum
#                 best_sum = current_sum
#     return best_sum # end of the iterations
#
#
# # output on the screen declared function with given argument [5, -3, 4, -9, 2, -6]
# print(f'Largest sum is: "{largest_sum_contiguous_sublist([5, -3, 4, -9, 2, -6])}".')
#
#
# import random
# a = [([(random.randint(1, 150)) for j in range(5)]) for i in range(5)]
# for i in a:
#     print(('{:<7}'*len(i)).format(*i))
# s = [sum(i) for i in a]
# print('Строка матрицы, сумма элементов которой наибольшая:',('{:<7}'*len(a[0])).format(*a[s.index(max(s), 0, len(a))]))

# В заданном листе найти непрерывный подлист сумма элементов в котором максимальна.
# def largest_sum_contiguous_sublist(array):
#     best_sum = 0
#     current_sum = 0
#     max_list = []
#     current_list = []
#     for i in array:
#         current_sum += i
#         if current_sum < 0:
#             current_sum = 0
#             current_list = []
#         else:
#             current_list.append(i)
#             if current_sum > best_sum:
#                 best_sum = current_sum
#                 max_list = current_list
#     return {
#         "Best sum: ": best_sum,
#         "Max list": max_list
#     }
# print(largest_sum_contiguous_sublist([5, -3, 4, -9, 2, -6]))

#TODO: Вывести саму подсумму largest_sum_contiguous_sublist([5, -3, 4, -9, 2, -6]) выводит в ответ [5, -3, 4]