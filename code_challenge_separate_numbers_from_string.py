# separate numbers from string
# 1
str_a = 's3t44r555i666n66g'
def spr_nmbrs_str(str_a):
    dgts = []
    num = ''
    chrs = ''
    for i in str_a:
        if i.isdigit():
            num += i
        else:
            if num:
                dgts.append(int(num))
                num = ''
            chrs += i
    if num:
        dgts.append(int(num))

    return f'Dgts: {dgts}\nChrs: {chrs}'

print(spr_nmbrs_str(str_a))

# 2
# import re
#
# str_a = 's3t44r555i666n66g'
# def spr_nmbrs_str(str_a):
#     nmbrs = re.findall(r'\d+', str_a)
#     ltrs = re.sub(r'\d+', '', str_a)
#     return nmbrs, ltrs
#
# print(spr_nmbrs_str(str_a))
