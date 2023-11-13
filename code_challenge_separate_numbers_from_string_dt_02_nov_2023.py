# separate numbers from letters in the string

str_1 = 'abcdef1g23hijk456lmnop789q10rst123'
def sprt_nmbr_fr_str(str_1):
    dgts = []
    chrs = ''
    num = ''
    for i in str_1:
        if i.isdigit():
            num += i
        else:
            if num:
                dgts.append(num)
                num = ''
            else:
                chrs += i

    if num:
        dgts.append(num)

    return f'Dgts: {dgts}\nChrs: {chrs}'

print(sprt_nmbr_fr_str(str_1))