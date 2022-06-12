# # Disney code interview dt 10 june 2022
# nums = [2,7,11,15]
# def wrkwlst(nums):
#     nlst=[]
#     nnlst=[]
#     for i in range(len(nums)):
#         if (nums[i-1] + nums[i]) == 9:
#             nlst.append(nums[i-1]), nlst.append(nums[i]),nnlst.append(i-1), nnlst.append(i)
#     return nlst, nnlst
# print(wrkwlst(nums))

# # Decimal to binary
# dec = int(input('Input decimal: '))
# bnr=''
# while dec > 0:
#     bnr += str(dec % 2)
#     dec = dec // 2
# bnr = bnr[::-1]
# print(bnr)

