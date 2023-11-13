# reverse the string
# 1
# str_a = 'Write a function that scrapes the Caesars Sportsbook website'

# def rv_st(str_a):
#     return str_a[::-1]
#
# print(rv_st(str_a))

# 2
str_a = 'Write a function that scrapes the Caesars Sportsbook website'

def rv_st(str_a):
    return ''.join(reversed(str_a))

print(rv_st(str_a))