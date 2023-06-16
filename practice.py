a = 'String sample'
print(f'{a}, {type(a)}')

b = 123
print(f'{b}, {type(b)}')

c = 123.456
print(f'{c}, {type(c)}')

d = type(c) == float
print(f'{d}, {type(d)}')

e = 0.1
f = 0.2
e_f = e + f
print(f'{e_f}, {type(e_f)}')

lst_1 = [-1, 0, 1, 2, 3, 4, 5]
print(f'{lst_1}, {type(lst_1)}')
for i in lst_1:
    if i > 0:
        print(i, end=" ")

tuple_1 = ('a', False, 2, 8.6)
print(f'{tuple_1}, {type(tuple_1)}')

dict_1 = {1: 1.3, 1: 1.3, 'b': 'String', 'c': False, 'b': 'String', 'c': False,'d': [-1, 0, 1, 2, 3, 4, 5], 'e': (1, 2, 3, 4, 5), 'f': {'a', 2}, 'f': {'a', 2}}
print(f'{dict_1}, {type(dict_1)}')

set_1 = set(dict_1)
print(f'{set_1}, {type(set_1)}')

lst_1 = [-13, 30, 15, 62, 36, 46, 56]
lst_2 = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]
print(f'{len(lst_1)}, {len(lst_2)}')
# 1 case 7 * 56
# 2 case 56 * 7
# if case 2 it is more profitable to use the first case

tuple_1 = ('Great', 1, 1,2, (1, 3, '32'))
print(f'{tuple_1}, {type(tuple_1)}')













