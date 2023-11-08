# Disney interview 02 nov 2023, wednsday, Alexey Ternov 2nd degree Senior Software Development Lead
a_list = list(range(10))  # [0,1,2,...,9]
print(a_list)
# swap first and last items in the list -> [9,1,2,3...,0]

a_list[0], a_list[-1] = a_list[-1], a_list[0]

# print(a_list)
print(a_list[::-1]) # start stop step

# to_zip = 'aabbbcccd'  # archive / compress / zip the string ->   a2b3c3d1
#
#
# def zp_st(to_zip):
#     res = ''
#     seen = ''  # temp placeholder
#     for ch in to_zip:
#         if ch in seen:
#             seen += ch
#         else:
#             res += f'{seen[0]}{len(seen)}'
#             seen = ch
#     if seen:
#         res += f'{seen[0]}{len(seen)}'
#
#
# # a3b4c4
# print(zp_st(to_zip))

def compress_string(to_compress):
    compressed = ""
    prev = ""
    count = 0

    for char in to_compress:
        if char != prev:
            if prev:
                compressed += prev + str(count)
            count = 1
            prev = char
        else:
            count += 1

    if prev:
        compressed += prev + str(count)

    return compressed


to_compress = "aabbbcccd"
print(compress_string(to_compress))
# a2b3c3d1