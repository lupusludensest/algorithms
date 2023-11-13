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
