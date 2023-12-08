# define if a phrase even with non-alphanumeric chars is a palyndrome

import re

str_a = str(input('Enter the word: '))

def f_plndrm(str_a):
    # Remove non-alphanumeric characters
    str_a = re.sub(r'[\W_]+', '', str_a)
    print(str_a)

    # Decapitalize
    str_a = str_a.lower()
    print(str_a)

    # Reverse string
    rvrsd_str_a = str_a[::-1]

    if rvrsd_str_a == str_a:
        return f'Palindrome'
    return f'Not palindrome'


print(f_plndrm(str_a))
