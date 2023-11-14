# extract the longest word from the string
# 1
# str_a = 'Write a function that scrapes the Caesars Sportsbook website'
# def lngst_wrd_str(str_a):
#     return max(str_a.split(), key = len)
#
# print(lngst_wrd_str(str_a))

# 2
str_a = 'Write a function that scrapes the Caesars Sportsbook website'
def lngst_wrd_str(str_a):
    lngst_wrd = ''
    for i in str_a.split():
        if len(i) > len(lngst_wrd):
            lngst_wrd = i

    return lngst_wrd

print(lngst_wrd_str(str_a))

# longest word from string by split and sort and key=len and index

str_1 = 'longest word from string'
def lngst_wrd_str(str_1):
    lst = list(str_1.split())
    lst.sort(key=len)
    return lst[-1]

print(lngst_wrd_str(str_1))
