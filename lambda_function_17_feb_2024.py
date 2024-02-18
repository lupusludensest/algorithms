# lambda function

def take_odd(i):
    if i % 2 != 0:
        return True
    return False

l = [1, 5, 8, 12, 15]
new_l = list(filter(take_odd, l))
print(new_l)

evens = list(filter(lambda x: x % 2 == 0, l))
print(evens)

my_list = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
new_l_1 = list(filter(lambda item: isinstance(item, str) and 'a' in item, my_list))
print(new_l_1)

from functools import reduce
res_1 = reduce(lambda x, y: x + y, l)
print(res_1)