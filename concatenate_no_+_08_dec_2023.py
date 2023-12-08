# We have a two different string 'Wsdfgh' and 'Kjhgfdsdfg'. Write a function to concatenate the not usin "+".
# Use a ' ' between them.

# a = 'Wsdfgh'
# b = ' Kjhgfdsdfg'
# c = ' '
#
# def nct_strns(a, b, c):
#     return f'{a}{c}{b}'
#
# print(nct_strns(a, b, c))

a = 'Wsdfgh'
b = ' Kjhgfdsdfg'
c = ' '

def nct_strns(a, b, c):
    return '{}{}{}'.format(a, b, c)

print(nct_strns(a, b, c))